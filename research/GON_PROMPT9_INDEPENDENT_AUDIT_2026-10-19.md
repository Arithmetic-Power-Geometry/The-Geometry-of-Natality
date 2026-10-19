# GoN Prompt 9 — Independent Statistical Audit and Resource Enforcement
Date: 2026-10-19

## Original Prompt 8 artifact independently recovered
- Original CI run: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39207537034
- Artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39207537034/artifacts/12165749720
- Independently downloaded ZIP SHA-256: `94c9c582933ab68b5031bd2e1a5501273d64b0a2c7fda8c5394a1b17e285ac8c`, matching GitHub metadata.
- Parsed raw JSON: exactly 36 matched cells, 36 negative controls, 1,440 successful measured trials; all 1,440 (instance,algorithm,repetition) keys unique.
- Frozen manifest SHA-256 from JSON: `6684f407eb332d9ed4a87799177c286c04636fdd85445b350adea675ca567e84`.
- Independently recomputed all 36 median paired differences from raw trial rows. Maximum discrepancy with the stored median paired differences: **0 seconds**.

## Descriptive results (Prompt 8 original, not isolated rerun)
Median across nine instance-level median paired wall-time differences, sign = first algorithm minus second:
| Matched stratum | Median difference | Interpretation |
|---|---:|---|
| fresh_symmetric: plain UCS minus quotient UCS | -3.442 ms | quotient UCS slower on these small synthetic cases |
| independent: full UCS minus decomposition | +0.344 ms | small descriptive decomposition advantage |
| history_local: full UCS minus decomposition | +0.359 ms | small descriptive decomposition advantage |
| negative_local: full UCS minus decomposition | +0.193 ms | small descriptive decomposition advantage |

The results are **not** a general speedup claim. Quotient's factorial orbit-key calculation can dominate at small sizes. These are exploratory CI-host measurements; the benchmark strata are small and synthetic, and all three seeds at a size share structural topology.

## Resource-limited rerun
- `experiments/research_gate/benchmark_trial_worker.py` isolates a single trial.
- `experiments/research_gate/benchmark_runner_isolated.py` invokes each trial as a separate Linux subprocess, imposes a 60-second `subprocess.run(timeout=60)` bound and 2 GiB `RLIMIT_AS` virtual address-space cap, records exit codes, timeouts and errors without dropping measured failures.
- The cap is **virtual address space**, not RSS, and a Python MemoryError or nonzero exit code is not automatically proof of hitting the cap. Wall-clock timing is measured inside each isolated process, while process launch overhead is separately recorded.
- The worker uses the **unchanged** frozen benchmark generator and the existing matching semantics. A full 20-repetition rerun is managed by `.github/workflows/gon-prompt9-independent-audit.yml`.
- `experiments/research_gate/independent_benchmark_audit.py` independently recomputes paired medians, IQRs and bootstrap intervals without importing the runner's statistics function, validates unique trial keys, costs, completeness, and generates dependency-free SVG summary figures.
- Original and rerun audit artifacts must be examined before making stronger numerical claims.

## Manuscript-ready Results (restricted)
“Across nine frozen synthetic fresh-name symmetry instances, quotient uniform-cost search preserved the independently checked optimal repair cost but incurred greater measured wall time than ordinary UCS. The median of instance-level median paired differences (plain minus quotient) was -3.442 ms in the initial CI-host experiment. Across three separate nine-instance local-repair strata, certified decomposition preserved optimal costs and showed small positive median paired differences relative to full-state UCS (+0.193 to +0.359 ms). These timings are descriptive for the finite synthetic benchmark and do not demonstrate general algorithmic superiority or real-world generalizability.”

## Limitations
The benchmark contains no independently sourced operational dependency networks, no matched GROOVE comparison, no verified general coupled-graph semantics, no large-scale evaluation, and no new foundational GoN theorem. Per-trial memory enforcement uses address-space limits rather than measured peak RSS. Bootstrap resampling of 20 repeated timings does not represent uncertainty over unseen network topologies. Figures are generated from JSON artifacts and must not be described as pre-existing evidence.

## Prompt 10 readiness
Conduct a claim-to-evidence audit of the manuscript. Revise propositions to exactly match proved finite-grammar assumptions, replace unsupported empirical statements with validated Prompt 9 numbers, inspect references and citation accuracy, and independently verify a fully reproducible submission package. Do not claim Q1 readiness until novelty and external validity are independently assessed.
