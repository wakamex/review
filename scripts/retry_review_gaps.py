#!/usr/bin/env python3
"""Retry missing review artifacts with exponential backoff."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROVIDERS = "claude,codex,gemini"


@dataclass(frozen=True)
class RunConfig:
    run_dir: Path
    manifest: Path
    source_manifest: Path
    papers_dir: Path


@dataclass(frozen=True)
class Gap:
    paper_id: str
    cycle: int
    provider: str
    review_path: Path
    error_path: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--run-dir",
        action="append",
        required=True,
        help="Review run directory containing manifest.jsonl, source_manifest.jsonl, and papers/. May be repeated.",
    )
    parser.add_argument("--providers", default=DEFAULT_PROVIDERS, help=f"Comma-separated providers. Default: {DEFAULT_PROVIDERS}.")
    parser.add_argument("--cycles", type=int, default=2, help="Review cycles expected per provider. Default: 2.")
    parser.add_argument("--attempts", type=int, default=5, help="Maximum attempts per gap scan. Default: 5.")
    parser.add_argument("--initial-delay", type=float, default=120.0, help="Initial retry delay in seconds. Default: 120.")
    parser.add_argument("--max-delay", type=float, default=3600.0, help="Maximum retry delay in seconds. Default: 3600.")
    parser.add_argument("--backoff", type=float, default=2.0, help="Delay multiplier after each pass. Default: 2.")
    parser.add_argument("--timeout", type=int, default=1200, help="Per-model timeout passed to run_review_cycle.py. Default: 1200.")
    parser.add_argument("--paper-id", action="append", help="Only retry these paper ids. May be repeated.")
    parser.add_argument("--max-papers", type=int, help="Retry at most this many currently gappy papers per pass.")
    parser.add_argument("--sleep-between-papers", type=float, default=0.0, help="Sleep between paper commands. Default: 0.")
    parser.add_argument("--execute", action="store_true", help="Actually run model CLIs. Without this, only write the plan.")
    parser.add_argument("--refresh-board", action=argparse.BooleanOptionalAction, default=True, help="Refresh board summaries after a paper has no remaining gaps. Default: true.")
    parser.add_argument("--log-dir", help="Retry log directory. Default: first run_dir/batch_logs/retry-gaps-<timestamp>.")
    parser.add_argument("--report-only", action="store_true", help="Only report current gaps, do not retry.")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def stamp() -> str:
    return datetime.now(UTC).strftime("%Y%m%d-%H%M%S")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def emit(value: object) -> None:
    print(json.dumps(value), flush=True)


def read_manifest_ids(path: Path) -> list[str]:
    ids = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        ids.append(str(row["arxiv_id"]))
    return ids


def infer_run_config(run_dir: Path) -> RunConfig:
    manifest = run_dir / "manifest.jsonl"
    source_manifest = run_dir / "source_manifest.jsonl"
    papers_dir = run_dir / "papers"
    missing = [path for path in (manifest, source_manifest, papers_dir) if not path.exists()]
    if missing:
        raise SystemExit(f"{run_dir} is not a complete run directory; missing: {', '.join(str(path) for path in missing)}")
    return RunConfig(run_dir=run_dir, manifest=manifest, source_manifest=source_manifest, papers_dir=papers_dir)


def provider_list(value: str) -> list[str]:
    providers = [provider.strip() for provider in value.split(",") if provider.strip()]
    if not providers:
        raise SystemExit("--providers cannot be empty")
    return providers


def gap_for(config: RunConfig, paper_id: str, cycle: int, provider: str) -> Gap | None:
    review_path = config.papers_dir / paper_id / "review_cycles" / f"cycle_{cycle:02d}" / "reviews" / f"{provider}.json"
    if review_path.exists():
        return None
    return Gap(
        paper_id=paper_id,
        cycle=cycle,
        provider=provider,
        review_path=review_path,
        error_path=review_path.with_suffix(".error.json"),
    )


def scan_gaps(
    config: RunConfig,
    providers: list[str],
    cycles: int,
    paper_filter: set[str] | None,
) -> list[Gap]:
    gaps: list[Gap] = []
    for paper_id in read_manifest_ids(config.manifest):
        if paper_filter is not None and paper_id not in paper_filter:
            continue
        for cycle in range(1, cycles + 1):
            for provider in providers:
                gap = gap_for(config, paper_id, cycle, provider)
                if gap is not None:
                    gaps.append(gap)
    return gaps


def group_papers(gaps: list[Gap], max_papers: int | None) -> list[str]:
    seen: set[str] = set()
    papers = []
    for gap in gaps:
        if gap.paper_id in seen:
            continue
        seen.add(gap.paper_id)
        papers.append(gap.paper_id)
        if max_papers is not None and len(papers) >= max_papers:
            break
    return papers


def command_for(
    config: RunConfig,
    paper_id: str,
    providers: list[str],
    cycles: int,
    timeout: int,
    execute: bool,
    refresh_board: bool,
) -> list[str]:
    command = [
        sys.executable,
        str(ROOT / "scripts" / "run_review_cycle.py"),
        "--source-manifest",
        str(config.source_manifest),
        "--papers-dir",
        str(config.papers_dir),
        "--paper-id",
        paper_id,
        "--providers",
        ",".join(providers),
        "--cycles",
        str(cycles),
        "--timeout",
        str(timeout),
        "--build-bundle",
        "--board",
    ]
    if execute:
        command.append("--execute")
    if refresh_board:
        command.append("--overwrite-board")
    return command


def run_command(command: list[str], log_dir: Path, label: str, execute: bool) -> dict[str, Any]:
    record = {
        "label": label,
        "command": command,
        "execute": execute,
        "started_at": utc_now(),
    }
    write_json(log_dir / f"{label}.command.json", record)
    if not execute:
        record.update({"finished_at": utc_now(), "status": "planned", "returncode": None})
        write_json(log_dir / f"{label}.result.json", record)
        return record

    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    (log_dir / f"{label}.stdout.txt").write_text(completed.stdout, encoding="utf-8")
    (log_dir / f"{label}.stderr.txt").write_text(completed.stderr, encoding="utf-8")
    record.update(
        {
            "finished_at": utc_now(),
            "status": "ok" if completed.returncode == 0 else "error",
            "returncode": completed.returncode,
        }
    )
    write_json(log_dir / f"{label}.result.json", record)
    return record


def gap_summary(config: RunConfig, gaps: list[Gap]) -> dict[str, Any]:
    by_paper: dict[str, list[dict[str, Any]]] = {}
    for gap in gaps:
        by_paper.setdefault(gap.paper_id, []).append(
            {
                "cycle": gap.cycle,
                "provider": gap.provider,
                "review_path": str(gap.review_path),
                "error_path": str(gap.error_path) if gap.error_path.exists() else None,
            }
        )
    return {
        "run_dir": str(config.run_dir),
        "gap_count": len(gaps),
        "paper_count": len(by_paper),
        "papers": by_paper,
    }


def retry_run(config: RunConfig, args: argparse.Namespace, providers: list[str], log_root: Path) -> dict[str, Any]:
    paper_filter = set(args.paper_id) if args.paper_id else None
    delay = args.initial_delay
    records: list[dict[str, Any]] = []
    final_gaps: list[Gap] = []

    for attempt in range(1, args.attempts + 1):
        gaps = scan_gaps(config, providers, args.cycles, paper_filter)
        final_gaps = gaps
        attempt_dir = log_root / safe_name(config.run_dir) / f"attempt-{attempt:02d}"
        write_json(attempt_dir / "gaps_before.json", gap_summary(config, gaps))
        emit({"event": "gap_scan", "run_dir": str(config.run_dir), "attempt": attempt, "gaps": len(gaps), "papers": len(group_papers(gaps, None))})
        if not gaps:
            break
        if args.report_only:
            break

        papers = group_papers(gaps, args.max_papers)
        for index, paper_id in enumerate(papers, start=1):
            paper_dir = attempt_dir / paper_id
            command = command_for(
                config=config,
                paper_id=paper_id,
                providers=providers,
                cycles=args.cycles,
                timeout=args.timeout,
                execute=args.execute,
                refresh_board=False,
            )
            emit({"event": "paper_retry_started", "run_dir": str(config.run_dir), "attempt": attempt, "index": index, "total": len(papers), "paper_id": paper_id})
            record = run_command(command, paper_dir, "retry", args.execute)
            after = [gap for gap in scan_gaps(config, providers, args.cycles, {paper_id}) if gap.paper_id == paper_id]
            write_json(paper_dir / "gaps_after_retry.json", gap_summary(config, after))
            record["remaining_gap_count"] = len(after)
            records.append(record)
            emit({"event": "paper_retry_finished", "run_dir": str(config.run_dir), "attempt": attempt, "paper_id": paper_id, "remaining_gaps": len(after), "returncode": record["returncode"]})

            if args.refresh_board and not after:
                board_command = command_for(
                    config=config,
                    paper_id=paper_id,
                    providers=providers,
                    cycles=args.cycles,
                    timeout=args.timeout,
                    execute=args.execute,
                    refresh_board=True,
                )
                board_record = run_command(board_command, paper_dir, "refresh-board", args.execute)
                records.append(board_record)
                emit({"event": "board_refresh_finished", "run_dir": str(config.run_dir), "attempt": attempt, "paper_id": paper_id, "returncode": board_record["returncode"]})

            if args.sleep_between_papers and index < len(papers):
                time.sleep(args.sleep_between_papers)

        gaps_after_pass = scan_gaps(config, providers, args.cycles, paper_filter)
        final_gaps = gaps_after_pass
        write_json(attempt_dir / "gaps_after.json", gap_summary(config, gaps_after_pass))
        if not gaps_after_pass:
            break
        if attempt < args.attempts and args.execute:
            sleep_for = min(delay, args.max_delay)
            emit({"event": "backoff_sleep", "run_dir": str(config.run_dir), "attempt": attempt, "seconds": sleep_for, "remaining_gaps": len(gaps_after_pass)})
            time.sleep(sleep_for)
            delay = min(delay * args.backoff, args.max_delay)

    final = gap_summary(config, scan_gaps(config, providers, args.cycles, paper_filter))
    final["records"] = records
    write_json(log_root / safe_name(config.run_dir) / "final_status.json", final)
    return final


def safe_name(path: Path) -> str:
    return "-".join(part for part in path.parts if part not in {".", "/"})


def main() -> int:
    args = parse_args()
    providers = provider_list(args.providers)
    configs = [infer_run_config(Path(run_dir)) for run_dir in args.run_dir]
    if args.attempts < 1:
        raise SystemExit("--attempts must be >= 1")

    default_log_root = configs[0].run_dir / "batch_logs" / f"retry-gaps-{stamp()}"
    log_root = Path(args.log_dir) if args.log_dir else default_log_root
    log_root.mkdir(parents=True, exist_ok=True)
    write_json(
        log_root / "run_config.json",
        {
            "created_at": utc_now(),
            "execute": args.execute,
            "report_only": args.report_only,
            "providers": providers,
            "cycles": args.cycles,
            "attempts": args.attempts,
            "initial_delay": args.initial_delay,
            "max_delay": args.max_delay,
            "backoff": args.backoff,
            "timeout": args.timeout,
            "run_dirs": [str(config.run_dir) for config in configs],
        },
    )

    results = []
    for config in configs:
        results.append(retry_run(config, args, providers, log_root))
    write_json(log_root / "final_status.json", {"updated_at": utc_now(), "runs": results})
    total_gaps = sum(int(result["gap_count"]) for result in results)
    emit({"event": "retry_gaps_finished", "log_dir": str(log_root), "remaining_gaps": total_gaps})
    return 0 if total_gaps == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
