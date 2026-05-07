# arXiv LLM Review Layer

## Core Idea

Build a public review layer on top of arXiv.

Every arXiv paper in a supported topic gets a structured machine review shortly
after posting. Each month, the site publishes a topic-specific selected issue:
the strongest papers, the most interesting contested papers, and notable flaw
flags, all with the review trail attached.

This should not be framed as an LLM journal at first. arXiv remains the
distribution layer. The site is a fast, transparent, contestable critique and
curation layer.

## Why This Is Better Than a Journal Replacement

Journal replacement creates legitimacy and suppression problems. If an LLM board
rejects a good unconventional paper, the system has effectively blocked it.

An arXiv overlay has better failure asymmetry:

- False positives do not suppress publication; the paper remains public.
- False negatives can be corrected later by author response, community feedback,
  human curator review, or later arXiv versions.
- The review artifact is useful even when the monthly selection is wrong.
- Readers can compare the paper, model reviews, author response, and later
  updates in one place.

For the Slotine/Lohmiller-style case, the win is not that a journal is replaced.
The win is that a Madelung/quantum-potential objection could have appeared next
to the arXiv preprint on day one instead of surfacing years later.

## What "Review Errors Are Legible" Means

"Review errors are legible" means a claimed review flaw can be checked by a
qualified reader without needing a hidden dataset, private lab setup, massive
replication effort, or subjective taste call.

Good launch fields have errors like:

- a missing term in a derivation
- misuse of a known theorem
- contradiction with a standard result
- an invalid limiting argument
- a missing baseline in an empirical paper
- benchmark leakage or evaluation mismatch
- a proof step that does not follow from the stated assumptions

Bad launch fields, at least initially, have many errors like:

- wet-lab claims requiring specialized replication
- private clinical or industrial data
- results depending on months of engineering context
- judgments that mostly reduce to field taste

This is why mathematical physics, quantum theory, cryptography, systems/control,
and narrower ML/statistics areas are better early targets than broad biology or
huge all-of-AI ingestion.

## April 2026 arXiv Volume Check

Counts were generated with:

```bash
python3 scripts/count_arxiv_month.py \
  --month 2026-04 \
  --source list \
  --sleep 0.5 \
  --json \
  --output data/arxiv_counts_2026-04.json
```

The script queries arXiv monthly list pages and parses the public
`Total of N entries` count for each configured category. These are arXiv list
entries, not globally deduplicated papers; cross-category overlap is expected.

| Topic | April 2026 Entries | Fit |
|---|---:|---|
| `math-ph` Mathematical Physics | 511 | Best first topic: strong theorem/derivation legibility and manageable volume. |
| `q-bio` Quantitative Biology | 362 | Manageable, but many claims are less legible without domain replication. |
| `cond-mat.stat-mech` Statistical Mechanics | 427 | Good theory-review target, but somewhat narrower audience. |
| `stat.ML` Machine Learning - Statistics | 472 | Good math/empirical surface, but overlaps heavily with `cs.LG`. |
| `cs.CR` Cryptography and Security | 843 | Good proof/attack surface, but security recency matters. |
| `eess.SY` Systems and Control | 904 | Good stability/control fit; less obvious public demo than quantum. |
| `cs.RO` Robotics | 976 | Moderate volume, but empirical claims often need hardware context. |
| `hep-th` High Energy Physics - Theory | 812 | Deep theory surface, but harder to calibrate for non-specialists. |
| `quant-ph` Quantum Physics | 1,696 | Highly relevant to the motivating example, but broad for a first full pass. |
| `cs.CL` Computation and Language | 2,527 | Good benchmark checks, too high-volume for first launch. |
| `cs.CV` Computer Vision | 3,262 | Strong empirical target, too high-volume and gaming-prone initially. |
| `cs.LG` Machine Learning | 3,897 | Useful eventually, too broad for MVP. |
| `cs.AI` Artificial Intelligence | 5,023 | Too broad and noisy for a first topic. |

## Recommended First Topic

