#!/usr/bin/env python3
"""Count arXiv monthly entries for candidate review-layer launch topics.

The default source is arXiv's public monthly list pages, which expose a
"Total of N entries" count for each category. The official Atom API path is
also available, but it is often rate-limited more aggressively.
"""

from __future__ import annotations

import argparse
import calendar
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


ARXIV_LIST_BASE = "https://arxiv.org/list"
ARXIV_API_BASE = "https://export.arxiv.org/api/query"
USER_AGENT = "arxiv-review-layer-counts/0.1 (local research script)"


TOPICS = {
    "math": {
        "label": "Mathematics",
        "list_archive": "math",
        "api_query": "cat:math.*",
        "fit": "Too broad for a first launch, but useful as the parent volume check.",
    },
    "math.AC": {
        "label": "Commutative Algebra",
        "list_archive": "math.AC",
        "api_query": "cat:math.AC",
        "fit": "Proof-heavy and legible; specialized audience.",
    },
    "math.AG": {
        "label": "Algebraic Geometry",
        "list_archive": "math.AG",
        "api_query": "cat:math.AG",
        "fit": "Proof-heavy and prestigious; high specialist-depth risk.",
    },
    "math.AP": {
        "label": "Analysis of PDEs",
        "list_archive": "math.AP",
        "api_query": "cat:math.AP",
        "fit": "Good for theorem/hypothesis checks; technical estimates can be hard.",
    },
    "math.AT": {
        "label": "Algebraic Topology",
        "list_archive": "math.AT",
        "api_query": "cat:math.AT",
        "fit": "Proof-heavy; specialist notation can be dense.",
    },
    "math.CA": {
        "label": "Classical Analysis and ODEs",
        "list_archive": "math.CA",
        "api_query": "cat:math.CA",
        "fit": "Good derivation and assumption-check surface.",
    },
    "math.CO": {
        "label": "Combinatorics",
        "list_archive": "math.CO",
        "api_query": "cat:math.CO",
        "fit": "Often legible via counterexamples, constructions, and proof checks.",
    },
    "math.CT": {
        "label": "Category Theory",
        "list_archive": "math.CT",
        "api_query": "cat:math.CT",
        "fit": "Low volume, but high abstraction and notation sensitivity.",
    },
    "math.CV": {
        "label": "Complex Variables",
        "list_archive": "math.CV",
        "api_query": "cat:math.CV",
        "fit": "Good theorem/hypothesis review surface.",
    },
    "math.DG": {
        "label": "Differential Geometry",
        "list_archive": "math.DG",
        "api_query": "cat:math.DG",
        "fit": "Good fit near mathematical physics; specialist calculations matter.",
    },
    "math.DS": {
        "label": "Dynamical Systems",
        "list_archive": "math.DS",
        "api_query": "cat:math.DS",
        "fit": "Good for stability, examples, and theorem-condition checks.",
    },
    "math.FA": {
        "label": "Functional Analysis",
        "list_archive": "math.FA",
        "api_query": "cat:math.FA",
        "fit": "Strong operator/proof surface; good overlap with math-ph.",
    },
    "math.GM": {
        "label": "General Mathematics",
        "list_archive": "math.GM",
        "api_query": "cat:math.GM",
        "fit": "Low volume but noisy and less prestigious as a launch category.",
    },
    "math.GN": {
        "label": "General Topology",
        "list_archive": "math.GN",
        "api_query": "cat:math.GN",
        "fit": "Low volume and proof-heavy; narrow audience.",
    },
    "math.GR": {
        "label": "Group Theory",
        "list_archive": "math.GR",
        "api_query": "cat:math.GR",
        "fit": "Good proof/counterexample surface.",
    },
    "math.GT": {
        "label": "Geometric Topology",
        "list_archive": "math.GT",
        "api_query": "cat:math.GT",
        "fit": "Specialist but proof-heavy; diagrams may matter.",
    },
    "math.HO": {
        "label": "History and Overview",
        "list_archive": "math.HO",
        "api_query": "cat:math.HO",
        "fit": "Low volume, but less aligned with technical review.",
    },
    "math.IT": {
        "label": "Information Theory",
        "list_archive": "math.IT",
        "api_query": "cat:math.IT",
        "fit": "Good theorem/empirical boundary; alias overlap with cs.IT.",
    },
    "math.KT": {
        "label": "K-Theory and Homology",
        "list_archive": "math.KT",
        "api_query": "cat:math.KT",
        "fit": "Low volume and technical; specialist-depth risk.",
    },
    "math.LO": {
        "label": "Logic",
        "list_archive": "math.LO",
        "api_query": "cat:math.LO",
        "fit": "Good formal surface; may benefit from proof-assistant adjacency.",
    },
    "math.MG": {
        "label": "Metric Geometry",
        "list_archive": "math.MG",
        "api_query": "cat:math.MG",
        "fit": "Moderate proof surface; specialized audience.",
    },
    "quant-ph": {
        "label": "Quantum Physics",
        "list_archive": "quant-ph",
        "api_query": "cat:quant-ph",
        "fit": "Good error legibility for derivation/foundations claims, but broad.",
    },
    "math-ph": {
        "label": "Mathematical Physics",
        "list_archive": "math-ph",
        "api_query": "cat:math-ph",
        "fit": "Strong theorem/derivation legibility; narrower than quant-ph.",
    },
    "math.MP": {
        "label": "Mathematical Physics",
        "list_archive": "math-ph",
        "api_query": "cat:math.MP",
        "fit": "Alias for math-ph; use math-ph for public URLs.",
    },
    "math.NA": {
        "label": "Numerical Analysis",
        "list_archive": "math.NA",
        "api_query": "cat:math.NA",
        "fit": "Good algorithmic and error-bound checks; some empirical validation.",
    },
    "math.NT": {
        "label": "Number Theory",
        "list_archive": "math.NT",
        "api_query": "cat:math.NT",
        "fit": "Proof-heavy and visible; high specialist-depth risk.",
    },
    "math.OA": {
        "label": "Operator Algebras",
        "list_archive": "math.OA",
        "api_query": "cat:math.OA",
        "fit": "Strong overlap with quantum/math-ph; good technical review target.",
    },
    "math.OC": {
        "label": "Optimization and Control",
        "list_archive": "math.OC",
        "api_query": "cat:math.OC",
        "fit": "Good for theorem-condition and systems/control checks.",
    },
    "math.PR": {
        "label": "Probability",
        "list_archive": "math.PR",
        "api_query": "cat:math.PR",
        "fit": "Good theorem/asymptotic checks; high volume.",
    },
    "math.QA": {
        "label": "Quantum Algebra",
        "list_archive": "math.QA",
        "api_query": "cat:math.QA",
        "fit": "Good math-physics bridge; specialist notation risk.",
    },
    "math.RA": {
        "label": "Rings and Algebras",
        "list_archive": "math.RA",
        "api_query": "cat:math.RA",
        "fit": "Proof-heavy; moderate volume.",
    },
    "math.RT": {
        "label": "Representation Theory",
        "list_archive": "math.RT",
        "api_query": "cat:math.RT",
        "fit": "Good proof surface; high specialist-depth risk.",
    },
    "math.SG": {
        "label": "Symplectic Geometry",
        "list_archive": "math.SG",
        "api_query": "cat:math.SG",
        "fit": "Good physics-adjacent launch candidate.",
    },
    "math.SP": {
        "label": "Spectral Theory",
        "list_archive": "math.SP",
        "api_query": "cat:math.SP",
        "fit": "Excellent fit for operator/quantum/math-ph review.",
    },
    "math.ST": {
        "label": "Statistics Theory",
        "list_archive": "math.ST",
        "api_query": "cat:math.ST",
        "fit": "Good theory/empirical boundary; alias overlap with stat.TH.",
    },
    "hep-th": {
        "label": "High Energy Physics - Theory",
        "list_archive": "hep-th",
        "api_query": "cat:hep-th",
        "fit": "Technical and high-volume; good for theory critique but harder to validate.",
    },
    "cond-mat.stat-mech": {
        "label": "Condensed Matter - Statistical Mechanics",
        "list_archive": "cond-mat.stat-mech",
        "api_query": "cat:cond-mat.stat-mech",
        "fit": "Good theory/derivation checks; moderate specialization.",
    },
    "cs.LG": {
        "label": "Machine Learning",
        "list_archive": "cs.LG",
        "api_query": "cat:cs.LG",
        "fit": "Excellent baseline/evidence checks, but too high-volume for a first pass.",
    },
    "stat.ML": {
        "label": "Machine Learning - Statistics",
        "list_archive": "stat.ML",
        "api_query": "cat:stat.ML",
        "fit": "Good math/empirical legibility; overlaps heavily with cs.LG.",
    },
    "cs.AI": {
        "label": "Artificial Intelligence",
        "list_archive": "cs.AI",
        "api_query": "cat:cs.AI",
        "fit": "Readable to a broad audience, but topic boundaries are loose.",
    },
    "cs.CL": {
        "label": "Computation and Language",
        "list_archive": "cs.CL",
        "api_query": "cat:cs.CL",
        "fit": "Good benchmark/evaluation checks; high model-relevance and fast-moving.",
    },
    "cs.CV": {
        "label": "Computer Vision and Pattern Recognition",
        "list_archive": "cs.CV",
        "api_query": "cat:cs.CV",
        "fit": "Good empirical-review target; very high volume and benchmark gaming risk.",
    },
    "cs.RO": {
        "label": "Robotics",
        "list_archive": "cs.RO",
        "api_query": "cat:cs.RO",
        "fit": "Moderate volume; empirical claims often need hardware context.",
    },
    "cs.CR": {
        "label": "Cryptography and Security",
        "list_archive": "cs.CR",
        "api_query": "cat:cs.CR",
        "fit": "Good theorem/attack legibility; some security claims require live context.",
    },
    "eess.SY": {
        "label": "Systems and Control",
        "list_archive": "eess.SY",
        "api_query": "cat:eess.SY",
        "fit": "Moderate volume; strong fit for control-theory and stability checks.",
    },
    "q-bio": {
        "label": "Quantitative Biology",
        "list_archive": "q-bio",
        "api_query": "cat:q-bio.*",
        "fit": "Interesting but less legible without wet-lab/domain-specific validation.",
    },
}


