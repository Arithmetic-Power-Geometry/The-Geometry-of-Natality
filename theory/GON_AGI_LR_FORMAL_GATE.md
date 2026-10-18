# GoN research gate G0/G3: deterministic action discovery
No version number. This is a baseline implementation, not a new algorithm.

An instance is an ordered list of finite actions. Action i has positive integer cost c_i, nonnegative integer reward r_i, and either no prerequisite or a parent j<i. Initially only actions with no parent are enabled. Performing an enabled action incurs its cost, earns its reward, and reveals its direct child actions. Actions can execute at most once. Budget B limits total cost. The objective is the sum of earned rewards. This is a deterministic, fully specified action-catalogue model with *online presentation* of actions, not a partially observable stochastic model; the oracle is granted the complete catalogue.

Correctness baseline A: exhaustive enumeration of all feasible execution sequences.
Correctness baseline B: memoized exact dynamic programming on (executed bitmask, remaining budget).
Weak decision baseline C: greedy highest immediately available reward/cost ratio.

Experiment: 120 deterministic seeds, 4–10 actions, costs 1–3, rewards 0–9, budget 2–9. Independent local Python execution: 120/120 DP-vs-exhaustive matches; DP beats greedy in 24 instances and ties in 96; 0 failures. A three-action witness yields optimum 6 versus greedy 4.

**Critical negative conclusion:** This grammar is a prerequisite forest with a static underlying action catalogue. Its apparent 'action discovery' is simply a presentation convention. The objective reduces to precedence-constrained knapsack. It is NOT a new generative graph planning problem and NOT Q1-ready. The greedy comparison is insufficient for algorithmic publication.

Next gate: create a grammar with genuine previously unenumerated identities or adversarial partial observations and prove that it is not a disguised classical model. Compare to established graph transformation planning and contingent planning. If equivalent, explicitly stop rather than renumber.
