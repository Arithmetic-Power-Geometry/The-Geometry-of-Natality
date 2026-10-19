# Geometry of Natality — Prompt 2 falsification and conditional theorem (19 October 2026)

## Model
Finite typed costed state system, shared observation map obs, capability set X, budget B. F_B(X) is the set of reachable observation classes within cost B; V_B(X)=|F_B(X)|. Natality gain N(B)=|F_B(E)\\F_B(empty)|. Pairwise interaction Δ=V(ab)-V(a)-V(b)+V(empty). These are exploratory observables, not established new mathematical operations.

## C1 REFUTED
States s,x; creation-enabled s→x costs 1 and creation-free s→x costs 2. At budgets 0,1,2, gain is 0,1,0. Thus gain is not monotone in budget, although F_B(empty)⊆F_B(E) for fixed B.

## C2 REFUTED
States s,xa,xb; a creates xa and b creates xb, each at cost 1. Both created states map to observation 'new'. At B=1, V(empty,a,b,ab)=(1,2,2,2), so Δ=-1. Redundant capabilities can yield negative interaction.

## C3 REFUTED AS STATED
Two locally independent bits and cost-one local creation actions a,b. Observations 00,10,01,11. At budget 1, V=(1,2,2,3), Δ=0. At budget 2, V=(1,2,2,4), Δ=1. No action reads/writes the other component. **Important correction:** product-outcome cardinality itself induces a positive interaction once both changes are affordable; 'shared budget coupling' is not the only explanation. Zero interaction requires additional conditions on the value functional, not just local transition independence.

## C4 CONDITIONAL THEOREM
Suppose a finite group acts equivariantly on states and actions, preserving costs, capability labels, admissibility, initial-state orbit, history-dependent guards, and observation classes. Form the exact orbit quotient with induced weighted transitions. For each X,B, the quotient preserves the reachable observation classes F_B(X), hence V_B(X), natality gain and all pairwise interactions.

Proof: Project each concrete path to a same-cost quotient path. Conversely, for each quotient transition from an orbit and any representative of its source, equivariance transports a witness edge to that representative with the same cost and capability label. Inductively lift every quotient path to a concrete path. Observation invariance and budgets preserve exactly the outcome classes. Apply to each X. QED.

This is a specialization of established symmetry quotient principles, NOT a novel foundational theorem. Unequal creation costs break the purported identity swap and invalidate naive quotienting. The finite test checks a two-name swap and independently rejects a non-equivariant cost assignment.

## Independent tests
See `research/theory/p02_natality_oracles.py`: Python standard library, Dijkstra and separate Bellman-Ford relaxation. All assertions passed in the executed local source and matching committed regression logic. Synthetic finite models only; no GROOVE execution or real operational traces in Prompt 2.

## Prior art checked
Rensink (2004), GROOVE state-space generation DOI 10.1007/978-3-540-25959-6_40; Fernández and Gabbay (2005), nominal rewriting with name generation DOI 10.1145/1069774.1069779; Bach (2019), submodular set-functions DOI 10.1007/s10107-018-1248-6. Name generation, graph rewriting and second set-function differences are established. Minimal correction-set literature remains a required deeper comparison.

## Verdict
C1,C2,C3 falsified; C4 conditional proof and finite regression passed. Mathematical falsification gate PASS. **No new natality-specific structural theorem established; journal novelty gate NOT PASSED.** Prompt 3 must seek and adversarially test such a theorem.