TOPIC_SETS = {
    "default": [
        "quant-ph",
        "math-ph",
        "hep-th",
        "cond-mat.stat-mech",
        "cs.LG",
        "stat.ML",
        "cs.AI",
        "cs.CL",
        "cs.CV",
        "cs.RO",
        "cs.CR",
        "eess.SY",
        "q-bio",
    ],
    "math": [
        "math",
        "math.AC",
        "math.AG",
        "math.AP",
        "math.AT",
        "math.CA",
        "math.CO",
        "math.CT",
        "math.CV",
        "math.DG",
        "math.DS",
        "math.FA",
        "math.GM",
        "math.GN",
        "math.GR",
        "math.GT",
        "math.HO",
        "math.IT",
        "math.KT",
        "math.LO",
        "math.MG",
        "math-ph",
        "math.NA",
        "math.NT",
        "math.OA",
        "math.OC",
        "math.PR",
        "math.QA",
        "math.RA",
        "math.RT",
        "math.SG",
        "math.SP",
        "math.ST",
    ],
}


@dataclass
class CountResult:
    topic: str
    label: str
    month: str
    source: str
    count: int | None
    url: str
    fit: str
    error: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count arXiv entries for candidate launch topics."
    )
    parser.add_argument(
        "--month",
        required=True,
        help="Month to count, in YYYY-MM format. Example: 2026-04.",
    )
    parser.add_argument(
        "--source",
        choices=("list", "api"),
        default="list",
        help="arXiv source to query. Default: monthly list pages.",
    )
    parser.add_argument(
        "--topics",
        default=None,
        help=(
            "Comma-separated topic keys. Use --list-topics to see options. "
            "Default: the selected topic set."
        ),
    )
    parser.add_argument(
        "--topic-set",
        choices=tuple(TOPIC_SETS),
        default="default",
        help="Named topic set to count when --topics is omitted. Default: default.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=1.0,
        help="Seconds to sleep between requests. Default: 1.0.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON instead of a Markdown table.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write the same output that is printed.",
    )
    parser.add_argument(
        "--list-topics",
        action="store_true",
        help="List configured topic keys and exit.",
    )
    return parser.parse_args()


