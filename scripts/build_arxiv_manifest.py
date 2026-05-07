#!/usr/bin/env python3
"""Build a JSONL manifest for an arXiv monthly category list."""

from __future__ import annotations

import argparse
import html
import json
import re
import time
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path


ARXIV_BASE = "https://arxiv.org"
ARXIV_LIST_BASE = f"{ARXIV_BASE}/list"
PAGE_SIZE = 2000
USER_AGENT = "arxiv-review-layer-manifest/0.1 (local research script)"


@dataclass
class ManifestEntry:
    arxiv_id: str
    topic: str
    month: str
    listing_index: int
    title: str
    comments: str | None
    page_count: int | None
    has_html: bool
    html_url: str | None
    pdf_url: str
    abs_url: str
    subjects: list[str]
    primary_subject: str | None
    categories: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--month", required=True, help="Month in YYYY-MM format.")
    parser.add_argument("--topic", required=True, help="arXiv category, e.g. math.SG.")
    parser.add_argument("--output", required=True, help="JSONL output path.")
    parser.add_argument("--summary-output", help="Optional Markdown summary path.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Sleep between pages.")
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


def parse_categories(subjects: list[str]) -> list[str]:
    categories = []
    for subject in subjects:
        for category in re.findall(r"\(([a-z]+(?:-[a-z]+)?(?:\.[A-Z]+)?)\)", subject):
            if category not in categories:
                categories.append(category)
    return categories


def parse_articles(page_html: str, topic: str, month: str, offset: int) -> tuple[int | None, list[ManifestEntry]]:
    total_match = re.search(r"Total of\s+([\d,]+)\s+entries", page_html)
    total = int(total_match.group(1).replace(",", "")) if total_match else None
    entries = []

    chunks = re.split(r"<dt>", page_html)[1:]
    for chunk_index, chunk in enumerate(chunks, start=1):
        id_match = re.search(r'href\s*=\s*"/abs/([^"]+)"', chunk)
        if not id_match:
            continue
        arxiv_id = id_match.group(1)
        title = extract_block(r"<div class='list-title[^']*'.*?</span>(.*?)</div>", chunk) or ""
        comments = extract_block(r"<div class='list-comments[^']*'.*?</span>(.*?)</div>", chunk)
        subjects_text = extract_block(r"<div class='list-subjects'.*?</span>(.*?)</div>", chunk)
        subjects = [part.strip() for part in subjects_text.split(";")] if subjects_text else []
        html_match = re.search(r'href="(https://arxiv\.org/html/[^"]+)"[^>]*>\s*html\s*</a>', chunk)
        html_url = html_match.group(1) if html_match else None
        primary_subject = subjects[0] if subjects else None
        entries.append(
            ManifestEntry(
                arxiv_id=arxiv_id,
                topic=topic,
                month=month,
                listing_index=offset + chunk_index,
                title=title,
                comments=comments,
                page_count=parse_page_count(comments),
                has_html=html_url is not None,
                html_url=html_url,
                pdf_url=f"{ARXIV_BASE}/pdf/{urllib.parse.quote(arxiv_id)}",
                abs_url=f"{ARXIV_BASE}/abs/{urllib.parse.quote(arxiv_id)}",
                subjects=subjects,
                primary_subject=primary_subject,
                categories=parse_categories(subjects),
            )
        )
    return total, entries


def fetch_manifest(topic: str, month: str, sleep: float) -> list[ManifestEntry]:
    entries_by_id: dict[str, ManifestEntry] = {}
    total = None
    skip = 0
    while True:
        url = f"{ARXIV_LIST_BASE}/{topic}/{month}?skip={skip}&show={PAGE_SIZE}"
        page_total, entries = parse_articles(fetch_text(url), topic, month, skip)
        total = total if total is not None else page_total
        for entry in entries:
            entries_by_id[entry.arxiv_id] = entry
        if total is None or len(entries_by_id) >= total or not entries:
            break
        skip += PAGE_SIZE
        time.sleep(sleep)
    return sorted(entries_by_id.values(), key=lambda entry: entry.listing_index)


def sort_smallest(entries: list[ManifestEntry]) -> list[ManifestEntry]:
    return sorted(
        entries,
        key=lambda entry: (
            not entry.has_html,
            entry.page_count is None,
            entry.page_count if entry.page_count is not None else 10**9,
            entry.listing_index,
        ),
    )


def render_summary(entries: list[ManifestEntry]) -> str:
    html_count = sum(1 for entry in entries if entry.has_html)
    lines = [
        f"# arXiv Manifest: `{entries[0].topic}` {entries[0].month}" if entries else "# arXiv Manifest",
        "",
        f"- Entries: {len(entries)}",
        f"- HTML available: {html_count}",
        "",
        "## Smallest HTML Candidates",
        "",
        "| Rank | arXiv ID | Pages | Title | Comments |",
        "|---:|---|---:|---|---|",
    ]
    for rank, entry in enumerate([entry for entry in sort_smallest(entries) if entry.has_html][:12], start=1):
        pages = str(entry.page_count) if entry.page_count is not None else "?"
        comments = (entry.comments or "").replace("|", "\\|")
        title = entry.title.replace("|", "\\|")
        lines.append(
            f"| {rank} | [{entry.arxiv_id}]({entry.abs_url}) | {pages} | {title} | {comments} |"
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    entries = fetch_manifest(args.topic, args.month, args.sleep)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "\n".join(json.dumps(asdict(entry), sort_keys=True) for entry in entries) + "\n",
        encoding="utf-8",
    )
    if args.summary_output:
        summary_path = Path(args.summary_output)
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(render_summary(entries) + "\n", encoding="utf-8")
    print(render_summary(entries))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
