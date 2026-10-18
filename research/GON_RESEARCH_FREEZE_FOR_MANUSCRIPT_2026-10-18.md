# GoN research freeze for manuscript drafting — 18 October 2026

## Decision
Freeze the **currently verified synthetic research evidence** for transparent manuscript drafting. This is **NOT a claim that the research is complete or Q1 submission-ready**. Any new research claim requires a new experiment and a new dated evidence record.

## Primary artifact and reproducibility
- Repo: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality
- Verified CI: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39151100642 (success)
- Original fixture: `applications/workflow_repair/fixture.json`
- Independent oracle: `applications/workflow_repair/compare_independent_oracles.py`
- Exhaustive certificate: `applications/workflow_repair/optimality_certificate.py`
- Scaling: `applications/workflow_repair/scaling_benchmark.py`
- Decomposition and coupling guard: `applications/workflow_repair/decomposition_research.py`
- Experimental interpretation: `experiments/research_gate/GON_SCALING_VERIFIED_2026-10-18.md`
- Theorem and limitations: `experiments/research_gate/GON_DECOMPOSITION_RESEARCH_GATE.md`
- Working manuscript: `paper/GoN_Cost_Optimal_Repair_Planning_DRAFT.md`
- Bibliography: `references.bib`, 27 entries at freeze; entries require metadata verification before final publication.

## Verified, narrow results
1. Three-service synthetic fixture: minimum repair cost 3; two optimal plans; 16 ordered subsets exhaustively audited.
2. Twelve synthetic scaling instances (n=1..4, three action-order seeds): exact enumeration and uniform-cost search agree on optimum 3n. CI passed.
3. Twenty-four synthetic decomposition cases (n=1..8, three seeds): exact independent-component decomposition returns 3n; full UCS cross-check performed for n<=4. CI passed.
4. Counterexample to coarse alive/edge/birth-count summary for exact goal-reachability quotient; counterexample to independently selected plans under shared restart capacity.
5. Proof of optimal-cost separability under strict action/goal independence. This is a known decomposition principle, not a GoN novelty theorem.

## Claims prohibited in the manuscript
- That GoN is demonstrated novel versus GROOVE, CEGAR, symmetry reduction, partial-order reduction, or standard UCS.
- That GROOVE has been benchmarked on a matched GoN repair grammar.
- That synthetic results are real-world validation.
- That there are completed publication-quality figures, tables, or four new algorithms.
- That a Q1 journal will accept the work or that Q1 originality has been achieved.

## Remaining scientific gates (not completed)
1. GoN-specific valid GROOVE grammar and matched cost/goal comparison.
2. Coupled, varied workloads and ideally real dependency-network evidence.
3. A mathematically nontrivial, literature-distinct GoN algorithm or theorem with proof, ablation and reproduction.

## Paper-writing instruction
Draft a rigorous **preliminary methods/verification paper** or working preprint from these artifacts, explicitly label it preliminary, and leave missing results as limitations. Do not invent benchmarks, datasets, or citations. If the target is a novel Q1 research article, do not submit until the three remaining scientific gates are met.
