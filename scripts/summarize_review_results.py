#!/usr/bin/env python3
"""Summarize completed review outputs into a teaser-ready report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, help="Filtered arXiv manifest for paper order.")
    parser.add_argument("--papers-dir", required=True, help="Per-paper review output directory.")
    parser.add_argument("--json-output", help="Optional JSON output path.")
    parser.add_argument("--markdown-output", help="Optional Markdown output path.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def load_manifest(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def paper_summary(entry: dict[str, object], papers_dir: Path) -> dict[str, object]:
    arxiv_id = str(entry["arxiv_id"])
    paper_dir = papers_dir / arxiv_id
    run_summary = load_json(paper_dir / "review_run_summary.json") or {}
    board = load_json(paper_dir / "board" / "claude.json") or {}
    score_summary = run_summary.get("score_summary") if isinstance(run_summary.get("score_summary"), dict) else {}
    selected_score = (
        score_summary.get("selected_final_score")
        if isinstance(score_summary.get("selected_final_score"), dict)
        else {}
    )
    calls = run_summary.get("calls") if isinstance(run_summary.get("calls"), list) else []
    return {
        "arxiv_id": arxiv_id,
        "title": entry.get("title"),
        "abs_url": entry.get("abs_url"),
        "page_count": entry.get("page_count"),
        "selected_score": selected_score.get("overall_score_10"),
        "score_source": selected_score.get("source"),
        "general_reader_takeaway": board.get("general_reader_takeaway"),
        "technical_takeaway": board.get("technical_takeaway"),
        "run_status": "complete" if run_summary else "missing",
        "call_status_counts": {
            status: sum(1 for call in calls if isinstance(call, dict) and call.get("status") == status)
            for status in sorted({str(call.get("status")) for call in calls if isinstance(call, dict)})
        },
    }


def render_markdown(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Review Teasers",
        "",
        "| Rank | Score | arXiv ID | Pages | Title | General-Reader Takeaway |",
        "|---:|---:|---|---:|---|---|",
    ]
    for rank, row in enumerate(rows, start=1):
        score = row.get("selected_score")
        score_text = f"{score:.3g}" if isinstance(score, (int, float)) else ""
        arxiv_id = str(row["arxiv_id"])
        abs_url = str(row.get("abs_url") or f"https://arxiv.org/abs/{arxiv_id}")
        pages = str(row.get("page_count") or "")
        title = str(row.get("title") or "").replace("|", "\\|")
        takeaway = str(row.get("general_reader_takeaway") or "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {rank} | {score_text} | [{arxiv_id}]({abs_url}) | {pages} | {title} | {takeaway} |")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    rows = [paper_summary(entry, Path(args.papers_dir)) for entry in load_manifest(Path(args.manifest))]
    if args.json_output:
        output_path = Path(args.json_output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps({"papers": rows}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    markdown = render_markdown(rows)
    print(markdown)
    if args.markdown_output:
        output_path = Path(args.markdown_output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
