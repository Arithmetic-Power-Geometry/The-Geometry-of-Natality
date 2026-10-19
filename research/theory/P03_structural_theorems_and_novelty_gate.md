# Geometry of Natality — Prompt 3 structural research gate (2026-10-19)

## Precise theorems (elementary, not novel)
For finite common observation classes o, fixed initial state, nonnegative transition costs and capability-restricted distances d_X(o), define F_B(X)={o:d_X(o)<=B} and V_B(X)=|F_B(X)|.

**P3.1 Budget-interval identity:** With E the full capability set and 0 the no-create system, unchanged common transitions imply d_E(o)<=d_0(o). Then N(B)=|F_B(E)\F_B(0)|=Σ_o 1[d_E(o)<=B<d_0(o)]. Proof: indicator expansion of the set difference.

**P3.2 Integrated gain:** If all distances are finite nonnegative integers, Σ_{B>=0}N(B)=Σ_o(d_0(o)-d_E(o)). Proof: count the integer budgets in each half-open interval. Infinite baseline distance can make the integral infinite. Real-valued costs admit a Lebesgue integral analogue.

**P3.3 Interaction sign identity:** Let A=F_B(0), P=F_B(a), Q=F_B(b), R=F_B(ab), with A⊆P,Q⊆R. Then Δ=|R|-|P|-|Q|+|A|=|R\(P∪Q)|-| (P∩Q)\A |. Proof: inclusion-exclusion. Joint-only observations contribute positively; overlapping new observations negatively. This is classical set algebra, not a new theorem of graph rewriting.

## Independent finite experiments
Local standard-library script `p03_exhaustive.py` (included in the Prompt 3 downloadable archive) enumerates 2/3-state directed graphs with up to 3 arcs, costs 1/2, labels ordinary/a/b, observation assignments 0/1 and budgets 0–4. Independent Floyd–Warshall and synchronous Bellman–Ford agree in **393,600** distance-vector comparisons across **98,400** graph-observation-budget cases.

Interaction signs: **96,950 zero, 842 negative, 608 positive**. Counts reflect exhaustive synthetic enumeration, NOT independent network samples or a distribution over real systems.

Positive witness: s -a(1)-> x -b(1)-> y, observations obs(s)=obs(x)=0, obs(y)=1, B=2; V=(1,1,1,2), Δ=+1.
Negative witness: s -a(1)-> x and s -b(1)-> y, obs(s)=0, obs(x)=obs(y)=1, B=1; V=(1,2,2,2), Δ=-1.
Zero witness: all reachable states observationally equivalent, V=(1,1,1,1), Δ=0.

Threshold and integer integrated-gain identities passed finite regression tests. No GROOVE experiment was performed in Prompt 3; previous Prompt 17 GROOVE evidence must not be conflated with these cases.

## Primary literature comparison
Rensink (2004), GROOVE simulator DOI 10.1007/978-3-540-25959-6_40: graph rewriting and state-space generation established.
Fernández and Gabbay (2005), Nominal Rewriting with Name Generation DOI 10.1145/1069774.1069779: fresh-name generation established.
Bach (2013), Learning with Submodular Functions arXiv:1111.6453; Bach (2015), Submodular Functions: from Discrete to Continuous Domains arXiv:1511.00394: set-function marginal interactions established.

## Editorial gate
Elementary theorem correctness: PASS. Finite computational falsification: PASS. Full independent GROOVE matched test: NOT PERFORMED. Genuine new natality-specific theorem: NOT ESTABLISHED. **Novelty gate FAIL; do not proceed to Prompt 4 submission drafting.** The original 14-page paper, its 6 propositions/4 algorithms/4 figures/8 tables/23 references, and the user's original conceptual PNG remain preserved in the downloadable archive. Figure is schematic, not experimental evidence.
