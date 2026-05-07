#!/usr/bin/env python3
"""Smoke-test local model CLIs used by the review pipeline.

By default this only checks that commands exist and their help output runs.
Use --execute to run tiny paid/model-backed prompts.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from dataclasses import dataclass


@dataclass
class Check:
    name: str
    path: str | None
    help_ok: bool | None = None
    execute_ok: bool | None = None
    output_excerpt: str | None = None
    error: str | None = None


def run(args: list[str], timeout: int = 60, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        capture_output=True,
        text=True,
        timeout=timeout,
        env=env,
    )


def check_help(name: str, path: str) -> bool:
    result = run([path, "--help"], timeout=20)
    return result.returncode == 0 and "Usage" in result.stdout + result.stderr


def excerpt(value: str, limit: int = 500) -> str:
    value = value.strip()
    return value[:limit] + ("..." if len(value) > limit else "")


def execute_claude(path: str) -> tuple[bool, str]:
    env = {key: value for key, value in os.environ.items() if key != "CLAUDECODE"}
    result = run(
        [
            path,
            "-p",
            "Return exactly: ok",
            "--tools",
            "",
            "--no-session-persistence",
            "--output-format",
            "json",
            "--model",
            "sonnet",
            "--max-budget-usd",
            "0.05",
        ],
        timeout=120,
        env=env,
    )
    if result.returncode != 0:
        return False, result.stderr
    try:
        data = json.loads(result.stdout)
        return data.get("result", "").strip() == "ok", result.stdout
    except json.JSONDecodeError:
        return result.stdout.strip() == "ok", result.stdout


def execute_codex(path: str) -> tuple[bool, str]:
    result = run(
        [
            path,
            "exec",
            "--json",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--skip-git-repo-check",
            "Return exactly: ok",
        ],
        timeout=120,
    )
    if result.returncode != 0:
        return False, result.stderr
    ok = False
    for line in result.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item") or {}
        if event.get("type") == "item.completed" and item.get("text", "").strip() == "ok":
            ok = True
    return ok, result.stdout


def execute_gemini(path: str) -> tuple[bool, str]:
    result = run(
        [
            path,
            "-p",
            "Return exactly: ok",
            "--approval-mode",
            "plan",
            "--output-format",
            "json",
        ],
        timeout=120,
    )
    if result.returncode != 0:
        return False, result.stderr
    return "ok" in result.stdout.lower(), result.stdout


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Run tiny model-backed prompts. This may spend API credits/tokens.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checks = []
    executors = {
        "claude": execute_claude,
        "codex": execute_codex,
        "gemini": execute_gemini,
    }

    for name in ("claude", "codex", "gemini"):
        path = shutil.which(name)
        check = Check(name=name, path=path)
        if not path:
            check.error = "not found on PATH"
            checks.append(check)
            continue
        try:
            check.help_ok = check_help(name, path)
            if args.execute:
                ok, output = executors[name](path)
                check.execute_ok = ok
                check.output_excerpt = excerpt(output)
        except Exception as exc:  # noqa: BLE001 - diagnostic script.
            check.error = str(exc)
        checks.append(check)

    print(json.dumps([check.__dict__ for check in checks], indent=2, sort_keys=True))
    return 1 if any(check.error or check.help_ok is False or check.execute_ok is False for check in checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