Start with `math-ph` for the first full monthly issue.

Reasons:

- It has manageable volume: 511 April 2026 entries, roughly 17 per day.
- Review errors are unusually legible: equations, assumptions, limiting cases,
  known theorems, known correspondences, and derivation checks.
- It is close enough to the motivating Slotine/Lohmiller case to make the demo
  emotionally and intellectually coherent.
- It avoids the initial scale problem of `quant-ph`, `cs.LG`, `cs.CL`, and
  `cs.CV`.
- It lets the site build trust on technical critique before entering noisier
  empirical fields.

Add a parallel watchlist for `quant-ph` papers that make high-risk claims:

- "derive quantum mechanics"
- "classical derivation of quantum"
- "Bell theorem"
- "hidden variable"
- "wavefunction collapse"
- "Madelung"
- "Bohmian"
- "path integral exact"

This captures the public-value demos without requiring the MVP to review all
1,696 `quant-ph` entries in month one.

## Math As A Launch Family

Math is attractive for LLM review, but not because an LLM can certify arbitrary
proofs. It is attractive because many review failures are local and auditable:
missing hypotheses, invalid reductions, misuse of standard theorems, incorrect
examples, notation conflicts, unsupported novelty claims, or contradiction with
known results.

The right review posture is therefore:

- do not claim to verify proofs end-to-end
- flag suspicious proof steps and missing assumptions
- compare claims to known reference results
- ask for counterexamples or edge cases
- extract theorem dependencies and check whether stated hypotheses match usage

Broad `math` is not low-volume. April 2026 had 5,436 arXiv `math` entries.
The low-volume opportunity comes from subcategories.

Math-category counts were generated with:

```bash
python3 scripts/count_arxiv_month.py \
  --month 2026-04 \
  --topic-set math \
  --source list \
  --sleep 0.35 \
  --json \
  --output data/arxiv_math_counts_2026-04.json
```

Saved outputs:

- `data/arxiv_math_counts_2026-04.json`
- `data/arxiv_math_counts_2026-04.md`

Good first math slices:

| Topic | April 2026 Entries | Why It Fits |
|---|---:|---|
| `math.SP` Spectral Theory | 78 | Excellent overlap with quantum, operators, semiclassical analysis, and the motivating paper. |
| `math.OA` Operator Algebras | 90 | Strong quantum/math-physics adjacency and good theorem-review surface. |
| `math.QA` Quantum Algebra | 68 | Physics-adjacent and low volume, though notation-heavy. |
| `math.SG` Symplectic Geometry | 49 | Classical/quantum mechanics adjacency and low volume. |
| `math.LO` Logic | 98 | Formal surface; could pair well with proof-assistant-style checks. |
| `math.CA` Classical Analysis and ODEs | 125 | Good derivation and assumption-check surface. |
| `math.FA` Functional Analysis | 212 | Operator-heavy and relevant, but more volume. |
| `math-ph` Mathematical Physics | 511 | Strong fit, but larger than the narrow slices above. |

One-leaf launch shortlist:

```bash
python3 scripts/count_arxiv_month.py \
  --month 2026-04 \
  --source list \
  --sleep 0.35 \
  --topics math.SP,math.OA,math.SG,cs.LG \
  --json \
  --output data/arxiv_single_leaf_shortlist_2026-04.json
```

Saved outputs:

- `data/arxiv_single_leaf_shortlist_2026-04.json`
- `data/arxiv_single_leaf_shortlist_2026-04.md`

| Topic | April 2026 Entries | Launch Assessment |
|---|---:|---|
| `math.SP` Spectral Theory | 78 | Best if the priority is a quantum/operator-adjacent demo with directly checkable spectral claims. |
| `math.OA` Operator Algebras | 90 | Also strong. Good quantum/noncommutative-geometry overlap, but narrower and more abstract for public demos. |
| `math.SG` Symplectic Geometry | 49 | Best if the priority is the fastest complete end-to-end MVP; lower volume, still physics-adjacent. |
| `cs.LG` Machine Learning | 3,897 | Biggest audience and best eventual business wedge, but far too high-volume for the first one-leaf implementation. |

