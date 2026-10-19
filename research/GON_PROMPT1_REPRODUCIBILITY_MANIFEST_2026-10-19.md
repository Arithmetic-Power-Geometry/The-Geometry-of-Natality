# GoN Prompt 1 — reproducibility manifest and claim/evidence audit
Date: 2026-10-19
Status: RESEARCH AUDIT; NOT Q1-READY; NO NEW EXPERIMENTS CLAIMED

## Immutable baseline
- Repository: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality
- Audited default-branch tree SHA: `f5a2cc3de82b2a55d95fcaa2e046b33c10ba2147`
- Audited main commit SHA: `f5a2cc3de82b2a55d95fcaa2e046b33c10ba2147`
- Working branch: `research/gon-stage1-20261019`
- Prior stage-1 audit commit: `d178926e0ab8c08accb9832f89b5913b368af010`
- Source manuscript: user-provided 14-page PDF, 6 propositions, 4 algorithms, 4 figures, 8 tables, 23 cited references. Manuscript PDF and uploaded ZIP are NOT stored on the audited main branch.
- Evidence classification: `CI observed` = GitHub Actions job metadata inspected; `source inspected` = repository text read; `not rerun` = no new execution in this audit.

## Claim-to-evidence ledger
| Claim | Source | Status / limitation |
|---|---|---|
| Fixture has two cost-3 optimal plans | `applications/workflow_repair/fixture.json`, `compare_independent_oracles.py`, `optimality_certificate.py` | CI observed success; 16 ordered subsets, four feasible, two goal-reaching; synthetic only |
| 12 scaling executions | `scaling_benchmark.py` | CI observed success; n=1..4 x three action-order seeds, not 12 independent graph topologies |
| Enumeration visits 314217 versus UCS expansions 399 at n=4 | `scaling_benchmark.py`, manuscript Table 6 | Different work metrics, not a fair speedup ratio |
| 24 decomposition cases | `decomposition_research.py` | CI observed success; n=1..8 x 3 seeds; full UCS check only n<=4 |
| Shared restart-capacity counterexample | `decomposition_research.py` | Demonstrates invalid concatenated plan, not necessarily higher optimum cost |
| Fresh-name orbit quotient optimality | manuscript Proposition 6 | Standard symmetry projection/lifting under full equivariance; proof needs explicit action/history group action; no novel-priority clearance |
| Orbit UCS algorithm | manuscript Algorithm 4; `experiments/research_gate/fresh_name_quotient_prototype.py` | PROTOTYPE EXISTS; not a general exact canonical key, no matched benchmark; action labels/history fixed while vertices renamed |
| Automatic footprint certificate | manuscript Proposition 5; `decomposition_research.py` | NOT IMPLEMENTED: current guard rejects declared coupling/global resource, no extracted conservative R/W footprints |
| GROOVE execution | `.github/workflows/gon-groove-smoke.yml`, `GON_VERIFIED_CI_EXECUTION_EVIDENCE_2026-10-18.md` | Official GROOVE smoke test reported success; NOT matched GoN grammar/cost benchmark; some later smoke workflow runs failed |
| Real-world application | manuscript discussion; repository | NOT VERIFIED: only synthetic fixture evidence |
| Bibliography accuracy | `references.bib`, `research/GON_BIB_AUDIT_2026-10-18.json` | Metadata not independently verified here; historical audit covers a different 10-entry snapshot, whereas manuscript cites 23 references |

## CI evidence
- Exact-oracle regression run 39151100642: completed SUCCESS, commit `a04e6fa7d2b952edad903c22867d5f2a23eabbaa`. Jobs API shows success for oracle comparison, exhaustive certificate, scaling and decomposition.
- GROOVE smoke run 39145685509 is reported successful in repository evidence document; this audit did not reexecute GROOVE.
- Later GROOVE smoke runs 39150121889, 39150129935 and 39150232113 show FAILURE in GitHub run listing. Investigate logs and pin release/sample versions; do not claim a stable validated baseline.
- `.github/workflows/gon-oracle-regression.yml` only triggers on changes under `applications/workflow_repair/**` or the workflow itself. It does not test changes to `experiments/research_gate/fresh_name_quotient_prototype.py`.
- `.github/workflows/gon-research-integrity.yml` checks bibliography structure and a counterexample; not orbit UCS.
- No new CI run was triggered by this documentation-only commit.

