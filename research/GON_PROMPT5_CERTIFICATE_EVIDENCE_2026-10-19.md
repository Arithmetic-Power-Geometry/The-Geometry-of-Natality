# Prompt 5 — conservative independence certificate and decomposition verification
Date: 2026-10-19
Status: **PASS for closed multi-component DSL, not arbitrary repair systems**

## Verified CI
- Successful run: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39206483392
- Tested commit: `34791e9bdd9dbac7e529e0ed05930b6d86be6102`
- All steps succeeded: compilation, exhaustive unit-test suite, benchmark JSON generation, evidence upload.
- Evidence artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39206483392/artifacts/12166340242
- GitHub artifact digest: `sha256:25129dc8221f9915c429ce34df44451c42993160dcfaa1522279a8df04949760`.
- No claims of externally benchmarked speedup; timing data are exploratory.

## Semantics and proof scope
The new `experiments/research_gate/footprint_certificate.py` defines a *separate* closed multi-component repair DSL. Each component has local stage, local history, local identity allocation, and three possible actions (restart, create, rewire) with heterogeneous nonnegative integer costs. A global budget is an external bound on the sum of costs. Global restart capacity, cross edges, global history guards, global negative conditions, shared allocation and opaque guards are explicitly modeled as uncertifiable coupling.

The checker derives action read/write/guard/allocation footprints from operation type and declared problem semantics. It refuses known cross-component conflicts and all opaque semantics. Local history prerequisites and local negative guards remain within component footprints. A successful certificate means the finite global transition system is the asynchronous product of local systems, with additive cost and conjunctive goal. Therefore its unbounded minimum cost is the sum of local minima; under a nonnegative additive global budget B, a feasible goal exists iff the sum is <=B. Concatenating local optimal plans is valid because all cross-component operations commute and have no shared guards/resources. This is a standard product/separability argument, not new foundational theory.

## Independent verification
- 288 deterministic combinations: n=1,2,3; heterogeneous restart costs; create/rewire costs; four budgets; restart prohibition.
- For all combinations, decomposed result is compared with full-state UCS; for n<=2, also with independent full trace-tree enumeration.
- Explicit zero-cost actions, local history requirement, unreachable goals and external budget tests.
- Conservative rejection tests: global restart capacity, cross-service edges, global history guard, shared allocation, opaque guard, global negative condition.
- Benchmark script reports synthetic n=1..4 costs, full UCS expansions and certificate overhead; single-run timings do not support performance generalization.

## Counterexample CE-02: strict optimal-cost gap
Two components, each restart cost 1, create cost 2, rewire cost 1. Unconstrained independent minimum = 2 by restart/restart. A global restart capacity of one invalidates that plan. Globally feasible optimum = 4 by one restart plus one create/rewire. The certificate refuses the shared-capacity instance, preventing an incorrect decomposition. This improves on the prior example in which the combined plan was infeasible but the optimum did not change.

## Limitations / unresolved
1. Footprints are generated from the *closed* DSL; arbitrary graph rewrite syntax is unsupported.
2. Cross-component edge constraints are refused, not analyzed for more permissive decompositions.
3. Shared budget is handled as external feasibility bound, not as a stateful consumable resource.
4. General history-sensitive and negative-condition semantics beyond the local DSL are not supported.
5. Decomposition is standard separability; no GoN-specific novel complexity result has been established.
6. No matched GROOVE baseline, production dependency traces or publication-grade runtime statistics.
7. The manuscript's Proposition 5 must be rewritten with these explicit restrictions before claiming implementation.

## Prompt 6 research gate
Investigate genuinely new structural results for creation-enabled repair that cannot be reduced to standard product separability or group symmetry. Formulate falsifiable conjectures, independently search small counterexamples, prove surviving statements, position against known work and give algorithmic consequences. Preserve failed conjectures and distinguish original theorem from restatement. No forced novelty or fabricated proof.