If starting with exactly one official arXiv leaf, the choice is now:

- choose `math.SG` if the priority is fastest complete MVP
- choose `math.SP` if the priority is the strongest public demo near
  quantum/operator/spectral claims

On balance, `math.SG` is probably the better first engineering target, while
`math.SP` is the better first public demo target.

Rough workload proxies:

```bash
python3 scripts/compare_arxiv_leaf_workload.py \
  --month 2026-04 \
  --topics math.SP,math.OA,math.SG,cs.LG \
  --sleep 0.35 \
  --json \
  --output data/arxiv_leaf_workload_2026-04.json
```

Saved outputs:

- `data/arxiv_leaf_workload_2026-04.json`
- `data/arxiv_leaf_workload_2026-04.md`

| Topic | Entries | HTML Available | Median Reported Pages | P90 Reported Pages |
|---|---:|---:|---:|---:|
| `math.SP` | 78 | 92.3% | 25 | 58 |
| `math.OA` | 90 | 93.3% | 29 | 59.5 |
| `math.SG` | 49 | 81.6% | 36 | 67 |
| `cs.LG` | 3,897 | 89.9% | 16 | 39 |

This means `math.SG` is faster overall because there are fewer papers. It is
not obviously faster per paper: reported SG papers are longer on median, and
fewer have arXiv HTML available.

Original argument for `math.SP` Spectral Theory:

Why:

- 78 April 2026 entries is small enough to review thoroughly.
- The category naturally includes Schrodinger operators, operators on
  manifolds, differential operators, resonances, and random matrices.
- Review flaws are relatively legible: missing hypotheses, spectral-domain
  assumptions, invalid operator identities, mistaken limiting arguments, and
  contradiction with known spectral results.
- It is adjacent to quantum mechanics and mathematical physics without
  inheriting all of `quant-ph`'s volume.
- It can produce a credible first demo before expanding to `math.OA`,
  `math.SG`, or selected `math-ph` cross-lists.

Why not the others first:

- `math.OA`: strong second category, but more abstract and harder for outsiders
  to evaluate from the review artifact.
- `math.SG`: elegant and low-volume, but a monthly issue with 49 entries may
  feel too sparse unless the audience is already very targeted.
- `cs.LG`: strategically important later, but 3,897 April 2026 entries means
  the first launch would become an operations and ranking problem instead of a
  review-quality demo.

Multi-leaf launch wedge, if expanding after the one-leaf demo:

Start with a "Mathematical Physics and Operators" issue that includes:

- `math.SP`
- `math.OA`
- `math.QA`
- `math.SG`
- selected `math-ph` papers routed by cross-list or inferred tags

This is small enough to review thoroughly, close to the original scientific
process demo, and more coherent than all of `math-ph` or all of `math`.

## Category And Subcategory Strategy

Use three layers of topic metadata.

Layer 1: official arXiv category.

arXiv exposes a primary category and all category terms in its Atom metadata.
For example, an API record can include:

- `arxiv:primary_category term="quant-ph"`
- `category term="quant-ph"`
- `category term="math-ph"`
- `category term="math.DG"`
- `category term="math.OA"`

This layer is stable enough to use for routing, counting, and public topic
pages.

Layer 2: official cross-lists.

Cross-lists are the best first proxy for subcategory-like routing. A paper with
primary `quant-ph` and cross-list `math-ph` should likely get a different rubric
than primary `quant-ph` plus cross-list `cs.LG` or `cond-mat.stat-mech`.

Layer 3: inferred review tags.

For finer buckets like "quantum foundations", "semiclassical analysis",
"Bell/EPR", "RL theory", or "benchmark paper", arXiv does not provide a
uniform official taxonomy. These should be inferred tags produced by a classifier
or LLM and treated as soft metadata, not authoritative routing labels.

The rule:

