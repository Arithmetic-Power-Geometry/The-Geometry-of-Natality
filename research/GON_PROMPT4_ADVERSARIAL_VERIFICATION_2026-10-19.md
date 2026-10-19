# Prompt 4 — adversarial semantic verification report
Date: 2026-10-19
Status: **PASS for bounded closed grammar; no general-grammar certification**

## GitHub evidence
- Tested SHA: `9547d0948daa2f151b82d38d0bfc8cf993962618`
- Workflow: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39206246637
- GitHub jobs API: completed SUCCESS. Syntax, independent semantic unittest, JSON generation, and artifact upload succeeded.
- Artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39206246637/artifacts/12165563397
- GitHub-reported artifact digest: `sha256:fcfd258ff8d8aee3ab9962bfe4871935b23805815b2096b03d8d82b1989c0a37`.
- The artifact contains machine-readable case details; individual numeric counts have not been independently extracted into this report.

## Audit construction
The independent interpreter in `experiments/research_gate/semantic_audit.py` builds full reachable graphs using its own action generator and state updates. It compares each state’s exact weighted successor set to the planner. For each reachable state and each role-preserving permutation it checks:
1. renamed state belongs to the independently generated reachable graph;
2. exact canonical key remains equal;
3. weighted successor transitions commute with renaming;
4. goal truth is invariant.
Finally it compares ordinary and quotient UCS optimal costs.

CI covers n=1,2,3 with capacities 0..n, plus zero-cost and unreachable variants. The tests exercise name-sensitive cost, fixed-name preference and opaque-guard refusal. This is exhaustive over reachable states for **each chosen small grammar**, not exhaustive over all possible grammars.

## Counterexample ledger
**CE-01: identity-specific creation cost.** Two exchangeable-looking names a,b with creation costs 0 and 2. The post-create graph states are orbit-equivalent under name permutation, but the weighted transitions are not cost-preserving. Quotienting is therefore invalid unless cost semantics and the group are restricted. Current `search(...,quotient=True)` refuses `identity_costs`, preventing this unsound merge. This is an explicit negative-control witness, not a newly discovered failure of the supported implementation.

No failing counterexample within the tested certified grammar was observed by CI. Do not infer absence of counterexamples outside this finite scope.

## Proof-obligation matrix
| Obligation | Status |
|---|---|
| Exact finite orbit key iff permitted permutation | Mathematical group argument plus Prompt 2 exhaustive tests |
| Complete weighted successor commutation for bounded reachable states | Independent executable exhaustive tests PASSED |
| Goal invariance for bounded reachable states | Independent executable tests PASSED |
| Plain/quotient UCS agreement in tested grammars | Executable tests PASSED |
| Concrete plan applicability and claimed cost | Independent replay tests PASSED (Prompt 3) |
| General arbitrary graph rewrite equivariance | NOT established |
| Arbitrary history-dependent prerequisites | NOT supported by current grammar |
| Multiple interacting role pools | NOT supported by current planner |
| Negative conditions beyond create/rewire applicability | NOT supported |
| General complexity improvement | NOT established |
| Independent established symmetry tool comparison | NOT performed |
| Publication-level originality | NOT established |

## Remaining risks and repair policy
The tests found no supported-grammar semantic mismatch requiring a code repair. The counterexample is handled by refusing non-equivariant policies. A future grammar extension must add new proof obligations and independent tests before permitting quotient search. The existing trusted certificate flags are **not** a universal automatic verifier.

## Prompt 5
Implement an executable conservative read/write footprint checker for the closed action grammar and define independence precisely. Verify decomposition against full-state UCS, including shared capacity, history-sensitive guards, negative application conditions and cross-service edges. Refuse uncertified decomposition and preserve minimized counterexamples. Do not assert general separability from merely disjoint names.
