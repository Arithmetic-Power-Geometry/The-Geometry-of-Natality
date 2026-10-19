# Prompt 8 — verified GitHub CI evidence
Date: 2026-10-19

## Verified source and run
- Tested code commit: `2228673b1d3aa0de57306eb400e712e192958526`.
- GitHub Actions: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39207537034
- Jobs API: completed SUCCESS. Compilation, matched smoke tests, full 20-repetition benchmark, result assertions and artifact upload all succeeded.
- Raw results: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39207537034/artifacts/12165749720
- Artifact SHA256 (GitHub ZIP digest): `94c9c582933ab68b5031bd2e1a5501273d64b0a2c7fda8c5394a1b17e285ac8c`.
- CI asserts **36 matched cells**, **36 correct refusal cells**, **1,440 measured trials**, and **20 paired repetitions** for every matched comparison.
- Each matched cell's algorithms are checked against independent exhaustive optimum and returned plan replay before timing; each measured trial's returned cost is checked against the same optimum.
- Full numeric results and paired bootstrap summaries are in the artifact, **not separately re-extracted or independently recomputed** in this report.

## Cautions
- No per-trial 60-second hard timeout or 2 GiB memory enforcement; 35-minute job cap only.
- Timing is CI-host-dependent and `tracemalloc` is not process RSS.
- No external GROOVE matched baseline, real-world dataset or novel theorem.
- Graph-coupled and opaque-guard cases are refusal-only; their partial interpreter costs must never be used as coupled/guarded optimization results.
- No plots were generated in this stage.
- The benchmark generator and frozen manifest have not been modified.
- GitHub success demonstrates that the programmed assertions passed, not that a publication-level superiority claim is justified.

## Next gate
Prompt 9: independently retrieve and reanalyze the raw artifact, add per-trial resource enforcement, re-run with explicit censored outcomes, produce reproducible plots and carefully scoped manuscript tables.
