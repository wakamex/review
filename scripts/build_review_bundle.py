#!/usr/bin/env python3
"""Build a compact review bundle from a source manifest entry."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-manifest", required=True, help="JSONL source manifest.")
    parser.add_argument("--paper-id", required=True, help="arXiv paper id.")
    parser.add_argument(
        "--papers-dir",
        required=True,
        help="Output directory containing per-paper review bundles.",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=140_000,
        help="Maximum source text characters in bundle. Default: 140000.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing bundle.")
    return parser.parse_args()


def load_source_record(path: Path, paper_id: str) -> dict[str, object]:
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get("arxiv_id") == paper_id:
            return record
    raise SystemExit(f"paper id {paper_id!r} not found in {path}")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_html_source(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript|svg|math)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)</?(h[1-6]|p|div|section|article|li|dt|dd|tr|br|blockquote)[^>]*>", "\n", raw)
    raw = re.sub(r"(?i)</?(td|th)[^>]*>", " | ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    text = html.unescape(raw)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return "\n".join(line.strip() for line in text.splitlines()).strip()


def clean_markdown_source(raw: str) -> str:
    raw = raw.replace("\r\n", "\n")
    raw = re.sub(r"\n{4,}", "\n\n\n", raw)
    return raw.strip()


def source_text(record: dict[str, object]) -> tuple[str, str]:
    source_path = Path(str(record["source_path"]))
    raw = source_path.read_text(encoding="utf-8", errors="replace")
    if record.get("source_type") == "arxiv_html":
        return clean_html_source(raw), sha256_text(raw)
    return clean_markdown_source(raw), sha256_text(raw)


def render_bundle(record: dict[str, object], text: str, raw_hash: str, max_chars: int) -> tuple[str, dict[str, object]]:
    truncated = len(text) > max_chars
    bundle_text = text[:max_chars].rstrip() if truncated else text
    metadata = {
        "arxiv_id": record["arxiv_id"],
        "title": record.get("title"),
        "topic": record.get("topic"),
        "month": record.get("month"),
        "abs_url": record.get("abs_url"),
        "pdf_url": record.get("pdf_url"),
        "source_type": record.get("source_type"),
        "source_path": record.get("source_path"),
        "source_url": record.get("source_url"),
        "subjects": record.get("subjects", []),
        "categories": record.get("categories", []),
        "comments": record.get("comments"),
        "page_count": record.get("page_count"),
        "raw_source_sha256": raw_hash,
        "source_text_chars": len(text),
        "bundle_text_chars": len(bundle_text),
        "truncated": truncated,
        "bundle_sha256": sha256_text(bundle_text),
    }

    header = [
        f"# Review Bundle: {record['arxiv_id']}",
        "",
        "## Metadata",
        "",
        "```json",
        json.dumps(metadata, indent=2, sort_keys=True),
        "```",
        "",
        "## Source Text",
        "",
    ]
    if truncated:
        header.extend(
            [
                f"[TRUNCATED: included first {max_chars} of {len(text)} cleaned characters.]",
                "",
            ]
        )
    return "\n".join(header) + bundle_text + "\n", metadata


def main() -> int:
    args = parse_args()
    record = load_source_record(Path(args.source_manifest), args.paper_id)
    paper_dir = Path(args.papers_dir) / args.paper_id
    bundle_path = paper_dir / "bundle.md"
    metadata_path = paper_dir / "metadata.json"
    if bundle_path.exists() and not args.overwrite:
        print(bundle_path)
        return 0

    text, raw_hash = source_text(record)
    bundle, metadata = render_bundle(record, text, raw_hash, args.max_chars)
    paper_dir.mkdir(parents=True, exist_ok=True)
    bundle_path.write_text(bundle, encoding="utf-8")
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(bundle_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
