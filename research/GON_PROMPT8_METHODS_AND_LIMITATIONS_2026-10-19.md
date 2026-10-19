# Prompt 8 — matched frozen benchmark interpretation and integrity gates
Date: 2026-10-19
Status: execution workflow submitted; CI result must be checked separately.

## Scope
Frozen generator `benchmark_v1.py` is unchanged. `benchmark_runner_v1.py` verifies the 72-cell manifest, executes 36 semantically matched cells (9 fresh_symmetric and 27 multi-component independent/history_local/negative_local) and 36 refusal-only cells. It runs three warmups and 20 paired measured repetitions per matched cell and algorithm, for **1,440 raw measured algorithm trials**. Every matched instance has independent exhaustive optimal-cost validation and plan replay; all 36 negative controls require refusal. Comparison pairs are *within identical instances and model grammars*.

## Measurements
Raw trials contain algorithm name, repetition, execution order, cost, plan hash, expansions, generated successors, distinct keys, canonicalization calls and time (when applicable), certificate time (when applicable), wall seconds and Python tracemalloc peak bytes. Each instance comparison reports median paired wall-time difference, IQR and fixed-seed 1,000-resample percentile bootstrap 95% interval for median paired difference. Metadata include GitHub commit, UTC time, Python version, OS, CPU description, seed, topology and instance hashes.

## Prespecified exclusions
The 36 refusal cells are not cost-performance observations. In particular, graph coupling and opaque guards are *not* enforced by existing plain UCS interpreters. GROOVE is not a matched baseline. No real-world logs are represented. Do not claim these results prove superiority or a novel GoN theorem.

## Protocol deviations / limitations to disclose
- Runner currently records elapsed time but does not enforce a 60-second per-trial wall timeout or a 2 GiB hard memory cap. The CI job has a 35-minute aggregate timeout. Consequently, the run is a preliminary matched experiment and **does not fully satisfy Prompt 7's preregistered resource-censoring protocol**.
- It uses Python `tracemalloc` peak allocation, not resident-set memory. 
- Each pair is run on a shared CI host; execution order is deterministically randomized but environmental interference is not controlled.
- Bootstrap intervals quantify resampling of within-instance trials only, not generalization to new graph topologies or operational workloads.
- Timing and summary JSON are CI artifacts, not committed static results.
- No plot/figure generated yet; figures can be produced from the complete JSON after successful CI.
- Missing or failed CI is not a successful experimental result.

## Decision rule
Only if CI reports success and uploads valid 1,440-row raw JSON may the matched experimental correctness gate be considered passed. Publication-grade comparative performance remains conditional on resource-limit enforcement, external baseline and broader independent workloads. Originality remains unresolved.

## Prompt 9
Perform independent results audit: retrieve and inspect the Prompt 8 raw JSON; recompute statistics from scratch; verify pairing, hashes, run completeness, anomalies and all failures. Implement enforceable per-trial time/memory limits with explicit censoring and repeat the frozen benchmark without altering the generator. Produce figures with uncertainty and manuscript-ready results that avoid unsupported external validity or novelty claims. Assess whether any result warrants a publication-level contribution, and do not force a positive conclusion.
