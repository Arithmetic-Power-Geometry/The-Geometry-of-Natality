# Prompt 6 — structural conjecture falsification and prior-art positioning
Date: 2026-10-19
Status: **three falsifiable hypotheses; no new GoN theorem established**

## Model and hypotheses
Closed two-choice multi-component repair model. Component i has nonnegative restart cost r_i and creation-plus-rewire cost q_i=c_i+w_i. A shared capacity permits at most k restarts. No other coupling, identity-sensitive constraints or negative conditions.

- **H1 (false):** Sum of independent local minima remains optimal under shared restart capacity.
- **H2 (false):** Select the k lowest absolute restart costs to minimize global cost.
- **H3 (true for this restricted model, but standard):** Let d_i=q_i-r_i. Optimal cost is sum_i q_i minus the sum of the largest at most k strictly positive d_i.

## Proof of H3
For any chosen restart subset S with |S|<=k, the plan cost is
C(S)=sum_i q_i - sum_{i in S}(q_i-r_i).
Thus minimizing C is equivalent to maximizing the sum of savings d_i over subsets of cardinality <=k. No negative or zero saving is needed. An exchange argument replaces any chosen smaller positive saving by an unchosen larger saving without violating cardinality or increasing cost. Repeating yields the k largest positive savings. The plan is feasible because no coupling exists except unit restart capacity. This is the uniform-matroid greedy principle (or elementary cardinality-constrained selection), **not a new GoN theorem**.

## Minimal explanatory counterexamples
- **H1:** two components, r=1, c=2, w=1 each, k=1. Independent sum=2; globally feasible optimum=4. (Existing CE-02.)
- **H2:** two components: A (r=1,c=1,w=0), B (r=2,c=2,w=2), k=1. Cheapest restart selects A, cost 1+4=5; choosing B gives 1+2=3. This demonstrates that savings, not absolute restart cost, governs choice.
- **H3:** no counterexample in enumerated finite domain, subject to CI confirmation; proof above covers all nonnegative costs in this model.

## Reproducible search
- `experiments/research_gate/natality_conjectures.py` enumerates n=1..3 components, all triples (r,c,w) in {0,1,2}^3, all capacities 0..n.
- Number of model/capacity combinations = 27*2 + 27^2*3 + 27^3*4 = **80,973**.
- Independent brute force enumerates all 2^n strategy vectors with at most k restarts.
- `tests/test_natality_conjectures.py` tests all enumerated instances plus explicit strict-gap and heterogeneous-savings fixtures.
- GitHub Actions: `.github/workflows/gon-conjecture-gate.yml`. Evidence artifact contains deterministic counterexample ledger and tested counts.

## Prior art: verified public primary/secondary sources (not exhaustive novelty clearance)
1. Hoffmann, Lomonosov & Sitharam (2000/2003), *Planning Geometric Constraint Decomposition via Optimal Graph Transformations*, DOI 10.1007/3-540-45104-8_25 — prior optimal graph-transformation planning and decomposition.
2. Varró-Gyapay & Varró (2007), *Optimization in Graph Transformation Systems Using Petri Net Based Techniques*, DOI 10.14279/tuj.eceasst.2.61 — costed rule-based reachability optimization.
3. Crespelle, Drange, Fomin & Golovach (2023), *A survey of parameterized algorithms and the complexity of edge modification*, DOI 10.1016/j.cosrev.2023.100556 — substantial existing graph modification/parameterized complexity literature.
4. *Empowering model repair: a rule-based approach to graph repair without side effects—extended version* (2024), https://link.springer.com/article/10.1007/s11334-024-00587-w — formal correctness and implementation of graph repair.
5. *Experimenting with Reaction Systems using Graph Transformation and GROOVE* (2025/26), https://link.springer.com/article/10.1007/s11047-025-10045-6 — modern graph-transformation state-space methodology.

These references establish crowded prior art; no claim of exhaustive literature search, theorem priority, or publication novelty is made. Do not insert H3 as a new principal theorem without a demonstrably distinct extension.

## Decision
H1 and H2 should be preserved as counterexamples and diagnostic controls. H3 can be a **baseline lemma** for shared-capacity repair selection, but its proof is elementary and algorithmic consequence is sorting savings in O(n log n), not new complexity theory. The Prompt 6 novelty gate is **NOT PASSED**. Proceed to benchmark design (Prompt 7) only with this limitation explicitly retained.

## Prompt 7
Freeze a stratified benchmark protocol: independent, shared-resource, graph-coupled, identity-sensitive and history-sensitive instances; generated seeds and topology hashes; exact baseline comparability; synthetic versus externally sourced networks; falsification metrics; matched plain UCS, orbit UCS, decomposition, and an established symmetry/GROOVE baseline when genuinely supported. Pre-register failure and uncertainty reporting. Do not fabricate real-world evidence.
