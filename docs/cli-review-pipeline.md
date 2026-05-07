# CLI Review Pipeline

This project can be instrumented entirely through command-line model runners.
The deterministic pipeline should be normal scripts. The LLMs should be
stateless subprocesses that receive explicit paper bundles and return structured
JSON.

Useful local references:

- `/code/paperclip/doc/spec/agent-runs.md` documents `claude --print` and
  `codex exec --json` adapters.
- `/code/loophole/loophole/llm.py` wraps `claude -p` with JSON output, no
  tools, no session persistence, and a system-prompt file.
- `/code/skills/skills/skill-creator/scripts/run_eval.py` removes
  `CLAUDECODE` before nesting `claude -p` inside another Claude/Codex session.

## Principle

Use scripts for everything deterministic:

- arXiv discovery
- download
- parsing
- prompt assembly
- subprocess execution
- JSON validation
- retries
- artifact storage
- board synthesis
- static-site rendering

Use model CLIs only for bounded judgment tasks:

- claim extraction
- independent review
- cross-review
- final synthesis
- author-response re-review

The model should not decide what files exist, where state lives, or whether a
paper has already been reviewed.

## End-To-End Flow

1. Build monthly manifest.

   For the first leaf, query `math.SG`:

   ```bash
   python3 scripts/count_arxiv_month.py \
     --month 2026-04 \
     --topics math.SG \
     --source list
   ```

   A real manifest script should output one JSONL row per paper:

   ```json
   {"arxiv_id":"2604.01009","primary_category":"math.SG","month":"2026-04","abs_url":"https://arxiv.org/abs/2604.01009"}
   ```

2. Fetch paper assets.

   Preferred source order:

   - arXiv HTML, when available
   - arXiv source TeX, when available
   - PDF text extraction fallback

   Store raw inputs and parser metadata. Do not overwrite old versions.

3. Build a paper bundle.

   Create a compact review input:

   - metadata
   - abstract
   - subject/cross-list categories
   - table of contents
   - theorem/proposition/lemma statements
   - introduction and conclusion
   - selected proof chunks
   - bibliography titles/authors if extractable
   - parser warnings

   The bundle is the only content given to first-pass reviewers. This makes
   reviews reproducible and keeps prompt injection quarantined.

4. Run independent reviewers.

   Each reviewer gets the same bundle and the same schema. They do not see each
   other yet.

   Claude:

   ```bash
   env -u CLAUDECODE claude -p \
     --tools "" \
     --no-session-persistence \
     --output-format json \
     --json-schema "$(cat schemas/review.schema.json)" \
     --system-prompt-file prompts/reviewer_math_sg.md \
     < runs/2026-04/math.SG/papers/2604.01009/bundle.md \
     > runs/2026-04/math.SG/papers/2604.01009/reviews/claude.json
   ```

   Codex:

   ```bash
   codex exec \
     --json \
     --ephemeral \
     --sandbox read-only \
     --skip-git-repo-check \
     --output-schema schemas/review.schema.json \
     -o runs/2026-04/math.SG/papers/2604.01009/reviews/codex.json \
     "$(cat prompts/reviewer_math_sg_codex.md runs/2026-04/math.SG/papers/2604.01009/bundle.md)" \
     > runs/2026-04/math.SG/papers/2604.01009/logs/codex.jsonl
   ```

   Gemini:

   ```bash
   gemini -p "$(cat prompts/reviewer_math_sg_gemini.md runs/2026-04/math.SG/papers/2604.01009/bundle.md)" \
     --approval-mode plan \
     --output-format json \
     > runs/2026-04/math.SG/papers/2604.01009/reviews/gemini.json
   ```

   For v1, disable tools or run in read-only/plan mode. Any literature lookup
   should be a separate deterministic retrieval stage, not an uncontrolled model
   browser action.

5. Validate and normalize.

   Parse each CLI's native output:

   - Claude returns one JSON object with `result`, `session_id`, usage, and cost.
     When `--json-schema` is used, the schema-conforming payload may appear in
     `structured_output` while `result` contains prose or is empty; adapters
     should prefer `structured_output`.
   - Codex returns JSONL events; extract the final `agent_message`, thread id,
     and `turn.completed.usage`.
   - Gemini can emit JSON/text depending on flags; wrap and validate exactly as
     a provider-specific adapter.

   Store:

   - raw stdout
   - raw stderr
   - parsed review JSON
   - usage
   - model/version
   - command argv
   - prompt hash
   - bundle hash
   - exit code

6. Cross-review.

   Run each model against the other reviews:

   - Which objections are valid?
   - Which objections are hallucinated or unsupported?
   - What did everyone miss?
   - Which claims need human spot-checking?

7. Board synthesis.

   Feed the paper bundle, independent reviews, and cross-reviews into a final
   synthesis prompt. Output both JSON and Markdown:

   - verdict
   - confidence
   - strongest supported claims
   - strongest objections
   - weak/speculative objections
   - suggested author questions
   - public summary

