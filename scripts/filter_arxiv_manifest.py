#!/usr/bin/env python3
"""Filter an arXiv JSONL manifest into a repeatable review tranche."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input arXiv JSONL manifest.")
    parser.add_argument("--output", required=True, help="Filtered JSONL manifest.")
    parser.add_argument("--summary-output", help="Optional Markdown summary path.")
    parser.add_argument("--primary-category", help="Keep entries whose primary category matches this leaf.")
    parser.add_argument("--require-html", action="store_true", help="Keep only entries with arXiv HTML.")
    parser.add_argument("--max-pages", type=int, help="Keep only entries with page_count <= this value.")
    parser.add_argument("--limit", type=int, help="Optional limit after sorting.")
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def primary_category(entry: dict[str, object]) -> str | None:
    primary = str(entry.get("primary_subject") or "")
    match = re.search(r"\(([^)]+)\)", primary)
    return match.group(1) if match else None


def keep_entry(entry: dict[str, object], args: argparse.Namespace) -> bool:
    if args.primary_category and primary_category(entry) != args.primary_category:
        return False
    if args.require_html and not entry.get("has_html"):
        return False
    if args.max_pages is not None:
        page_count = entry.get("page_count")
        if not isinstance(page_count, int) or page_count > args.max_pages:
            return False
    return True


def sort_entries(entries: list[dict[str, object]]) -> list[dict[str, object]]:
    return sorted(
        entries,
        key=lambda entry: (
            entry.get("page_count") is None,
            entry.get("page_count") if isinstance(entry.get("page_count"), int) else 10**9,
            entry.get("listing_index") if isinstance(entry.get("listing_index"), int) else 10**9,
            str(entry.get("arxiv_id")),
        ),
    )


def render_summary(entries: list[dict[str, object]], args: argparse.Namespace) -> str:
    lines = [
        "# Filtered arXiv Review Tranche",
        "",
        f"- Source: `{args.input}`",
        f"- Entries: {len(entries)}",
        f"- Primary category: `{args.primary_category}`" if args.primary_category else "- Primary category: any",
        f"- Require HTML: `{args.require_html}`",
        f"- Max pages: `{args.max_pages}`" if args.max_pages is not None else "- Max pages: none",
        "",
        "| Rank | arXiv ID | Pages | Title | Comments |",
        "|---:|---|---:|---|---|",
    ]
    for rank, entry in enumerate(entries, start=1):
        arxiv_id = str(entry.get("arxiv_id"))
        pages = str(entry.get("page_count")) if entry.get("page_count") is not None else "?"
        title = str(entry.get("title") or "").replace("|", "\\|")
        comments = str(entry.get("comments") or "").replace("|", "\\|")
        abs_url = str(entry.get("abs_url") or f"https://arxiv.org/abs/{arxiv_id}")
        lines.append(f"| {rank} | [{arxiv_id}]({abs_url}) | {pages} | {title} | {comments} |")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    entries = sort_entries([entry for entry in load_jsonl(Path(args.input)) if keep_entry(entry, args)])
    if args.limit is not None:
        entries = entries[: args.limit]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "\n".join(json.dumps(entry, sort_keys=True) for entry in entries) + "\n",
        encoding="utf-8",
    )
    summary = render_summary(entries, args)
    print(summary)
    if args.summary_output:
        summary_path = Path(args.summary_output)
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(summary + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