## Implementation blockers (priority order)
1. **P0: Canonical key soundness.** `fresh_name_quotient_prototype.py` permutes allocated vertex names but retains used-action history unchanged; actions are fixed labels. This cannot establish full equivariance or orbit iff-equivalence for general creation actions. Define the group action on actions, histories, negative conditions, allocations, constraints, costs and goals before quotienting.
2. **P0: Source syntax check.** The fetched prototype includes the literal text `==2\\n    assert` in a line; inspect actual bytes and run `python -m py_compile` before using it.
3. **P0: Exact canonicalization.** Implement `K(s)=K(t) iff s,t` lie in the same permitted orbit. Exhaustive permutation oracle for <=8 fresh identities; explicit error/limit for larger cases; type/role-preserving group only.
4. **P0: Concrete plan replay.** Verify quotient UCS's returned concrete actions replay from original state to goal at the reported cost; handle representatives and predecessor traces.
5. **P1: Baselines.** Plain UCS, orbit UCS, and an established symmetry method on identical instances and identical metrics (expansions, generated states, wall time, memory, canonicalization overhead).
6. **P1: Robustness.** Identity-sensitive negative controls, heterogeneous costs, negative application conditions, role constraints, shared capacity, graph coupling, zero-cost actions.
7. **P1: Footprint checker.** No automatic conservative read/write extractor currently; keep certificate theoretical until implemented.
8. **P1: Independent baseline.** Implement matched GROOVE repair grammar or document verified impossibility; smoke-test is insufficient.
9. **P1: Application.** Realistic dependency topology and externally grounded failure scenario, explicitly distinguish synthetic case studies from real logs.
10. **P2: Manuscript.** Correct abstract creation-free terminology, integrate contribution four, formalize budget and plan reconstruction; do not add unmeasured claims.

## Minimal independent reproduction commands (not run during this audit)
```bash
git checkout f5a2cc3de82b2a55d95fcaa2e046b33c10ba2147
python --version
python -m py_compile experiments/research_gate/fresh_name_quotient_prototype.py
python applications/workflow_repair/compare_independent_oracles.py
python applications/workflow_repair/optimality_certificate.py
python applications/workflow_repair/scaling_benchmark.py --max-n 4
python applications/workflow_repair/decomposition_research.py
python experiments/research_gate/symmetry_gate.py
python research/check_bib_integrity.py
```
Record OS, Python version, git SHA, UTC timestamp, stdout/stderr, exit codes, SHA256 of outputs and runtime/memory. Do not overwrite frozen evidence without preserving a copy.

## Prompt 2 acceptance gates
- Fix any syntax errors and create tested exact canonicalization.
- Specify finite group of permitted role-preserving fresh-name permutations and its action on graph, action history and all identity-bearing attributes.
- Prove or mechanically check orbit equivalence (reflexive/symmetric/transitive) and canonical key iff orbit on bounded fixtures.
- Reject or avoid quotienting whenever equivariance cannot be established; test negative controls.
- Commit code, tests, JSON evidence, documentation and CI workflow to the research branch; provide commit SHA.
- Do NOT infer Q1 novelty, speedup, or real-world applicability from these gates alone.

## Important interpretive distinction
The repository README and RESEARCH_RESET explicitly reject Q1 novelty and propose an alternative AGI-LR research question. The present 14-page manuscript instead develops cost-optimal repair and nominal quotient search. These are distinct research directions; do not combine results without a common formal semantics and matched evidence.
