#!/usr/bin/env python3
"""Analyze alignment between LLM review scores and Sabine bullshit-meter scores."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import mean
from typing import Iterable


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--teasers",
        action="append",
        required=True,
        help="Path to a summarize_review_results.py teaser JSON file. May be repeated.",
    )
    parser.add_argument("--json-output", help="Optional JSON output path.")
    parser.add_argument("--markdown-output", help="Optional Markdown output path.")
    return parser.parse_args()


def load_rows(paths: Iterable[Path]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for row in data.get("papers", []):
            if not isinstance(row, dict):
                continue
            rows.append({"source_teasers": str(path), **row})
    return rows


def numeric(value: object) -> float | None:
    return float(value) if isinstance(value, (int, float)) else None


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2:
        return None
    x_mean = mean(xs)
    y_mean = mean(ys)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys, strict=True))
    x_den = math.sqrt(sum((x - x_mean) ** 2 for x in xs))
    y_den = math.sqrt(sum((y - y_mean) ** 2 for y in ys))
    if x_den == 0 or y_den == 0:
        return None
    return numerator / (x_den * y_den)


def ranks(values: list[float]) -> list[float]:
    indexed = sorted(enumerate(values), key=lambda pair: pair[1])
    result = [0.0] * len(values)
    i = 0
    while i < len(indexed):
        j = i + 1
        while j < len(indexed) and indexed[j][1] == indexed[i][1]:
            j += 1
        rank = (i + 1 + j) / 2
        for original_index, _ in indexed[i:j]:
            result[original_index] = rank
        i = j
    return result


def distribution(values: list[float]) -> dict[str, int]:
    bins = {"0-2": 0, "2-4": 0, "4-6": 0, "6-8": 0, "8-10": 0}
    for value in values:
        if value < 2:
            bins["0-2"] += 1
        elif value < 4:
            bins["2-4"] += 1
        elif value < 6:
            bins["4-6"] += 1
        elif value < 8:
            bins["6-8"] += 1
        else:
            bins["8-10"] += 1
    return bins


def build_analysis(rows: list[dict[str, object]]) -> dict[str, object]:
    pairs = []
    for row in rows:
        llm_score = numeric(row.get("selected_score"))
        sabine_score = numeric(row.get("sabine_bullshit_meter_score_10"))
        if llm_score is None or sabine_score is None:
            continue
        pairs.append(
            {
                "arxiv_id": row.get("arxiv_id"),
                "title": row.get("title"),
                "llm_selected_score_10": llm_score,
                "sabine_bullshit_meter_score_10": sabine_score,
                "abs_url": row.get("abs_url"),
                "source_teasers": row.get("source_teasers"),
            }
        )

    xs = [float(row["llm_selected_score_10"]) for row in pairs]
    ys = [float(row["sabine_bullshit_meter_score_10"]) for row in pairs]
    return {
        "paper_rows": len(rows),
        "numeric_pair_count": len(pairs),
        "llm_selected_score_distribution": distribution(xs),
        "sabine_bullshit_meter_distribution": distribution(ys),
        "llm_selected_score_mean": round(mean(xs), 3) if xs else None,
        "sabine_bullshit_meter_mean": round(mean(ys), 3) if ys else None,
        "pearson_llm_quality_vs_sabine_bullshit": round(pearson(xs, ys), 3) if pearson(xs, ys) is not None else None,
        "spearman_llm_quality_vs_sabine_bullshit": (
            round(pearson(ranks(xs), ranks(ys)), 3) if len(pairs) >= 2 else None
        ),
        "alignment_note": (
            "The two scales point in opposite directions: higher LLM score means stronger paper; "
            "higher Sabine score means more bullshit. A negative correlation is the expected alignment direction."
        ),
        "pairs": pairs,
    }


def render_markdown(analysis: dict[str, object]) -> str:
    lines = [
        "# Sabine Alignment Analysis",
        "",
        f"Numeric pairs: {analysis['numeric_pair_count']} / {analysis['paper_rows']}",
        f"Pearson quality-vs-bullshit: {analysis['pearson_llm_quality_vs_sabine_bullshit']}",
        f"Spearman quality-vs-bullshit: {analysis['spearman_llm_quality_vs_sabine_bullshit']}",
        "",
        "Higher LLM score means stronger paper; higher Sabine score means more bullshit, so negative correlation is better alignment.",
        "",
        "| LLM | Sabine | ID | Title |",
        "|---:|---:|---|---|",
    ]
    pairs = sorted(
        analysis.get("pairs", []),
        key=lambda row: (row["sabine_bullshit_meter_score_10"], row["llm_selected_score_10"]),
        reverse=True,
    )
    for row in pairs:
        title = str(row.get("title") or "").replace("|", "\\|")
        arxiv_id = str(row.get("arxiv_id") or "")
        url = str(row.get("abs_url") or "")
        label = f"[{arxiv_id}]({url})" if url else arxiv_id
        lines.append(
            f"| {row['llm_selected_score_10']:.3g} | {row['sabine_bullshit_meter_score_10']:.3g} | {label} | {title} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    rows = load_rows(Path(path) for path in args.teasers)
    analysis = build_analysis(rows)
    if args.json_output:
        output = Path(args.json_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    markdown = render_markdown(analysis)
    if args.markdown_output:
        output = Path(args.markdown_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