def validate_month(month: str) -> None:
    if not re.fullmatch(r"\d{4}-\d{2}", month):
        raise ValueError("month must be in YYYY-MM format")
    year, month_num = [int(part) for part in month.split("-")]
    if month_num < 1 or month_num > 12:
        raise ValueError("month must be between 01 and 12")
    if year < 1991:
        raise ValueError("arXiv did not exist before 1991")


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def count_from_list(topic: str, month: str) -> CountResult:
    cfg = TOPICS[topic]
    archive = cfg["list_archive"]
    url = f"{ARXIV_LIST_BASE}/{archive}/{month}?skip=0&show=25"
    try:
        html = fetch_text(url)
        match = re.search(r"Total of\s+([\d,]+)\s+entries", html)
        if not match:
            title = re.search(r"<title>(.*?)</title>", html, re.DOTALL)
            title_text = re.sub(r"\s+", " ", title.group(1)).strip() if title else ""
            raise RuntimeError(f"could not find total count; page title={title_text!r}")
        count = int(match.group(1).replace(",", ""))
        return CountResult(topic, cfg["label"], month, "list", count, url, cfg["fit"])
    except Exception as exc:  # noqa: BLE001 - keep batch runs going.
        return CountResult(topic, cfg["label"], month, "list", None, url, cfg["fit"], str(exc))