8. Publish.

   Generate static pages from artifacts:

   - paper page
   - monthly issue
   - review JSON download
   - author response page
   - correction log

## Artifact Layout

```text
runs/
  2026-04/
    math.SG/
      manifest.jsonl
      issue.md
      papers/
        2604.01009/
          metadata.json
          source/
          parsed/
            paper.md
            sections.json
            extraction_warnings.json
          bundle.md
          reviews/
            claude.json
            codex.json
            gemini.json
          cross_reviews/
            claude.json
            codex.json
            gemini.json
          board/
            report.json
            report.md
          logs/
            claude.stdout.json
            claude.stderr.txt
            codex.jsonl
            codex.stderr.txt
            gemini.stdout.json
            gemini.stderr.txt
```

## Review Schema Sketch

The first-pass review schema should be conservative:

```json
{
  "paper_id": "2604.01009",
  "reviewer": "claude|codex|gemini",
  "summary": "...",
  "main_claims": [],
  "technical_objections": [
    {
      "claim": "...",
      "paper_location": "...",
      "objection": "...",
      "evidence": "...",
      "severity": "minor|moderate|major",
      "confidence": 0.0
    }
  ],
  "missing_assumptions": [],
  "novelty_assessment": "...",
  "recommended_verdict": "strong_select|promising|routine|weak_evidence|major_flaw|contested",
  "confidence": 0.0,
  "overall_score_10": 7.2,
  "dimension_scores": {
    "technical_soundness": 7,
    "novelty": 8,
    "significance": 8,
    "clarity": 6,
    "reviewer_confidence": 6
  },
  "score_rationale": "..."
}
```

The run harness also emits a compact `score_summary` at the end of
`review_run_summary.json` and stdout. That block repeats only the information
needed for ranking and dashboards: reviewer, overall score, dimension scores,
board verdict, board confidence, and board score. It also includes a
mechanical average for each review cycle, plus the board score delta against
the final-cycle mechanical average, so synthesis drift is visible. The selected
final score defaults to the final-cycle mechanical average; pass
`--score-source board` to use the board synthesizer's score instead.

## Why CLI-Only Works

CLI-only is enough because this system is batch-oriented:

- each paper is a file bundle
- each model pass is a subprocess
- each output is an artifact
- each artifact is hashable, retryable, and inspectable
- no long-lived agent memory is required

The first production version can be a set of Python scripts plus cron/GitHub
Actions/systemd timers. A database and web app can come later once the review
artifact format is stable.

## CLI Smoke Test

Check the local command surfaces without making paid model calls:

```bash
python3 scripts/smoke_model_clis.py
```

Run tiny model-backed prompts only when intentionally testing credentials and
JSON parsing:

```bash
python3 scripts/smoke_model_clis.py --execute
```

## Repeated Review Cycles

Use artifact-fed review cycles, not hidden CLI chat history.

The harness is:

```bash
python3 scripts/run_review_cycle.py \
  --source-manifest runs/2026-04/math.SG/source_manifest.jsonl \
  --paper-id 2604.19237 \
  --build-bundle \
  --cycles 2 \
  --board \
  --providers claude,codex,gemini
```

By default this is a dry run. It builds `bundle.md`, then writes prompt files
and command previews for every reviewer/cycle without spending model tokens.

To actually run the model CLIs:

```bash
python3 scripts/run_review_cycle.py \
  --source-manifest runs/2026-04/math.SG/source_manifest.jsonl \
  --paper-id 2604.19237 \
  --cycles 2 \
  --board \
  --providers claude,codex,gemini \
  --execute
```

Use `--score-source board` only when the qualitative board synthesizer should
control the selected ranking score. The default `--score-source mechanical`
keeps the board report as synthesis while using the final-cycle score average
for ranking.

Cycle semantics:

- Cycle 1: each reviewer receives only the paper bundle and review schema.
- Cycle 2+: each reviewer receives the paper bundle, its own previous JSON
  review, and the other reviewers' previous JSON reviews.
- Board synthesis receives the paper bundle and all review-cycle artifacts.

Artifacts for the first test paper live under:

```text
runs/2026-04/math.SG/papers/2604.19237/
  bundle.md
  metadata.json
  review_cycles/
    cycle_01/reviews/{claude,codex,gemini}.prompt.md
    cycle_02/reviews/{claude,codex,gemini}.prompt.md
  board/claude.prompt.md
  review_run_summary.json
```

### Should We Reuse CLI Sessions?

No, not as the primary mechanism.

For this product, the reliable unit of state should be a file artifact:

- paper bundle
- prompt
- raw stdout/stderr
- parsed review JSON
- usage/cost metadata
- board report

Do not rely on a hidden Claude/Codex/Gemini session to remember prior rounds.
That makes reviews harder to reproduce, audit, diff, retry, or migrate between
providers. It also weakens reviewer independence because the model's private
conversation history becomes part of the review state.

The right CLI pattern is:

