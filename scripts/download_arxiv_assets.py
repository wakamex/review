#!/usr/bin/env python3
"""Download preferred arXiv paper assets from a JSONL manifest."""

from __future__ import annotations

import argparse
import json
import time
import urllib.request
from pathlib import Path


USER_AGENT = "arxiv-review-layer-download/0.1 (local research script)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, help="JSONL manifest path.")
    parser.add_argument("--out-dir", required=True, help="Directory for downloaded assets.")
    parser.add_argument(
        "--prefer",
        choices=("html", "pdf"),
        default="html",
        help="Preferred asset type. Default: html.",
    )
    parser.add_argument(
        "--fallback",
        choices=("none", "pdf"),
        default="none",
        help="Fallback when preferred HTML is unavailable. Default: none.",
    )
    parser.add_argument("--limit", type=int, help="Optional max number of papers to process.")
    parser.add_argument("--sleep", type=float, default=1.0, help="Sleep between downloads.")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without downloading.")
    return parser.parse_args()


def load_manifest(path: Path) -> list[dict[str, object]]:
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            entries.append(json.loads(line))
    return entries


def asset_for(entry: dict[str, object], prefer: str, fallback: str) -> tuple[str, str] | None:
    if prefer == "html" and entry.get("html_url"):
        return "html", str(entry["html_url"])
    if prefer == "pdf":
        return "pdf", str(entry["pdf_url"])
    if fallback == "pdf":
        return "pdf", str(entry["pdf_url"])
    return None


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest)
    out_dir = Path(args.out_dir)
    entries = load_manifest(manifest_path)
    if args.limit is not None:
        entries = entries[: args.limit]

    downloaded = 0
    skipped = 0
    manifest_records = []
    for index, entry in enumerate(entries):
        arxiv_id = str(entry["arxiv_id"])
        selected = asset_for(entry, args.prefer, args.fallback)
        if selected is None:
            skipped += 1
            manifest_records.append(
                {
                    "arxiv_id": arxiv_id,
                    "status": "skipped",
                    "reason": f"no {args.prefer} asset and fallback={args.fallback}",
                }
            )
            continue

        asset_type, url = selected
        paper_dir = out_dir / arxiv_id
        suffix = "html" if asset_type == "html" else "pdf"
        target = paper_dir / f"paper.{suffix}"
        record = {
            "arxiv_id": arxiv_id,
            "asset_type": asset_type,
            "url": url,
            "path": str(target),
            "status": "planned" if args.dry_run else "downloaded",
        }
        if args.dry_run:
            print(json.dumps(record, sort_keys=True))
            manifest_records.append(record)
            continue

        paper_dir.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            if index:
                time.sleep(args.sleep)
            target.write_bytes(fetch_bytes(url))
        else:
            record["status"] = "exists"
        (paper_dir / "asset.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        manifest_records.append(record)
        downloaded += 1
        print(json.dumps(record, sort_keys=True))

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "download_manifest.json").write_text(
        json.dumps(
            {
                "manifest": str(manifest_path),
                "prefer": args.prefer,
                "fallback": args.fallback,
                "downloaded_or_existing": downloaded,
                "skipped": skipped,
                "records": manifest_records,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
