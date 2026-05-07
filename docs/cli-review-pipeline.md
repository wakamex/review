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
     --bare \
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
  "confidence": 0.0
}
```

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

## First Implementation Slice

For `math.SG`, implement:

1. `build_manifest.py`: produce `manifest.jsonl` for one month.
2. `fetch_paper.py`: download HTML/source/PDF into `runs/.../source`.
3. `build_bundle.py`: create `bundle.md`.
4. `run_review.py`: run one provider adapter against one bundle.
5. `run_board.py`: run cross-review and synthesis.
6. `render_static.py`: write a paper page and monthly issue.

This keeps the system boring in the best way: scripts in, artifacts out.
