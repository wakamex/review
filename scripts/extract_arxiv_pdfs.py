#!/usr/bin/env python3
"""Extract Markdown/text from downloaded arXiv PDFs.

This implements the extraction chain summarized in
`/code/pdf-extraction/RESULTS.md`:

- `pymupdf4llm`: best local/free default for text-based PDFs.
- `pdfplumber`: useful when tables are the focus.
- `pdfminer`: plain-text fallback.
- `pymupdf-text`: fastest raw-text fallback.
- `gemini`: high-quality OCR/LaTeX extraction for scanned PDFs, opt-in.

Firecrawl is intentionally not called here yet; it is best treated as a
separate URL-based extractor because it works from the PDF URL rather than the
local PDF asset.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import time
from pathlib import Path


LOCAL_METHODS = {"pymupdf4llm", "pdfplumber", "pdfminer", "pymupdf-text"}
METHODS = tuple(sorted(LOCAL_METHODS | {"gemini"}))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assets-dir", required=True, help="Directory containing per-paper assets.")
    parser.add_argument(
        "--method",
        choices=METHODS,
        default="pymupdf4llm",
        help="Extraction method. Default: pymupdf4llm.",
    )
    parser.add_argument(
        "--only-pdf",
        action="store_true",
        help="Only process papers with a downloaded paper.pdf asset.",
    )
    parser.add_argument("--limit", type=int, help="Optional max number of PDFs to process.")
    parser.add_argument("--sleep", type=float, default=0.0, help="Sleep between extractions.")
    parser.add_argument(
        "--gemini-model",
        default="gemini-3-flash-preview",
        help="Gemini model for --method gemini.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing extraction output.",
    )
    return parser.parse_args()


def extract_pymupdf4llm(pdf_path: Path) -> str:
    import pymupdf4llm

    return pymupdf4llm.to_markdown(str(pdf_path))


def extract_pdfplumber(pdf_path: Path) -> str:
    import pdfplumber

    parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            parts.append(page.extract_text() or "")
            for table_index, table in enumerate(page.extract_tables(), start=1):
                parts.append(f"\n[TABLE page={page.page_number} index={table_index}]")
                for row in table:
                    parts.append(" | ".join(str(cell or "") for cell in row))
    return "\n\n".join(parts)


def extract_pdfminer(pdf_path: Path) -> str:
    from pdfminer.high_level import extract_text

    return extract_text(str(pdf_path))


def extract_pymupdf_text(pdf_path: Path) -> str:
    import fitz

    doc = fitz.open(pdf_path)
    return "\n\n".join(page.get_text("text") for page in doc)


def extract_gemini(pdf_path: Path, model: str) -> str:
    gemini = shutil.which("gemini")
    if not gemini:
        raise RuntimeError("gemini CLI not found on PATH")
    prompt = (
        "Extract the complete text of this academic PDF into clean Markdown. "
        "Preserve section headings, theorem/proposition/lemma statements, proof "
        "structure, equations as LaTeX, figure captions, and bibliography. "
        "Do not summarize. @"
        + pdf_path.name
    )
    result = subprocess.run(
        [
            gemini,
            "-m",
            model,
            "-y",
            "-p",
            prompt,
            "--output-format",
            "text",
        ],
        cwd=pdf_path.parent,
        text=True,
        capture_output=True,
        timeout=300,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "gemini extraction failed")
    return result.stdout


def extract(pdf_path: Path, method: str, gemini_model: str) -> str:
    if method == "pymupdf4llm":
        return extract_pymupdf4llm(pdf_path)
    if method == "pdfplumber":
        return extract_pdfplumber(pdf_path)
    if method == "pdfminer":
        return extract_pdfminer(pdf_path)
    if method == "pymupdf-text":
        return extract_pymupdf_text(pdf_path)
    if method == "gemini":
        return extract_gemini(pdf_path, gemini_model)
    raise ValueError(f"unknown method: {method}")


def iter_pdf_assets(assets_dir: Path) -> list[Path]:
    return sorted(assets_dir.glob("*/paper.pdf"))


def main() -> int:
    args = parse_args()
    assets_dir = Path(args.assets_dir)
    pdfs = iter_pdf_assets(assets_dir)
    if args.limit is not None:
        pdfs = pdfs[: args.limit]

    records = []
    for index, pdf_path in enumerate(pdfs):
        paper_dir = pdf_path.parent
        out_dir = paper_dir / "extracted"
        suffix = "md" if args.method in {"pymupdf4llm", "gemini"} else "txt"
        output_path = out_dir / f"{args.method}.{suffix}"
        record = {
            "arxiv_id": paper_dir.name,
            "pdf_path": str(pdf_path),
            "method": args.method,
            "output_path": str(output_path),
            "status": "pending",
        }
        try:
            if output_path.exists() and not args.overwrite:
                record["status"] = "exists"
                record["chars"] = len(output_path.read_text(encoding="utf-8", errors="replace"))
            else:
                if index and args.sleep:
                    time.sleep(args.sleep)
                started = time.time()
                text = extract(pdf_path, args.method, args.gemini_model)
                out_dir.mkdir(parents=True, exist_ok=True)
                output_path.write_text(text, encoding="utf-8")
                record["status"] = "extracted"
                record["chars"] = len(text)
                record["seconds"] = round(time.time() - started, 3)
            (out_dir / f"{args.method}.json").write_text(
                json.dumps(record, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
        except Exception as exc:  # noqa: BLE001 - batch extraction should continue.
            record["status"] = "error"
            record["error"] = str(exc)
        records.append(record)
        print(json.dumps(record, sort_keys=True))

    summary = {
        "assets_dir": str(assets_dir),
        "method": args.method,
        "processed": len(records),
        "ok": sum(1 for record in records if record["status"] in {"extracted", "exists"}),
        "errors": sum(1 for record in records if record["status"] == "error"),
        "records": records,
    }
    (assets_dir / f"pdf_extraction_{args.method}.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 1 if summary["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
