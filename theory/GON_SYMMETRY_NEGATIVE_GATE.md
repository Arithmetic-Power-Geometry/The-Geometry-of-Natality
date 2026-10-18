# GoN research gate: symmetry and succinctness — NEGATIVE novelty finding

No new numbered GoN version. This is an adversarial baseline and stop/go decision.

## Formal experiment
There are n independent one-shot birth actions. Action i adds one distinct persistent child i. A configuration is the subset S of completed actions, so the explicit reachable-state graph has exactly 2^n configurations. If observations, rewards, and future action rules depend **only on |S|**, all subsets with the same cardinality can be quotiented into n+1 count states. The count quotient preserves the count-labelled transition possibilities under this restricted observation model.

Proof: all subsets of [n] are reachable, hence 2^n; each count k in [0,n] occurs, hence n+1. For k<n, any size-k subset has a successor of size k+1, and no other birth successor counts. Thus count transitions are well defined. This is ordinary symmetry reduction / counter abstraction.

## Critical counterexample to an overstrong claim
If the observer asks whether child 0 exists, S={0} and S={1} have the same count but different observations. Therefore the count quotient is **not** sound for identity-sensitive properties. The experiment includes this adversarial check.

## Independent local execution
Ran the Python standard-library script on n=1..16; all assertions passed. The largest case has 65,536 explicit states and 17 count states (ratio 3,855.0588). These are exact cardinalities, not timing measurements or general solver speedups.

## Prior art and novelty
Burch et al. (1992), *Symbolic model checking: 10^20 states and beyond*, DOI 10.1016/0890-5401(92)90017-A, develops symbolic state-space representations. Emerson and Wahl (2005), *Efficient Reduction Techniques for Systems with Many Components*, DOI 10.1016/j.entcs.2005.03.019, explicitly use symmetry reduction through counter abstraction.

**Gate result:** FAIL for originality. Exponential-vs-count compression in this family is not a new GoN theorem or algorithm. This gate prevents rebranding classical symmetry reduction as GoN performance.

## Next research decision
No more counting examples or new V-number. An original result must survive comparison with symmetry reduction, BDD/SAT symbolic methods, graph rewriting, and planning, on identity-sensitive and locally constrained generative tasks. If no such problem can be defined and justified, develop GoN as a conceptual book rather than claim a Q1 theory paper.
