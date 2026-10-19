# Prompt 3 CI evidence — 2026-10-19

## Verification
- GitHub Actions run: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39205971349
- Tested commit: `cb7c9decaf1e62bbc46148aba677374220fb5e2e`
- Conclusion: **SUCCESS**, confirmed from GitHub Actions runs and jobs APIs.
- Successful steps: syntax compilation; exact UCS/exhaustive/adversarial unittest suite; independent replay unittest suite; representative matched examples; synthetic benchmark; evidence upload.
- Evidence artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39205971349/artifacts/12164948976
- Artifact SHA256 (GitHub-reported): `c5c17446f0431aa1c015d381c908e2bc5592c4122d8698d986baa0f95d8dce83`.
- Benchmark outputs are stored as downloadable GitHub Actions artifact, not automatically committed into the repository. This manifest does not reproduce or independently inspect every benchmark JSON value.

## Verified interpretation
- The source implements a finite closed grammar with one interchangeable role pool, exact canonical orbit keys, plain/quotient UCS, trace-tree enumeration, independent replay and fail-closed identity-sensitive controls.
- CI success demonstrates that the current test suite passed on the stated commit. It does not prove unrestricted graph-rewriting soundness or external baseline superiority.
- Test parameter grid is n=1..3, target=1..2 where target<=n, capacity=1..3, budget in {0,2,4,7}, creation cost in {0,1,2}, rewire cost in {0,1}, restore cost in {0,2,4}. Total cases by source enumeration: (1+2+2)*3*4*3*2*3 = 1080. The same grammar is compared using exhaustive search, plain UCS and quotient UCS.
- The separate benchmark covers n=1..4 with target up to three and single-run timing/peak tracemalloc measurements. No uncertainty estimate is provided.
- Explicit non-equivariant identity costs and fixed-name guards cause quotient refusal; ordinary UCS remains available.
- The independent replay checker is a separate interpreter, not merely a second call to planner `step`.

## Proof scope
For the declarative grammar, each fresh name in a role pool is treated uniformly by action generation and transitions. Costs, capacity, budget and goal depend only on role-invariant features. The permutation action therefore defines a weighted transition automorphism. Under finite nonnegative-cost assumptions, the orbit quotient preserves minimum goal cost; Dijkstra/UCS over orbit keys returns the minimum cost. A concrete path is retained in each queued representative and independently replayed.

## Remaining blockers
- One pool only; no general identity-sensitive graph rewrite grammar.
- Exact canonicalization factorial; up to eight fresh names.
- No matched GROOVE model or established symmetry-reduction baseline.
- No real-world workload or independently sourced service-network logs.
- Synthetic tests alone do not establish novel algorithmic complexity or new theory.
- Timing data have no repeated-trial uncertainty and memory is Python tracemalloc, not process RSS.
- External bibliography verification and manuscript integration remain open.

## Prompt 4
Perform exhaustive semantic/property testing with independent transition-model oracle, group-action transition-commutation tests for every reachable small state, counterexample minimization, identity-sensitive adversarial cases, budget/capacity constraints, and reproducible CI evidence. If any equivalence fails, stop quotienting and fix the grammar or certificate before proceeding.
