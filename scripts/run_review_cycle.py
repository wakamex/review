#!/usr/bin/env python3
"""Run or plan repeated LLM review cycles for one paper.

The harness is artifact-driven: each follow-up cycle receives the paper bundle,
the reviewer's own previous JSON review, and the other reviewers' previous JSON
reviews explicitly. CLI session history is optional metadata, not source state.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from string import Template
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROVIDERS = "claude,codex,gemini"
SCORE_DIMENSIONS = [
    "technical_soundness",
    "novelty",
    "significance",
    "clarity",
    "reviewer_confidence",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-manifest", required=True, help="JSONL source manifest.")
    parser.add_argument("--paper-id", required=True, help="arXiv paper id.")
    parser.add_argument(
        "--papers-dir",
        default=None,
        help="Per-paper output directory root. Default: sibling papers/ under manifest directory.",
    )
    parser.add_argument(
        "--providers",
        default=DEFAULT_PROVIDERS,
        help=f"Comma-separated providers. Default: {DEFAULT_PROVIDERS}.",
    )
    parser.add_argument("--cycles", type=int, default=2, help="Review cycles. Default: 2.")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually run model CLIs. Default is dry-run prompt/command generation.",
    )
    parser.add_argument(
        "--build-bundle",
        action="store_true",
        help="Build bundle.md before running/planning.",
    )
    parser.add_argument(
        "--max-bundle-chars",
        type=int,
        default=140_000,
        help="Source text character cap when building bundle. Default: 140000.",
    )
    parser.add_argument(
        "--board",
        action="store_true",
        help="Plan/run final board synthesis after review cycles.",
    )
    parser.add_argument(
        "--overwrite-board",
        action="store_true",
        help="Overwrite only the board synthesis output; reviewer outputs are reused unless --overwrite is also set.",
    )
    parser.add_argument(
        "--score-source",
        choices=["mechanical", "board"],
        default="mechanical",
        help=(
            "Selected final score source. 'mechanical' uses the final-cycle "
            "reviewer average; 'board' uses board_score_10 only for legacy "
            "scoring board artifacts. Default: mechanical."
        ),
    )
    parser.add_argument("--claude-model", default="sonnet", help="Claude model alias/id.")
    parser.add_argument("--codex-model", default=None, help="Optional Codex model id.")
    parser.add_argument("--gemini-model", default=None, help="Optional Gemini model id.")
    parser.add_argument("--timeout", type=int, default=900, help="Per-call timeout seconds.")
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop on the first provider or board error. Default: record the error and continue.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs.")
    return parser.parse_args()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def load_template(path: Path) -> Template:
    return Template(path.read_text(encoding="utf-8"))


def default_papers_dir(source_manifest: Path) -> Path:
    return source_manifest.parent / "papers"


def build_bundle(args: argparse.Namespace, papers_dir: Path) -> Path:
    bundle_path = papers_dir / args.paper_id / "bundle.md"
    if bundle_path.exists() and not args.overwrite:
        return bundle_path
    command = [
        sys.executable,
        str(ROOT / "scripts" / "build_review_bundle.py"),
        "--source-manifest",
        args.source_manifest,
        "--paper-id",
        args.paper_id,
        "--papers-dir",
        str(papers_dir),
        "--max-chars",
        str(args.max_bundle_chars),
    ]
    if args.overwrite:
        command.append("--overwrite")
    subprocess.run(command, check=True)
    return bundle_path


def command_preview(provider: str, schema_path: Path, args: argparse.Namespace) -> list[str]:
    if provider == "claude":
        return [
            "env",
            "-u",
            "CLAUDECODE",
            "claude",
            "-p",
            "--tools",
            "",
            "--no-session-persistence",
            "--output-format",
            "json",
            "--json-schema",
            f"$(cat {schema_path})",
            "--model",
            args.claude_model,
        ]
    if provider == "codex":
        command = [
            "codex",
            "exec",
            "--json",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--skip-git-repo-check",
            "--output-schema",
            str(schema_path),
            "-",
        ]
        if args.codex_model:
            command[2:2] = ["--model", args.codex_model]
        return command
    if provider == "gemini":
        command = [
            "gemini",
            "-p",
            "Follow the instructions from stdin. Return only the requested JSON.",
            "--approval-mode",
            "plan",
            "--output-format",
            "json",
        ]
        if args.gemini_model:
            command[1:1] = ["--model", args.gemini_model]
        return command
    raise ValueError(f"unknown provider: {provider}")


def run_subprocess(command: list[str], prompt: str, timeout: int, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        timeout=timeout,
        env=env,
        cwd=ROOT,
    )


def parse_jsonish(text: str) -> Any:
    text = text.strip()
    if not text:
        raise ValueError("empty model output")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match_start = text.find("{")
    match_end = text.rfind("}")
    if match_start >= 0 and match_end > match_start:
        return json.loads(text[match_start : match_end + 1])
    raise ValueError("could not parse JSON from model output")


def execute_provider(provider: str, prompt: str, schema_path: Path, out_dir: Path, args: argparse.Namespace) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    schema_text = schema_path.read_text(encoding="utf-8")
    result_file = out_dir / f"{provider}.json"

    if provider == "claude":
        command = [
            "claude",
            "-p",
            "--tools",
            "",
            "--no-session-persistence",
            "--output-format",
            "json",
            "--json-schema",
            schema_text,
            "--model",
            args.claude_model,
        ]
        env = {key: value for key, value in os.environ.items() if key != "CLAUDECODE"}
        completed = run_subprocess(command, prompt, args.timeout, env=env)
        (out_dir / f"{provider}.stdout.json").write_text(completed.stdout, encoding="utf-8")
        (out_dir / f"{provider}.stderr.txt").write_text(completed.stderr, encoding="utf-8")
        if completed.returncode != 0:
            raise RuntimeError(f"claude exited {completed.returncode}: {completed.stderr.strip()}")
        wrapper = json.loads(completed.stdout)
        if wrapper.get("is_error"):
            raise RuntimeError(str(wrapper.get("result") or "claude returned is_error=true"))
        if "structured_output" in wrapper and wrapper["structured_output"] is not None:
            parsed = wrapper["structured_output"]
        else:
            payload = wrapper.get("result", wrapper)
            parsed = payload if isinstance(payload, dict) else parse_jsonish(str(payload))
        write_json(result_file, parsed)
        write_json(out_dir / f"{provider}.usage.json", wrapper)
        return parsed

    if provider == "codex":
        command = [
            "codex",
            "exec",
            "--json",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--skip-git-repo-check",
            "--output-schema",
            str(schema_path),
            "-",
        ]
        if args.codex_model:
            command[2:2] = ["--model", args.codex_model]
        completed = run_subprocess(command, prompt, args.timeout)
        (out_dir / f"{provider}.jsonl").write_text(completed.stdout, encoding="utf-8")
        (out_dir / f"{provider}.stderr.txt").write_text(completed.stderr, encoding="utf-8")
        if completed.returncode != 0:
            raise RuntimeError(f"codex exited {completed.returncode}: {completed.stderr.strip()}")
        final_text = ""
        usage = None
        thread_id = None
        for line in completed.stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") == "thread.started":
                thread_id = event.get("thread_id")
            if event.get("type") == "item.completed":
                item = event.get("item") or {}
                if item.get("type") == "agent_message":
                    final_text = item.get("text", "")
            if event.get("type") == "turn.completed":
                usage = event.get("usage")
        parsed = parse_jsonish(final_text)
        write_json(result_file, parsed)
        write_json(out_dir / f"{provider}.usage.json", {"thread_id": thread_id, "usage": usage})
        return parsed

    if provider == "gemini":
        command = [
            "gemini",
            "-p",
            "Follow the instructions from stdin. Return only the requested JSON.",
            "--approval-mode",
            "plan",
            "--output-format",
            "json",
        ]
        if args.gemini_model:
            command[1:1] = ["--model", args.gemini_model]
        completed = run_subprocess(command, prompt, args.timeout)
        (out_dir / f"{provider}.stdout.json").write_text(completed.stdout, encoding="utf-8")
        (out_dir / f"{provider}.stderr.txt").write_text(completed.stderr, encoding="utf-8")
        if completed.returncode != 0:
            raise RuntimeError(f"gemini exited {completed.returncode}: {completed.stderr.strip()}")
        wrapper = parse_jsonish(completed.stdout)
        if isinstance(wrapper, dict) and "response" in wrapper:
            parsed = parse_jsonish(str(wrapper["response"]))
        elif isinstance(wrapper, dict) and "text" in wrapper:
            parsed = parse_jsonish(str(wrapper["text"]))
        else:
            parsed = wrapper
        write_json(result_file, parsed)
        return parsed

    raise ValueError(f"unknown provider: {provider}")


def provider_review_path(paper_dir: Path, cycle: int, provider: str) -> Path:
    return paper_dir / "review_cycles" / f"cycle_{cycle:02d}" / "reviews" / f"{provider}.json"


def load_previous_reviews(paper_dir: Path, cycle: int, provider: str, providers: list[str]) -> tuple[str, str]:
    if cycle <= 1:
        return "{}", "[]"
    prior_cycle = cycle - 1
    own_path = provider_review_path(paper_dir, prior_cycle, provider)
    if own_path.exists():
        own = own_path.read_text(encoding="utf-8")
    else:
        own = json.dumps({"missing": str(own_path), "dry_run_note": "prior review not available yet"}, indent=2)
    others = []
    for other_provider in providers:
        if other_provider == provider:
            continue
        path = provider_review_path(paper_dir, prior_cycle, other_provider)
        if path.exists():
            others.append({"reviewer": other_provider, "review": read_json(path)})
        else:
            others.append(
                {
                    "reviewer": other_provider,
                    "missing": str(path),
                    "dry_run_note": "prior review not available yet",
                }
            )
    return own, json.dumps(others, indent=2, sort_keys=True)


def render_review_prompt(
    paper_id: str,
    reviewer: str,
    cycle: int,
    providers: list[str],
    paper_dir: Path,
    bundle: str,
    schema: str,
) -> str:
    if cycle == 1:
        template = load_template(ROOT / "prompts" / "reviewer_initial.md")
        return template.substitute(
            paper_id=paper_id,
            reviewer=reviewer,
            cycle=cycle,
            schema=schema,
            bundle=bundle,
        )
    own, others = load_previous_reviews(paper_dir, cycle, reviewer, providers)
    template = load_template(ROOT / "prompts" / "reviewer_followup.md")
    return template.substitute(
        paper_id=paper_id,
        reviewer=reviewer,
        cycle=cycle,
        schema=schema,
        bundle=bundle,
        own_previous_review=own,
        other_reviews=others,
    )


def write_plan_artifacts(
    out_dir: Path,
    provider: str,
    prompt: str,
    schema_path: Path,
    args: argparse.Namespace,
    phase: str,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{provider}.prompt.md").write_text(prompt, encoding="utf-8")
    write_json(
        out_dir / f"{provider}.command.json",
        {
            "provider": provider,
            "phase": phase,
            "execute": args.execute,
            "command_preview": command_preview(provider, schema_path, args),
            "prompt_sha256": sha256_text(prompt),
            "schema_path": str(schema_path),
        },
    )


def write_error_artifact(
    out_dir: Path,
    provider: str,
    phase: str,
    prompt_path: Path,
    schema_path: Path,
    exc: Exception,
) -> Path:
    error_path = out_dir / f"{provider}.error.json"
    write_json(
        error_path,
        {
            "provider": provider,
            "phase": phase,
            "status": "error",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "prompt_path": str(prompt_path),
            "schema_path": str(schema_path),
            "created_at": utc_now(),
        },
    )
    return error_path


def collect_review_artifacts(paper_dir: Path, cycles: int, providers: list[str]) -> list[dict[str, Any]]:
    artifacts = []
    for cycle in range(1, cycles + 1):
        for provider in providers:
            path = provider_review_path(paper_dir, cycle, provider)
            error_path = path.with_suffix(".error.json")
            artifacts.append(
                {
                    "cycle": cycle,
                    "reviewer": provider,
                    "path": str(path),
                    "review": read_json(path) if path.exists() else None,
                    "missing": not path.exists(),
                    "error_path": str(error_path) if error_path.exists() else None,
                    "error": read_json(error_path) if error_path.exists() else None,
                }
            )
    return artifacts


def render_board_prompt(
    paper_id: str,
    bundle: str,
    schema: str,
    artifacts: list[dict[str, Any]],
    mechanical_context: dict[str, Any],
) -> str:
    template = load_template(ROOT / "prompts" / "board_synthesis.md")
    return template.substitute(
        paper_id=paper_id,
        schema=schema,
        bundle=bundle,
        mechanical_context=json.dumps(mechanical_context, indent=2, sort_keys=True),
        review_artifacts=json.dumps(artifacts, indent=2, sort_keys=True),
    )


def compact_review_score(review: dict[str, Any]) -> dict[str, Any]:
    return {
        "overall_score_10": review.get("overall_score_10"),
        "dimension_scores": review.get("dimension_scores"),
    }


def compact_board_score(board: dict[str, Any]) -> dict[str, Any]:
    return {
        "final_verdict": board.get("final_verdict"),
        "confidence": board.get("confidence"),
        "board_score_10": board.get("board_score_10"),
        "dimension_scores": board.get("dimension_scores"),
    }


def compact_summarizer_result(board: dict[str, Any]) -> dict[str, Any]:
    return {
        "general_reader_takeaway": board.get("general_reader_takeaway"),
        "technical_takeaway": board.get("technical_takeaway"),
    }


def average_review_scores(reviews: list[dict[str, Any]]) -> dict[str, Any]:
    overall_values = [
        review["overall_score_10"]
        for review in reviews
        if isinstance(review.get("overall_score_10"), (int, float))
    ]
    dimension_scores = {}
    for dimension in SCORE_DIMENSIONS:
        values = []
        for review in reviews:
            value = (review.get("dimension_scores") or {}).get(dimension)
            if isinstance(value, (int, float)):
                values.append(value)
        if values:
            dimension_scores[dimension] = round(sum(values) / len(values), 3)

    average: dict[str, Any] = {}
    if overall_values:
        average["overall_score_10"] = round(sum(overall_values) / len(overall_values), 3)
    if dimension_scores:
        average["dimension_scores"] = dimension_scores
    return average


def board_delta(board: dict[str, Any], average: dict[str, Any]) -> dict[str, Any]:
    delta: dict[str, Any] = {}
    if isinstance(board.get("board_score_10"), (int, float)) and isinstance(
        average.get("overall_score_10"),
        (int, float),
    ):
        delta["score_10"] = round(board["board_score_10"] - average["overall_score_10"], 3)

    board_dimensions = board.get("dimension_scores") or {}
    average_dimensions = average.get("dimension_scores") or {}
    dimension_delta = {}
    for dimension in SCORE_DIMENSIONS:
        board_value = board_dimensions.get(dimension)
        average_value = average_dimensions.get(dimension)
        if isinstance(board_value, (int, float)) and isinstance(average_value, (int, float)):
            dimension_delta[dimension] = round(board_value - average_value, 3)
    if dimension_delta:
        delta["dimension_scores"] = dimension_delta
    return delta


def selected_mechanical_score(review_cycles: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not review_cycles:
        return None
    final_cycle = review_cycles[-1]
    average = final_cycle.get("mechanical_average")
    if not average:
        return None
    return {
        "source": "mechanical",
        "cycle": final_cycle.get("cycle"),
        "overall_score_10": average.get("overall_score_10"),
        "dimension_scores": average.get("dimension_scores"),
    }


def selected_board_score(board: dict[str, Any] | None) -> dict[str, Any] | None:
    if not board or not isinstance(board.get("board_score_10"), (int, float)):
        return None
    return {
        "source": "board",
        "reviewer": board.get("reviewer"),
        "overall_score_10": board.get("board_score_10"),
        "dimension_scores": board.get("dimension_scores"),
        "final_verdict": board.get("final_verdict"),
        "confidence": board.get("confidence"),
    }


def collect_score_summary(
    paper_dir: Path,
    cycles: int,
    providers: list[str],
    board_provider: str | None,
    score_source: str,
) -> dict[str, Any]:
    review_cycles = []
    for cycle in range(1, cycles + 1):
        reviews = []
        for provider in providers:
            path = provider_review_path(paper_dir, cycle, provider)
            if not path.exists():
                continue
            reviews.append({"reviewer": provider, **compact_review_score(read_json(path))})
        if reviews:
            cycle_summary = {"cycle": cycle, "reviews": reviews}
            average = average_review_scores(reviews)
            if average:
                cycle_summary["mechanical_average"] = average
            review_cycles.append(cycle_summary)

    score_summary: dict[str, Any] = {"review_cycles": review_cycles}
    if board_provider:
        board_path = paper_dir / "board" / f"{board_provider}.json"
        if board_path.exists():
            board_result = read_json(board_path)
            if "board_score_10" in board_result:
                board = {"reviewer": board_provider, **compact_board_score(board_result)}
                score_summary["board"] = board
            else:
                board = None
                score_summary["summarizer"] = {"reviewer": board_provider, **compact_summarizer_result(board_result)}
            if board and review_cycles:
                final_average = review_cycles[-1].get("mechanical_average")
                if final_average:
                    score_summary["final_cycle_mechanical_average"] = final_average
                    delta = board_delta(board, final_average)
                    if delta:
                        score_summary["board_delta_vs_final_cycle_mechanical_average"] = delta
    if review_cycles and "final_cycle_mechanical_average" not in score_summary:
        final_average = review_cycles[-1].get("mechanical_average")
        if final_average:
            score_summary["final_cycle_mechanical_average"] = final_average
    score_summary["selected_score_source"] = score_source
    if score_source == "mechanical":
        selected = selected_mechanical_score(review_cycles)
    else:
        selected = selected_board_score(score_summary.get("board"))
    if selected:
        score_summary["selected_final_score"] = selected
    else:
        score_summary["selected_final_score_error"] = f"{score_source} score unavailable"
    return score_summary


def main() -> int:
    args = parse_args()
    if args.cycles < 1:
        raise SystemExit("--cycles must be >= 1")
    providers = [provider.strip() for provider in args.providers.split(",") if provider.strip()]
    unknown = [provider for provider in providers if provider not in {"claude", "codex", "gemini"}]
    if unknown:
        raise SystemExit(f"unknown provider(s): {', '.join(unknown)}")
    if args.score_source == "board" and not args.board:
        raise SystemExit("--score-source board requires --board")

    source_manifest = Path(args.source_manifest)
    papers_dir = Path(args.papers_dir) if args.papers_dir else default_papers_dir(source_manifest)
    paper_dir = papers_dir / args.paper_id
    if args.build_bundle or not (paper_dir / "bundle.md").exists():
        bundle_path = build_bundle(args, papers_dir)
    else:
        bundle_path = paper_dir / "bundle.md"
    bundle = bundle_path.read_text(encoding="utf-8")
    review_schema_path = ROOT / "schemas" / "review.schema.json"
    board_schema_path = ROOT / "schemas" / "board.schema.json"
    review_schema = review_schema_path.read_text(encoding="utf-8")
    board_schema = board_schema_path.read_text(encoding="utf-8")

    summary: dict[str, Any] = {
        "paper_id": args.paper_id,
        "paper_dir": str(paper_dir),
        "bundle_path": str(bundle_path),
        "bundle_sha256": sha256_text(bundle),
        "providers": providers,
        "cycles": args.cycles,
        "execute": args.execute,
        "score_source": args.score_source,
        "board_role": "summarizer" if args.board else None,
        "calls": [],
    }

    for cycle in range(1, args.cycles + 1):
        for provider in providers:
            out_dir = paper_dir / "review_cycles" / f"cycle_{cycle:02d}" / "reviews"
            result_path = out_dir / f"{provider}.json"
            prompt = render_review_prompt(args.paper_id, provider, cycle, providers, paper_dir, bundle, review_schema)
            write_plan_artifacts(out_dir, provider, prompt, review_schema_path, args, f"cycle_{cycle:02d}")
            call_summary = {
                "cycle": cycle,
                "provider": provider,
                "result_path": str(result_path),
                "prompt_path": str(out_dir / f"{provider}.prompt.md"),
            }
            if args.execute:
                if result_path.exists() and not args.overwrite:
                    call_summary["status"] = "exists"
                else:
                    try:
                        execute_provider(provider, prompt, review_schema_path, out_dir, args)
                        call_summary["status"] = "ok"
                    except Exception as exc:  # noqa: BLE001 - preserve partial run.
                        call_summary["status"] = "error"
                        call_summary["error"] = str(exc)
                        call_summary["error_path"] = str(
                            write_error_artifact(
                                out_dir,
                                provider,
                                f"cycle_{cycle:02d}",
                                out_dir / f"{provider}.prompt.md",
                                review_schema_path,
                                exc,
                            )
                        )
                        summary["calls"].append(call_summary)
                        if args.stop_on_error:
                            write_json(paper_dir / "review_run_summary.json", summary)
                            return 1
                        continue
            else:
                call_summary["status"] = "planned"
            summary["calls"].append(call_summary)

    if args.board:
        board_dir = paper_dir / "board"
        board_dir.mkdir(parents=True, exist_ok=True)
        artifacts = collect_review_artifacts(paper_dir, args.cycles, providers)
        mechanical_context = collect_score_summary(paper_dir, args.cycles, providers, None, "mechanical")
        board_prompt = render_board_prompt(args.paper_id, bundle, board_schema, artifacts, mechanical_context)
        provider = providers[0]
        write_plan_artifacts(board_dir, provider, board_prompt, board_schema_path, args, "board")
        board_result_path = board_dir / f"{provider}.json"
        if args.execute:
            if board_result_path.exists() and not (args.overwrite or args.overwrite_board):
                summary["board"] = {"status": "exists", "provider": provider, "path": str(board_result_path)}
            else:
                try:
                    execute_provider(provider, board_prompt, board_schema_path, board_dir, args)
                    summary["board"] = {"status": "ok", "provider": provider, "path": str(board_result_path)}
                except Exception as exc:  # noqa: BLE001 - preserve partial run.
                    error_path = write_error_artifact(
                        board_dir,
                        provider,
                        "board",
                        board_dir / f"{provider}.prompt.md",
                        board_schema_path,
                        exc,
                    )
                    summary["board"] = {
                        "status": "error",
                        "provider": provider,
                        "path": str(board_result_path),
                        "error": str(exc),
                        "error_path": str(error_path),
                    }
                    if args.stop_on_error:
                        write_json(paper_dir / "review_run_summary.json", summary)
                        return 1
        else:
            summary["board"] = {
                "status": "planned",
                "provider": provider,
                "prompt_path": str(board_dir / f"{provider}.prompt.md"),
            }

    board_provider = summary.get("board", {}).get("provider") if isinstance(summary.get("board"), dict) else None
    score_summary = collect_score_summary(paper_dir, args.cycles, providers, board_provider, args.score_source)
    if score_summary["review_cycles"] or score_summary.get("board"):
        summary["score_summary"] = score_summary

    write_json(paper_dir / "review_run_summary.json", summary)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
