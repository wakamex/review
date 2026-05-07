#!/usr/bin/env python3
"""Compare rough review workload for arXiv leaf categories.

This script uses arXiv monthly list pages, not PDFs. It extracts counts,
comments, reported page counts, HTML availability, and cross-list metadata as
cheap proxies for parsing/review workload.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import statistics
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ARXIV_LIST_BASE = "https://arxiv.org/list"
USER_AGENT = "arxiv-review-layer-workload/0.1 (local research script)"
PAGE_SIZE = 2000


@dataclass
class Article:
    arxiv_id: str
    title: str
    comments: str | None
    page_count: int | None
    has_html: bool
    subjects: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare rough parsing workload for arXiv categories."
    )
    parser.add_argument("--month", required=True, help="Month in YYYY-MM format.")
    parser.add_argument(
        "--topics",
        required=True,
        help="Comma-separated arXiv category leaves, e.g. math.SP,math.SG.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.5,
        help="Seconds to sleep between requests. Default: 0.5.",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON.")
    parser.add_argument("--output", help="Optional output path.")
    return parser.parse_args()


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def clean_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def extract_block(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return clean_html(match.group(1)) if match else None


def parse_page_count(comments: str | None) -> int | None:
    if not comments:
        return None
    patterns = [
        r"(\d+)\s*pages?\b",
        r"(\d+)\s*pp\b",
        r"(\d+)\s*p\.\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, comments, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def parse_articles(page_html: str) -> tuple[int | None, list[Article]]:
    total_match = re.search(r"Total of\s+([\d,]+)\s+entries", page_html)
    total = int(total_match.group(1).replace(",", "")) if total_match else None
    articles: list[Article] = []

    chunks = re.split(r"<dt>", page_html)[1:]
    for chunk in chunks:
        id_match = re.search(r'href\s*=\s*"/abs/([^"]+)"', chunk)
        if not id_match:
            continue
        arxiv_id = id_match.group(1)
        title = extract_block(r"<div class='list-title[^']*'.*?</span>(.*?)</div>", chunk)
        comments = extract_block(r"<div class='list-comments[^']*'.*?</span>(.*?)</div>", chunk)
        subjects_text = extract_block(
            r"<div class='list-subjects'.*?</span>(.*?)</div>", chunk
        )
        subjects = []
        if subjects_text:
            subjects = [part.strip() for part in subjects_text.split(";") if part.strip()]
        articles.append(
            Article(
                arxiv_id=arxiv_id,
                title=title or "",
                comments=comments,
                page_count=parse_page_count(comments),
                has_html=f'id="html-{arxiv_id}"' in chunk or f"/html/{arxiv_id}" in chunk,
                subjects=subjects,
            )
        )
    return total, articles


def percentile(values: list[int], pct: float) -> float | None:
    if not values:
        return None
    sorted_values = sorted(values)
    index = (len(sorted_values) - 1) * pct
    lower = int(index)
    upper = min(lower + 1, len(sorted_values) - 1)
    if lower == upper:
        return float(sorted_values[lower])
    weight = index - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


def fetch_articles(topic: str, month: str, sleep: float) -> tuple[int | None, list[Article], list[str]]:
    articles_by_id: dict[str, Article] = {}
    urls = []
    total: int | None = None
    skip = 0

    while True:
        url = f"{ARXIV_LIST_BASE}/{topic}/{month}?skip={skip}&show={PAGE_SIZE}"
        urls.append(url)
        page_total, page_articles = parse_articles(fetch_text(url))
        if total is None:
            total = page_total
        for article in page_articles:
            articles_by_id[article.arxiv_id] = article
        if total is None or len(articles_by_id) >= total or not page_articles:
            break
        skip += PAGE_SIZE
        time.sleep(sleep)

    return total, list(articles_by_id.values()), urls


def summarize(topic: str, month: str, sleep: float) -> dict[str, object]:
    total, articles, urls = fetch_articles(topic, month, sleep)
    page_counts = [article.page_count for article in articles if article.page_count is not None]
    crosslisted = sum(1 for article in articles if len(article.subjects) > 1)
    return {
        "topic": topic,
        "month": month,
        "urls": urls,
        "total": total,
        "parsed_articles": len(articles),
        "html_available": sum(1 for article in articles if article.has_html),
        "html_available_pct": round(
            100 * sum(1 for article in articles if article.has_html) / len(articles), 1
        )
        if articles
        else None,
        "crosslisted": crosslisted,
        "crosslisted_pct": round(100 * crosslisted / len(articles), 1) if articles else None,
        "page_counts_reported": len(page_counts),
        "page_counts_reported_pct": round(100 * len(page_counts) / len(articles), 1)
        if articles
        else None,
        "page_count_mean": round(statistics.mean(page_counts), 1) if page_counts else None,
        "page_count_median": round(statistics.median(page_counts), 1) if page_counts else None,
        "page_count_p90": round(percentile(page_counts, 0.9), 1) if page_counts else None,
        "page_count_max": max(page_counts) if page_counts else None,
    }


def render_markdown(rows: list[dict[str, object]]) -> str:
    lines = [
        "| Topic | Entries | HTML | Cross-Listed | Page Counts | Median Pages | P90 Pages | Max Pages |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| `{topic}` | {total} | {html_available} ({html_available_pct}%) | "
            "{crosslisted} ({crosslisted_pct}%) | "
            "{page_counts_reported} ({page_counts_reported_pct}%) | "
            "{page_count_median} | {page_count_p90} | {page_count_max} |".format(
                **row
            )
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    topics = [topic.strip() for topic in args.topics.split(",") if topic.strip()]
    rows = []
    for index, topic in enumerate(topics):
        if index:
            time.sleep(args.sleep)
        rows.append(summarize(topic, args.month, args.sleep))

    output = json.dumps({"results": rows}, indent=2, sort_keys=True) if args.json else render_markdown(rows)
    print(output)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