def api_date_range(month: str) -> tuple[str, str]:
    year, month_num = [int(part) for part in month.split("-")]
    last_day = calendar.monthrange(year, month_num)[1]
    start = f"{year:04d}{month_num:02d}010000"
    end = f"{year:04d}{month_num:02d}{last_day:02d}2359"
    return start, end


def count_from_api(topic: str, month: str) -> CountResult:
    cfg = TOPICS[topic]
    start, end = api_date_range(month)
    search_query = f"{cfg['api_query']} AND submittedDate:[{start} TO {end}]"
    params = {
        "search_query": search_query,
        "start": "0",
        "max_results": "0",
    }
    url = f"{ARXIV_API_BASE}?{urllib.parse.urlencode(params)}"
    try:
        xml_text = fetch_text(url)
        root = ET.fromstring(xml_text)
        ns = {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"}
        total = root.findtext("opensearch:totalResults", namespaces=ns)
        if total is None:
            raise RuntimeError("could not find opensearch:totalResults")
        return CountResult(topic, cfg["label"], month, "api", int(total), url, cfg["fit"])
    except Exception as exc:  # noqa: BLE001 - keep batch runs going.
        return CountResult(topic, cfg["label"], month, "api", None, url, cfg["fit"], str(exc))


def render_json(results: list[CountResult]) -> str:
    payload = {
        "generated_by": Path(__file__).as_posix(),
        "results": [result.__dict__ for result in results],
    }
    return json.dumps(payload, indent=2, sort_keys=True)


def render_markdown(results: list[CountResult]) -> str:
    lines = [
        "| Topic | Label | Count | Source | Notes |",
        "|---|---:|---:|---|---|",
    ]
    for result in results:
        count = str(result.count) if result.count is not None else "ERROR"
        notes = result.fit
        if result.error:
            notes = f"{notes} Error: {result.error}"
        lines.append(
            f"| `{result.topic}` | {result.label} | {count} | "
            f"[{result.source}]({result.url}) | {notes} |"
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    if args.list_topics:
        print("Topic sets:")
        for name, topics in TOPIC_SETS.items():
            print(f"{name}\t{','.join(topics)}")
        print("\nTopics:")
        for topic, cfg in TOPICS.items():
            print(f"{topic}\t{cfg['label']}\t{cfg['fit']}")
        return 0

    validate_month(args.month)
    topics = args.topics if args.topics is not None else ",".join(TOPIC_SETS[args.topic_set])
    topic_keys = [topic.strip() for topic in topics.split(",") if topic.strip()]
    unknown = [topic for topic in topic_keys if topic not in TOPICS]
    if unknown:
        print(f"Unknown topic(s): {', '.join(unknown)}", file=sys.stderr)
        print("Run with --list-topics for valid keys.", file=sys.stderr)
        return 2

    results = []
    for index, topic in enumerate(topic_keys):
        if index:
            time.sleep(args.sleep)
        if args.source == "list":
            results.append(count_from_list(topic, args.month))
        else:
            results.append(count_from_api(topic, args.month))

    output = render_json(results) if args.json else render_markdown(results)
    print(output)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output + "\n", encoding="utf-8")

    return 1 if any(result.error for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
