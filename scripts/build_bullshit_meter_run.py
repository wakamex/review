#!/usr/bin/env python3
"""Build review manifests for Sabine Hossenfelder bullshit-meter sources.

The source dataset has one transcript per video plus a TSV of source documents.
This adapter turns each TSV row into one review target while keeping Sabine's
rating as sidecar metadata, not reviewer-visible bundle metadata.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
from pathlib import Path


DEFAULT_SOURCE_DIR = Path("/code/scripts/bullshit-meter")

SCORE_WORDS = {
    "zero": 0.0,
    "one": 1.0,
    "two": 2.0,
    "three": 3.0,
    "four": 4.0,
    "five": 5.0,
    "six": 6.0,
    "seven": 7.0,
    "eight": 8.0,
    "nine": 9.0,
    "ten": 10.0,
}

SCORE_OVERRIDES: dict[str, dict[str, object]] = {
    "bm-097-01": {
        "score": None,
        "status": "qualitative_no_numeric",
        "scope": "paper",
        "note": "Transcript says 'a low reading' but does not give a numeric score.",
    },
    "bm-119-01": {
        "score": None,
        "status": "ambiguous",
        "scope": "paper",
        "candidate_scores": [0.0, 10.0],
        "note": "Transcript says the score is either 0 or 10, and Sabine does not know which.",
    },
    "bm-123-01": {
        "score": 1.0,
        "status": "resolved",
        "scope": "paper",
        "note": "Transcript distinguishes interpretation=10 from paper=1.",
    },
    "bm-153-01": {
        "score": 1.0,
        "status": "resolved",
        "scope": "paper",
        "note": "Transcript distinguishes paper=1 from press release=10.",
    },
    "bm-153-02": {
        "score": 10.0,
        "status": "resolved",
        "scope": "press_release",
        "note": "Transcript distinguishes paper=1 from press release=10.",
    },
    "bm-185-01": {
        "score": 7.0,
        "status": "resolved",
        "scope": "paper",
        "note": "Transcript says the new dark-star candidate paper gets a bullshit rating of 7.",
    },
    "bm-185-02": {
        "score": None,
        "status": "not_scored_separately",
        "scope": "related_paper",
        "related_video_score": 7.0,
        "note": "Transcript's 7 score applies to the new spectroscopic candidate paper, not this earlier context paper.",
    },
    "bm-185-03": {
        "score": None,
        "status": "not_scored_separately",
        "scope": "foundational_paper",
        "related_video_score": 7.0,
        "note": "Transcript's 7 score applies to the new spectroscopic candidate paper, not this foundational context paper.",
    },
    "bm-195-02": {
        "score": None,
        "status": "not_scored_separately",
        "scope": "press_release",
        "related_video_score": 9.0,
        "note": "Transcript gives the linked paper a 9; it does not separately score the UBC release.",
    },
    "bm-212-02": {
        "score": None,
        "status": "not_scored_separately",
        "scope": "related_paper",
        "related_video_score": 0.0,
        "note": "Transcript gives the thesis a 0; it does not separately score this related paper.",
    },
    "bm-212-03": {
        "score": None,
        "status": "not_scored_separately",
        "scope": "related_paper",
        "related_video_score": 0.0,
        "note": "Transcript gives the thesis a 0; it does not separately score this related paper.",
    },
    "bm-218-01": {
        "score": 0.0,
        "status": "resolved",
        "scope": "paper",
        "note": "Transcript gives the paper 'zero out of 10' on the bullshit meter.",
    },
    "bm-221-01": {
        "score": 5.0,
        "status": "resolved_topic_score",
        "scope": "source_article",
        "note": "No specific paper was named; transcript scores photonic computing as a topic at 5.",
    },
    "bm-221-02": {
        "score": 5.0,
        "status": "resolved_topic_score",
        "scope": "background_review",
        "note": "No specific paper was named; transcript scores photonic computing as a topic at 5.",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", default=str(DEFAULT_SOURCE_DIR), help="bullshit-meter directory.")
    parser.add_argument("--output-dir", required=True, help="Fresh output run directory.")
    parser.add_argument(
        "--pdf-method",
        default="pymupdf4llm",
        choices=("pymupdf4llm", "pymupdf-text"),
        help="Local PDF extraction method. Default: pymupdf4llm.",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_new(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        handle.write(text)


def copy_new(source: Path, target: Path) -> None:
    if target.exists():
        raise FileExistsError(f"refusing to overwrite {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def transcript_info(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace")
    stem = path.stem
    parts = stem.split("__")
    video_index = parts[0] if parts else stem
    video_id = parts[-1] if len(parts) > 1 else None
    slug = parts[1] if len(parts) > 2 else stem
    title = slug.replace("-", " ").strip().title()
    return {
        "path": str(path),
        "stem": stem,
        "video_index": video_index,
        "video_id": video_id,
        "video_title": title,
        "youtube_url": f"https://www.youtube.com/watch?v={video_id}" if video_id else None,
        "text": text,
        "ratings": extract_ratings(text),
    }


def extract_ratings(text: str) -> list[dict[str, object]]:
    normalized = re.sub(r"\s+", " ", text)
    ratings: list[dict[str, object]] = []
    seen: set[tuple[float, int]] = set()
    score_atom = r"(?P<score>\d+(?:\.\d+)?|zero|one|two|three|four|five|six|seven|eight|nine|ten)"
    patterns = [
        re.compile(score_atom + r"\s*(?:/|out of)\s*10.{0,120}?bullshit meter", re.I),
        re.compile(score_atom + r"\s*(?:/|out of)\s*10.{0,120}?\bmeter\b", re.I),
        re.compile(r"bullshit meter.{0,120}?" + score_atom + r"\s*(?:/|out of)\s*10", re.I),
        re.compile(r"bullshit rating of\s+" + score_atom + r"\b", re.I),
    ]
    for pattern in patterns:
        for match in pattern.finditer(normalized):
            raw_score = match.group("score").lower()
            score = SCORE_WORDS.get(raw_score, float(raw_score) if re.match(r"\d", raw_score) else None)
            if score is None:
                continue
            window_start = max(0, match.start() - 180)
            window_end = min(len(normalized), match.end() + 180)
            window = normalized[window_start:window_end]
            key = (score, match.start())
            if key in seen:
                continue
            seen.add(key)
            ratings.append({"score_10": score, "excerpt": window.strip()})
    return ratings


def resolved_bullshit_score(paper_id: str, ratings: list[dict[str, object]]) -> dict[str, object]:
    override = SCORE_OVERRIDES.get(paper_id)
    if override is not None:
        score = override.get("score")
        result = {
            "sabine_bullshit_meter_score_10": score,
            "sabine_bullshit_meter_score_status": override.get("status"),
            "sabine_bullshit_meter_score_scope": override.get("scope"),
            "sabine_bullshit_meter_score_note": override.get("note"),
        }
        if "candidate_scores" in override:
            result["sabine_bullshit_meter_candidate_scores_10"] = override["candidate_scores"]
        if "related_video_score" in override:
            result["sabine_related_video_bullshit_meter_score_10"] = override["related_video_score"]
        return result

    scores = [rating.get("score_10") for rating in ratings if isinstance(rating.get("score_10"), (int, float))]
    if len(scores) == 1:
        return {
            "sabine_bullshit_meter_score_10": float(scores[0]),
            "sabine_bullshit_meter_score_status": "resolved",
            "sabine_bullshit_meter_score_scope": "paper",
            "sabine_bullshit_meter_score_note": None,
        }
    if not scores:
        return {
            "sabine_bullshit_meter_score_10": None,
            "sabine_bullshit_meter_score_status": "missing",
            "sabine_bullshit_meter_score_scope": None,
            "sabine_bullshit_meter_score_note": "No numeric bullshit-meter score was found in the transcript.",
        }
    return {
        "sabine_bullshit_meter_score_10": None,
        "sabine_bullshit_meter_score_status": "ambiguous_multiple_scores",
        "sabine_bullshit_meter_score_scope": None,
        "sabine_bullshit_meter_candidate_scores_10": scores,
        "sabine_bullshit_meter_score_note": "Multiple score mentions were found but no target-specific rule resolved them.",
    }


def clean_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def extract_html_title(path: Path) -> str | None:
    raw = path.read_text(encoding="utf-8", errors="replace")
    patterns = [
        r"(?is)<meta[^>]+property=[\"']og:title[\"'][^>]+content=[\"']([^\"']+)",
        r"(?is)<span[^>]+class=[\"'][^\"']*ltx_font_bold[^\"']*[\"'][^>]*style=[\"'][^\"']*font-size:144%[^\"']*[\"'][^>]*>(.*?)</span>",
        r"(?is)<h1[^>]*>(.*?)</h1>",
        r"(?is)<title[^>]*>(.*?)</title>",
    ]
    for pattern in patterns:
        match = re.search(pattern, raw)
        if match:
            title = clean_text(match.group(1))
            if title:
                return title
    return None


def extract_pdf_text(pdf_path: Path, method: str) -> str:
    if method == "pymupdf4llm":
        import pymupdf4llm

        return pymupdf4llm.to_markdown(str(pdf_path))
    if method == "pymupdf-text":
        import fitz

        doc = fitz.open(pdf_path)
        return "\n\n".join(page.get_text("text") for page in doc)
    raise ValueError(f"unknown PDF method: {method}")


def target_id(row: dict[str, str]) -> str:
    transcript_index = row["transcript"].split("__", 1)[0]
    return f"bm-{transcript_index}-{int(row['index']):02d}"


def build_records(source_dir: Path, output_dir: Path, pdf_method: str) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    rows = [row for row in read_tsv(source_dir / "source-papers" / "manifest.tsv") if row.get("status") == "ok"]
    transcripts = {
        path.name: transcript_info(path)
        for path in sorted(source_dir.glob("*.txt"))
    }
    manifest: list[dict[str, object]] = []
    source_manifest: list[dict[str, object]] = []
    sabine_context: list[dict[str, object]] = []

    for row in rows:
        paper_id = target_id(row)
        source_path = Path(row["saved_path"])
        if not source_path.exists():
            raise FileNotFoundError(source_path)

        asset_dir = output_dir / "assets" / paper_id
        transcript = transcripts.get(row["transcript"])
        if transcript is None:
            raise FileNotFoundError(f"missing transcript {row['transcript']}")
        score_fields = resolved_bullshit_score(paper_id, transcript["ratings"])

        is_pdf = source_path.suffix.lower() == ".pdf" or "pdf" in row.get("content_type", "").lower()
        copied_source = asset_dir / ("paper.pdf" if is_pdf else "paper.html")
        copy_new(source_path, copied_source)

        if is_pdf:
            extracted_path = asset_dir / "extracted" / f"{pdf_method}.md"
            text = extract_pdf_text(copied_source, pdf_method)
            write_new(extracted_path, text)
            review_source_path = extracted_path
            source_type = f"pdf_{pdf_method}"
            title = row["label"]
        else:
            review_source_path = copied_source
            source_type = "arxiv_html"
            title = extract_html_title(copied_source) or row["label"]

        comments = f"Sabine video: {transcript['video_title']}; source label: {row['label']}; source note: {row['note']}"
        common = {
            "arxiv_id": paper_id,
            "title": title,
            "topic": "bullshit-meter",
            "month": "sabine",
            "abs_url": row["original_url"],
            "pdf_url": row["fetched_url"] if is_pdf else None,
            "html_url": row["fetched_url"] if not is_pdf else None,
            "source_label": row["label"],
            "comments": comments,
            "page_count": None,
            "categories": ["bullshit-meter"],
            "subjects": ["Sabine Hossenfelder bullshit-meter source"],
        }
        manifest.append(
            {
                **common,
                "transcript": row["transcript"],
                "transcript_video_title": transcript["video_title"],
                "youtube_url": transcript["youtube_url"],
                "source_index": int(row["index"]),
                "original_url": row["original_url"],
                "fetched_url": row["fetched_url"],
                "saved_path": str(copied_source),
                "source_content_type": row["content_type"],
                "source_note": row["note"],
                "sabine_bullshit_ratings": transcript["ratings"],
                **score_fields,
            }
        )
        source_manifest.append(
            {
                **common,
                "source_path": str(review_source_path),
                "source_type": source_type,
                "source_url": row["fetched_url"],
                "fallback_pdf_path": str(copied_source) if is_pdf else None,
                "status": "ready",
            }
        )
        sabine_context.append(
            {
                "arxiv_id": paper_id,
                "transcript": row["transcript"],
                "transcript_path": transcript["path"],
                "video_title": transcript["video_title"],
                "youtube_url": transcript["youtube_url"],
                "source_label": row["label"],
                "original_url": row["original_url"],
                "fetched_url": row["fetched_url"],
                "sabine_bullshit_ratings": transcript["ratings"],
                **score_fields,
            }
        )

    return manifest, source_manifest, sabine_context


def render_summary(manifest: list[dict[str, object]]) -> str:
    lines = [
        "# Bullshit-Meter Review Targets",
        "",
        "| Rank | ID | Source | Video | Sabine Rating(s) | URL |",
        "|---:|---|---|---|---|---|",
    ]
    for index, row in enumerate(manifest, start=1):
        score = row.get("sabine_bullshit_meter_score_10")
        rating_text = str(score) if isinstance(score, (int, float)) else str(row.get("sabine_bullshit_meter_score_status") or "")
        lines.append(
            "| "
            + " | ".join(
                [
                    str(index),
                    str(row["arxiv_id"]),
                    str(row["source_label"]).replace("|", "\\|"),
                    str(row["transcript_video_title"]).replace("|", "\\|"),
                    rating_text,
                    str(row["original_url"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    source_dir = Path(args.source_dir)
    output_dir = Path(args.output_dir)
    if output_dir.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {output_dir}")
    output_dir.mkdir(parents=True)

    manifest, source_manifest, sabine_context = build_records(source_dir, output_dir, args.pdf_method)
    write_new(output_dir / "manifest.jsonl", "\n".join(json.dumps(row, sort_keys=True) for row in manifest) + "\n")
    write_new(
        output_dir / "source_manifest.jsonl",
        "\n".join(json.dumps(row, sort_keys=True) for row in source_manifest) + "\n",
    )
    write_new(
        output_dir / "sabine_context.jsonl",
        "\n".join(json.dumps(row, sort_keys=True) for row in sabine_context) + "\n",
    )
    write_new(output_dir / "manifest_summary.md", render_summary(manifest))
    print(json.dumps({"output_dir": str(output_dir), "targets": len(manifest)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
