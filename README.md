# review

LLM paper-review board. Three frontier LLMs (Claude, codex, gemini) independently
review each paper across two cycles; a board agent synthesizes the cross-review
into a public summary, strongest claims/objections, reviewer disagreements, and
spot-check suggestions.

Live site: **<https://mihaicosma.com/review/>** — catalog, scatter, drill-down.

---

## Datasets

| Key | Source | Count | Layout |
|---|---|---:|---|
| `gr-qc` | arXiv April 2026, gr-qc category, papers ≤10 pages | 66 | `runs/2026-04/gr-qc/` |
| `bs-meter · sabine` | Papers rated on Sabine Hossenfelder's bullshit-meter video series | 45 | `runs/bullshit-meter/sabine-20260509-164342/` |
| `bs-meter · latest-video` | Latest Sabine bullshit-meter video (separate run) | 1 | `runs/bullshit-meter/latest-video-20260510-225418/review-scored/` |
| `bs-meter · missing-video-318` | Backfill of a Sabine video missed by the main batch (arXiv 2405.06328) | 1 | `runs/bullshit-meter/missing-video-318-20260511-123655/review-scored/` |

The site renders the two bs-meter runs as one category, with Sabine's 0–10
bullshit score (higher = more bullshit) shown alongside the board's 0–10
quality score for direct comparison.

---

## Per-paper layout

Every paper directory under `runs/<run>/papers/<arxiv_id>/` contains:

```
board/claude.json               — board synthesis: public summary, strongest
                                  supported claims, strongest objections,
                                  reviewer disagreements, suggested human
                                  spot-checks, audit trail
review_run_summary.json         — mechanical & selected scores, per-cycle
                                  per-reviewer dimension scores, call status
review_cycles/cycle_01/
  reviews/{claude,codex,gemini}.json   — first-pass independent reviews
review_cycles/cycle_02/
  reviews/{claude,codex,gemini}.json   — cross-review/follow-up after seeing
                                         the cycle-1 reports
metadata.json                   — local metadata
```

Each `teasers.json` at the run root lists every paper with title, selected
score, abstract URL, and general-/technical-reader takeaways — bs-meter rows
also carry `sabine_bullshit_meter_score_10` and related sidecar fields.

---

## Pipeline scripts

| Script | Purpose |
|---|---|
| `scripts/run_review_cycle.py` | Run one reviewer × one cycle. Idempotent — won't overwrite existing JSON. |
| `scripts/retry_review_gaps.py` | Rescan a run's manifest and rerun only papers with missing reviewer JSON, exponential backoff between attempts. |
| `scripts/summarize_review_results.py` | Export the score-sorted `teasers.json` + Markdown from a finished run. `--quiet`, `--sort-by score|manifest`. |
| `scripts/build_bullshit_meter_run.py` | Turn Sabine's video/TSV dataset into a review manifest, keeping her rating as sidecar metadata (not reviewer-visible). |
| `scripts/enrich_bullshit_meter_scores.py` | Backfill resolved Sabine scores onto a completed run's JSON files. |
| `scripts/analyze_bullshit_meter_alignment.py` | Compare board scores vs. Sabine scores across teaser exports; reports the (expected-negative) correlation. |

See [`docs/cli-review-pipeline.md`](docs/cli-review-pipeline.md) for end-to-end
command examples.

---

## Site

`site/index.html`, `site/paper.html`, `site/style.css` — static, no build step.
Loads JSON via `..` for local dev (`python3 -m http.server` from this dir) and
via jsDelivr (`cdn.jsdelivr.net/gh/wakamex/review@main`) when served from
`mihaicosma.com/review/`. Override with `?data=cdn` or `?data=local`.

Deploy with `./deploy.sh` (scp's the three site files to the production VM;
data is served from jsDelivr on every push to `main`).

---

## Excluded from this repo

The `.gitignore` keeps only the artifacts the site reads (~11 MB):

- arXiv source bundles (`runs/**/assets/`, `runs/**/source/`) — copyrighted
- reviewer-call byproducts (`*.prompt.md`, `*.stderr.txt`, `*.stdout.json`,
  `*.usage.json`, `*.command.json`, `*.error.json`, `*.jsonl`, `bundle.md`)
- run-orchestration scratch (`batch_logs/`, `current_batch.json`)
- legacy runs not surfaced on the site (`runs/2026-04/math.SG/`,
  `runs/bullshit-meter/sabine-20260509-164211/`, `runs/retry-gaps-*/`)
