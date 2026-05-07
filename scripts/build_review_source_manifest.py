#!/usr/bin/env python3
"""Build a per-paper source manifest for review bundle generation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, help="Original arXiv JSONL manifest.")
    parser.add_argument("--assets-dir", required=True, help="Directory containing assets.")
    parser.add_argument("--output", required=True, help="Output JSONL path.")
    parser.add_argument(
        "--pdf-method",
        default="pymupdf4llm",
        help="PDF extraction method to use for PDF fallback paths.",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def source_for(entry: dict[str, object], assets_dir: Path, pdf_method: str) -> dict[str, object]:
    arxiv_id = str(entry["arxiv_id"])
    paper_dir = assets_dir / arxiv_id
    html_path = paper_dir / "paper.html"
    pdf_extract_path = paper_dir / "extracted" / f"{pdf_method}.md"
    pdf_path = paper_dir / "paper.pdf"

    if html_path.exists():
        return {
            "arxiv_id": arxiv_id,
            "source_type": "arxiv_html",
            "source_path": str(html_path),
            "source_url": entry.get("html_url"),
            "fallback_pdf_path": str(pdf_path) if pdf_path.exists() else None,
            "status": "ready",
        }
    if pdf_extract_path.exists():
        return {
            "arxiv_id": arxiv_id,
            "source_type": f"pdf_{pdf_method}",
            "source_path": str(pdf_extract_path),
            "source_url": entry.get("pdf_url"),
            "fallback_pdf_path": str(pdf_path) if pdf_path.exists() else None,
            "status": "ready",
        }
    return {
        "arxiv_id": arxiv_id,
        "source_type": None,
        "source_path": None,
        "source_url": None,
        "fallback_pdf_path": str(pdf_path) if pdf_path.exists() else None,
        "status": "missing",
    }


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest)
    assets_dir = Path(args.assets_dir)
    output_path = Path(args.output)
    entries = load_jsonl(manifest_path)
    records = []
    for entry in entries:
        record = dict(entry)
        record.update(source_for(entry, assets_dir, args.pdf_method))
        records.append(record)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n",
        encoding="utf-8",
    )

    ready = sum(1 for record in records if record["status"] == "ready")
    by_type: dict[str, int] = {}
    for record in records:
        by_type[str(record["source_type"])] = by_type.get(str(record["source_type"]), 0) + 1
    print(json.dumps({"total": len(records), "ready": ready, "by_type": by_type}, indent=2, sort_keys=True))
    return 1 if ready != len(records) else 0


if __name__ == "__main__":
    raise SystemExit(main())
