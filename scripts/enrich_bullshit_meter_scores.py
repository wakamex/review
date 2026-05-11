#!/usr/bin/env python3
"""Add resolved Sabine bullshit-meter scores to a completed run's JSON files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_bullshit_meter_run import (
    DEFAULT_SOURCE_DIR,
    read_tsv,
    resolved_bullshit_score,
    target_id,
    transcript_info,
)


SCORE_KEYS = (
    "sabine_bullshit_meter_score_10",
    "sabine_bullshit_meter_score_status",
    "sabine_bullshit_meter_score_scope",
    "sabine_bullshit_meter_score_note",
    "sabine_bullshit_meter_candidate_scores_10",
    "sabine_related_video_bullshit_meter_score_10",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, help="Run directory containing manifest.jsonl.")
    parser.add_argument("--source-dir", default=str(DEFAULT_SOURCE_DIR), help="bullshit-meter source directory.")
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text("\n".join(json.dumps(row, sort_keys=True) for row in rows) + "\n", encoding="utf-8")


def score_fields_by_id(source_dir: Path) -> dict[str, dict[str, object]]:
    transcripts = {path.name: transcript_info(path) for path in sorted(source_dir.glob("*.txt"))}
    fields: dict[str, dict[str, object]] = {}
    for row in read_tsv(source_dir / "source-papers" / "manifest.tsv"):
        if row.get("status") != "ok":
            continue
        paper_id = target_id(row)
        transcript = transcripts[row["transcript"]]
        fields[paper_id] = {
            "sabine_bullshit_ratings": transcript["ratings"],
            **resolved_bullshit_score(paper_id, transcript["ratings"]),
        }
    return fields


def apply_fields(row: dict[str, object], fields: dict[str, object]) -> dict[str, object]:
    updated = dict(row)
    for key in ("sabine_bullshit_ratings", *SCORE_KEYS):
        updated.pop(key, None)
    updated.update(fields)
    return updated


def enrich_manifest(run_dir: Path, fields_by_id: dict[str, dict[str, object]]) -> int:
    manifest_path = run_dir / "manifest.jsonl"
    rows = load_jsonl(manifest_path)
    enriched = []
    for row in rows:
        paper_id = str(row["arxiv_id"])
        enriched.append(apply_fields(row, fields_by_id.get(paper_id, {})))
    write_jsonl(manifest_path, enriched)
    return len(enriched)


def enrich_sabine_context(run_dir: Path, fields_by_id: dict[str, dict[str, object]]) -> int:
    context_path = run_dir / "sabine_context.jsonl"
    if not context_path.exists():
        return 0
    rows = load_jsonl(context_path)
    enriched = []
    for row in rows:
        paper_id = str(row["arxiv_id"])
        enriched.append(apply_fields(row, fields_by_id.get(paper_id, {})))
    write_jsonl(context_path, enriched)
    return len(enriched)


def enrich_teasers(run_dir: Path, fields_by_id: dict[str, dict[str, object]]) -> int:
    teaser_path = run_dir / "teasers.json"
    if not teaser_path.exists():
        return 0
    data = json.loads(teaser_path.read_text(encoding="utf-8"))
    papers = data.get("papers") if isinstance(data.get("papers"), list) else []
    for paper in papers:
        if not isinstance(paper, dict):
            continue
        paper_id = str(paper.get("arxiv_id"))
        fields = fields_by_id.get(paper_id, {})
        for key in SCORE_KEYS:
            if key in paper:
                paper.pop(key)
            if key in fields:
                paper[key] = fields[key]
    teaser_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return len(papers)


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir)
    fields = score_fields_by_id(Path(args.source_dir))
    summary = {
        "run_dir": str(run_dir),
        "resolved_fields": len(fields),
        "manifest_rows": enrich_manifest(run_dir, fields),
        "sabine_context_rows": enrich_sabine_context(run_dir, fields),
        "teaser_rows": enrich_teasers(run_dir, fields),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
