# GoN Prompt 7 — Frozen Benchmark Protocol v1.0.0
Date: 2026-10-19. Status: **protocol frozen; main comparative experiments NOT executed**.

## Questions and falsifiable hypotheses
RQ1: Under certified name symmetry, does quotient UCS preserve exact optimal cost and replayability on the same single-pool grammar as plain UCS? H1: yes; any discrepancy is a correctness failure.
RQ2: On certified independent multi-component grammars, does decomposition preserve the exact optimum and replayability relative to full UCS? H2: yes; any discrepancy is a correctness failure.
RQ3: How do expansion counts, generated successors, wall time, Python-traced memory and certification/canonicalization overhead change as size grows? H3: improvement is NOT presumed; report negative results.
RQ4: How often are unsafe symmetry or decomposition requests rejected? H4: all declared unsupported semantics must refuse, not silently return an optimum.

## Frozen synthetic design
Source: `experiments/research_gate/benchmark_v1.py`. Eight strata: independent, shared_restart, graph_coupled, fresh_symmetric, identity_cost, history_local, negative_local, opaque_guard. Three fixed seeds: 17,29,43. Sizes: 2,3,4. Total **72** synthetic manifest cells, with canonical SHA-256 over each complete instance record, a separate topology-only hash, and a top-level manifest hash. Stable sorted-key JSON and explicit generator version `gon-benchmark-v1.0.0`.

These are generated **synthetic scenarios**, not measured real service failures. Topology is a directed metadata representation. In the current multi-component solver, `cross_edges` is a conservative refusal flag; **the edges are not executed as graph dependencies by the full UCS interpreter**. Consequently, the graph-coupled stratum is valid for rejection tests only, NOT for claims about optimal repair costs on coupled graphs. Likewise, `opaque_guard` is not enforced by the plain UCS interpreter and is refusal-only; its apparent plain-UCS output is NOT a valid guarded-problem baseline.

## Baseline compatibility (frozen)
| Stratum | Plain UCS | Quotient UCS | Decomposition | GROOVE |
|---|---|---|---|---|
| fresh_symmetric | same single-pool grammar | supported | incompatible model | unverified |
| identity_cost | same single-pool grammar | MUST refuse | incompatible model | unverified |
| independent | same multi-component grammar | incompatible model | supported | unverified |
| history_local | same multi-component grammar | incompatible model | supported | unverified |
| negative_local | same multi-component grammar | incompatible model | supported | unverified |
| shared_restart | partial multi-component semantics | incompatible model | MUST refuse | unverified |
| graph_coupled | only partial semantics, NOT cost baseline | incompatible model | MUST refuse | unverified |
| opaque_guard | guard not executed, NOT cost baseline | MUST refuse | MUST refuse | unverified |

**Never compare plain UCS of one grammar to quotient UCS or decomposition of a different grammar.** Do not call GROOVE smoke tests a matched baseline. No external symmetry baseline has yet been implemented.

## Verification and execution protocol for Prompt 8
1. Recompute frozen JSON and verify all hashes; any generator or semantics change creates a new version and a new manifest, never silent edits.
2. Run supported matched algorithms on the identical frozen instance, with identical cost conventions, budgets and goals. Refusal-only strata check rejection; do not report their partial interpreter's costs as true coupled costs.
3. For small instances use independent exhaustive oracle and replay; record optimal cost, reachability, plan hash and all mismatches. If an oracle times out, label result uncertified.
4. For timing use at least 20 repetitions per supported instance per algorithm, warmup 3, paired randomized execution order with recorded deterministic seeds. Report median, interquartile range, bootstrap 95% interval for paired differences, and raw per-trial observations. Bootstrap seed fixed and recorded.
5. Record Python version, OS, CPU, memory, source commit, UTC time, seed, topology hash, complete-instance hash, process exit code and exception. Record wall-clock, expansions, generated states, distinct states, canonicalization calls/time, certificate overhead, peak traced Python allocation; explicitly distinguish tracemalloc from process RSS.
6. Pre-register timeout 60 seconds per trial and memory cap 2 GiB; report censored cases and coverage, never drop failures from aggregate. For n>4 or larger strata, add versioned extension rather than silently changing v1.
7. Main inferential comparisons are within identical grammar only. Use paired differences and uncertainty; avoid pseudo-replication across seeds that share topology and cost generation. Treat multiplicity and exploratory claims explicitly.
8. Keep counterexamples and all negative results; require independent semantic equivalence before any GROOVE matched comparison.
9. Do not infer practical significance from expansions alone, or claim Q1 novelty from a faster implementation of known symmetry reduction.

## Integrity gates
`tests/test_benchmark_v1.py` checks exact regeneration, tamper detection, seed/stratum coverage, topology digests, negative baseline compatibility. CI uploads a full frozen JSON manifest as an artifact. The manifest artifact is the evidence for instance identity; code and documentation define protocol.

## Blockers and next stage
No real-world operational network has been sourced or validated. No matched GROOVE grammar, no comparable general graph-coupled solver, no publication-grade performance statistics, no novel theorem (Prompt 6 failed originality gate). Prompt 8 should implement a strict benchmark runner and analyze only supported matched comparisons. If the semantics are not matched, record `not_comparable` rather than a numeric performance ratio.