```text
cycle_01: bundle -> reviewer JSON
cycle_02: bundle + cycle_01 own review + cycle_01 other reviews -> revised reviewer JSON
cycle_03: bundle + cycle_02 own review + cycle_02 other reviews -> revised reviewer JSON
board: bundle + all review JSON -> board report JSON
```

CLI resume can still be useful for debugging or cost experiments:

- Claude: persist the first call's `session_id`, then call
  `claude -p --resume <session_id> ...`.
- Codex: persist `thread.started.thread_id`, then call
  `codex exec --json resume <thread_id> -`.
- Gemini: use `gemini --resume <session> -p ...` if session persistence is
  enabled.

But this should be an optional adapter mode, not the canonical harness. The
canonical mode should keep `claude --no-session-persistence` and
`codex --ephemeral` for clean replayability.

## First Implementation Slice

For `math.SG`, implement:

1. `build_manifest.py`: produce `manifest.jsonl` for one month.
2. `fetch_paper.py`: download HTML/source/PDF into `runs/.../source`.
3. `build_bundle.py`: create `bundle.md`.
4. `run_review.py`: run one provider adapter against one bundle.
5. `run_board.py`: run cross-review and synthesis.
6. `render_static.py`: write a paper page and monthly issue.

This keeps the system boring in the best way: scripts in, artifacts out.

## First Real Paper

Use `2604.19237` as the first smoke-test paper:

- Title: "Bott-integrable contact forms with large systolic ratio"
- Category: `math.SG`
- Month: April 2026
- Size signal: 10 pages, 3 figures
- HTML: `https://arxiv.org/html/2604.19237v1`
- Local asset: `runs/2026-04/math.SG/assets/2604.19237/paper.html`

It tied for the smallest reported HTML-available April `math.SG` paper, but is
a cleaner first review target than the other 10-page candidate because it looks
like a compact technical paper rather than a note/version-refinement case.

Build the April `math.SG` manifest:

```bash
python3 scripts/build_arxiv_manifest.py \
  --month 2026-04 \
  --topic math.SG \
  --output runs/2026-04/math.SG/manifest.jsonl \
  --summary-output runs/2026-04/math.SG/manifest_summary.md \
  --sleep 0.35
```

Download all HTML-available April `math.SG` papers:

```bash
python3 scripts/download_arxiv_assets.py \
  --manifest runs/2026-04/math.SG/manifest.jsonl \
  --out-dir runs/2026-04/math.SG/assets \
  --prefer html \
  --fallback none \
  --sleep 0.5
```

April `math.SG` result:

- 49 manifest entries
- 40 HTML assets downloaded
- 9 papers skipped because no arXiv HTML asset was listed

Do not download every PDF up front. Keep PDFs/source as lazy fallback assets for
papers without HTML or for cases where HTML extraction fails.

## PDF Fallback Extraction

PDF extraction follows the method comparison in `/code/pdf-extraction/RESULTS.md`
(`/code/pdf-extract/RESULTS.md` was the intended path, but the local directory is
named `pdf-extraction`).

Extraction policy:

- Prefer arXiv HTML when available.
- For papers without HTML, download the PDF.
- Use `pymupdf4llm` first: it is the best local/free method from the comparison.
- Escalate to Gemini CLI when the PDF is scanned/image-only or when LaTeX math
  fidelity is more important than speed/cost.
- Use Firecrawl only as an optional high-quality URL-based parser when credits
  are available.
- Use `pdfplumber` when table extraction is the specific concern.
- Keep `pdfminer` and raw PyMuPDF text as plain-text fallbacks.

Download PDF fallbacks for non-HTML papers while leaving HTML papers unchanged:

```bash
python3 scripts/download_arxiv_assets.py \
  --manifest runs/2026-04/math.SG/manifest.jsonl \
  --out-dir runs/2026-04/math.SG/assets \
  --prefer html \
  --fallback pdf \
  --sleep 0.5
```

Extract the downloaded PDF fallbacks with the local/free method:

```bash
python3 scripts/extract_arxiv_pdfs.py \
  --assets-dir runs/2026-04/math.SG/assets \
  --method pymupdf4llm \
  --only-pdf
```

April `math.SG` PDF fallback result:

- 9 PDFs downloaded for papers with no arXiv HTML asset
- 9 Markdown extractions produced with `pymupdf4llm`
- Summary artifact:
  `runs/2026-04/math.SG/assets/pdf_extraction_pymupdf4llm.json`

Build the unified review source manifest:

```bash
python3 scripts/build_review_source_manifest.py \
  --manifest runs/2026-04/math.SG/manifest.jsonl \
  --assets-dir runs/2026-04/math.SG/assets \
  --output runs/2026-04/math.SG/source_manifest.jsonl \
  --pdf-method pymupdf4llm
```

Current source coverage:

- 49/49 April `math.SG` papers ready for bundle generation
- 40 sourced from arXiv HTML
- 9 sourced from PDF extraction with `pymupdf4llm`