- official arXiv categories decide inclusion and counting
- cross-lists choose the initial rubric variant
- inferred tags improve search, watchlists, and digest sections
- inferred tags should not be the only reason a paper is excluded from review

This matters because many interesting categories are already leaves in arXiv's
taxonomy. `quant-ph`, `math-ph`, and `hep-th` do not have official nested
subcategories underneath them. By contrast, broad archives such as `physics`,
`cs`, `math`, `stat`, `q-bio`, and `cond-mat` contain dotted categories like
`cs.LG`, `math.DG`, `q-bio.NC`, or `cond-mat.stat-mech`.

## Product Shape

Daily paper pages should include:

- arXiv metadata, abstract, authors, versions, links
- extracted claims
- three independent model reviews
- cross-review between models
- synthesized board report
- verdict and confidence
- topic tags
- author response
- correction history

Monthly issues should include:

- selected papers
- contested but important papers
- likely flawed papers worth noting
- strongest datasets/tools/methods, where relevant
- updates on papers whose verdict changed after author response or new versions

Use "selected" or "board-selected" rather than "accepted" at first. It avoids
journal cosplay and makes the advisory nature of the layer clearer.

## Review Pipeline

1. Ingest arXiv metadata, PDF, and source when available.
2. Parse text, references, equations, sections, and figures.
3. Assign topic and review rubric.
4. Run three independent model reviews.
5. Run cross-review, where each model critiques the other reviews.
6. Synthesize a public board report.
7. Route disagreement, high-impact claims, and author appeals to human spot
   checks.
8. Regenerate reviews when a new arXiv version appears.

The public report should distinguish:

- claims the paper clearly supports
- claims that are plausible but under-supported
- central objections
- weak or speculative objections
- missing references or baselines
- confidence and scope limits

## Verdicts

Suggested initial verdicts:

- `Strong Select`: likely important and technically solid
- `Promising`: worth reading, with caveats
- `Contested`: potentially important, board uncertain or split
- `Weak Evidence`: interesting claim, inadequate support
- `Major Flaw Flag`: likely central technical error
- `Routine`: competent but incremental

The verdict should never be the only artifact. The reasoning matters more than
the label.

## Trust And Safety

Credibility depends on making the review process auditable.

Minimum trust features:

- public review reports
- model names, dates, and review run IDs
- versioned prompts internally
- author right of reply
- correction mechanism
- visible uncertainty
- regenerated reports for new arXiv versions
- no personal judgments about authors

Anti-gaming requirements:

- strip or quarantine prompt-injection text from PDFs
- never let paper text control system prompts
- randomize some private rubric checks
- require serious objections to cite paper locations or known results
- track papers where the board appears uncertain or overly consensus-biased

## MVP

Phase 1:

- Support `math-ph`.
- Ingest one month of arXiv papers.
- Produce paper pages with three independent reviews and one synthesized report.
- Publish one monthly selected issue.
- Allow author responses by email or simple authenticated form.

Phase 2:

- Add `quant-ph` high-risk-claim watchlist.
- Add search by review attributes: "major flaw flag", "missing baseline",
  "contradicts known theorem", "contested".
- Track version-to-version verdict changes.

Phase 3:

- Add `stat.ML` or `eess.SY`.
- Add calibration dashboards.
- Add curator queues for high-disagreement papers.

CLI orchestration details are in `docs/cli-review-pipeline.md`. The short
version: deterministic Python scripts own crawling, parsing, state, validation,
and publishing; local model CLIs such as `claude -p`, `codex exec --json`, and
`gemini -p` run bounded stateless review passes and write JSON artifacts.

## Success Metrics

The site is working if:

- authors respond substantively to reviews
- readers use board reports as reading filters
- flaw flags are later validated by human comments, errata, or rebuttals
- selected papers age better than non-selected papers in the same topic
- the site corrects itself publicly when reviews are wrong

The long-term infrastructure value is not just ranking papers. It is producing
a structured, searchable, public critique trail for the scientific literature.
