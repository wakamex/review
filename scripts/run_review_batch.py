#!/usr/bin/env python3
"""Run or resume review cycles for every paper in a JSONL manifest."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, help="Filtered arXiv manifest used for paper order.")
    parser.add_argument("--source-manifest", required=True, help="Review source manifest.")
    parser.add_argument("--papers-dir", required=True, help="Per-paper review output directory.")
    parser.add_argument("--log-dir", required=True, help="Batch logs directory.")
    parser.add_argument("--providers", default="claude,codex,gemini", help="Providers passed to run_review_cycle.py.")
    parser.add_argument("--cycles", type=int, default=2, help="Review cycles. Default: 2.")
    parser.add_argument("--timeout", type=int, default=1200, help="Per-model timeout seconds. Default: 1200.")
    parser.add_argument("--max-papers", type=int, help="Optional maximum papers from manifest.")
    parser.add_argument("--sleep", type=float, default=0.0, help="Sleep between papers. Default: 0.")
    parser.add_argument("--execute", action="store_true", help="Actually run model CLIs.")
    parser.add_argument("--board", action="store_true", help="Run summarizer board pass.")
    parser.add_argument("--overwrite-board", action="store_true", help="Overwrite only board summaries.")
    parser.add_argument("--stop-on-error", action="store_true", help="Stop if a paper command exits non-zero.")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def load_manifest(path: Path, limit: int | None) -> list[dict[str, object]]:
    entries = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return entries[:limit] if limit is not None else entries


def command_for(entry: dict[str, object], args: argparse.Namespace) -> list[str]:
    command = [
        sys.executable,
        str(ROOT / "scripts" / "run_review_cycle.py"),
        "--source-manifest",
        args.source_manifest,
        "--papers-dir",
        args.papers_dir,
        "--paper-id",
        str(entry["arxiv_id"]),
        "--providers",
        args.providers,
        "--cycles",
        str(args.cycles),
        "--timeout",
        str(args.timeout),
        "--build-bundle",
    ]
    if args.execute:
        command.append("--execute")
    if args.board:
        command.append("--board")
    if args.overwrite_board:
        command.append("--overwrite-board")
    return command


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    entries = load_manifest(Path(args.manifest), args.max_papers)
    log_dir = Path(args.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    batch_records = []
    for index, entry in enumerate(entries, start=1):
        arxiv_id = str(entry["arxiv_id"])
        paper_log_dir = log_dir / arxiv_id
        paper_log_dir.mkdir(parents=True, exist_ok=True)
        command = command_for(entry, args)
        record = {
            "arxiv_id": arxiv_id,
            "index": index,
            "total": len(entries),
            "command": command,
            "started_at": utc_now(),
        }
        write_json(paper_log_dir / "command.json", record)
        print(json.dumps({"event": "paper_started", "index": index, "total": len(entries), "arxiv_id": arxiv_id}))

        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        (paper_log_dir / "stdout.txt").write_text(completed.stdout, encoding="utf-8")
        (paper_log_dir / "stderr.txt").write_text(completed.stderr, encoding="utf-8")
        record.update(
            {
                "finished_at": utc_now(),
                "returncode": completed.returncode,
                "status": "ok" if completed.returncode == 0 else "error",
            }
        )
        write_json(paper_log_dir / "result.json", record)
        batch_records.append(record)
        print(
            json.dumps(
                {
                    "event": "paper_finished",
                    "index": index,
                    "total": len(entries),
                    "arxiv_id": arxiv_id,
                    "status": record["status"],
                    "returncode": completed.returncode,
                },
            )
        )
        write_json(
            log_dir / "batch_status.json",
            {
                "manifest": args.manifest,
                "source_manifest": args.source_manifest,
                "papers_dir": args.papers_dir,
                "providers": args.providers,
                "cycles": args.cycles,
                "execute": args.execute,
                "board": args.board,
                "updated_at": utc_now(),
                "records": batch_records,
            },
        )
        if completed.returncode != 0 and args.stop_on_error:
            return completed.returncode
        if args.sleep and index < len(entries):
            time.sleep(args.sleep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
