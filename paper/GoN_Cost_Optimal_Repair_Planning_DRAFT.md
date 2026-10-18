# The Geometry of Natality: Cost-Optimal Repair Planning in Evolving Dependency Graphs

**Status: research working draft, NOT submission-ready.** This document distinguishes proven properties of an explicitly defined model from novelty claims that require external comparison.

## Abstract (provisional)
We study finite repair planning for dependency systems with failed services, creation of replacement services, and rewiring actions. A repair instance comprises an initial graph, finite actions with preconditions and nonnegative costs, a budget, forbidden configurations, and a recovery predicate. We provide an exact exhaustive oracle and an independently implemented uniform-cost search baseline. A three-service synthetic fixture admits two optimal repairs of cost three, independently verified. We additionally implement a parameterized family of independent failed services and compare exhaustive enumeration against uniform-cost search on 12 generated instances. These experiments validate the implementation on synthetic data only. A matched GROOVE baseline, real-world validation, and a distinctive new reduction theorem remain open. No superiority or Q1-level originality is claimed.

## 1. Problem statement
Let a state be `s=(V,E,L,H)`, where `V` are components, `E` are directed dependencies, `L` records component status and `H` records the action history when preconditions depend on past actions. Let `A` be a finite set of partial state transitions. Each `a in A` has a nonnegative cost `c(a)`. Given start state `s0`, forbidden-state predicate `F`, recovery predicate `Goal`, and budget `B`, find a finite applicable action sequence `pi` such that `Goal(T_pi(s0))`, no intermediate state satisfies `F`, and `sum(c(a)) <= B`. Minimize that sum. In the finite-action model, each action may execute at most once.

## 2. Algorithm 1: independent exhaustive oracle
Enumerate every ordered subset of distinct actions; simulate action preconditions, effects, forbidden states, and budget; retain feasible goal-reaching plans; select minimum total cost. Worst-case sequence count is `sum(k!/(k-j)!, j=0..k)`, before pruning.

## 3. Algorithm 2: uniform-cost search
Use a min-priority queue keyed by accumulated nonnegative cost. Include the *full relevant state and used-action mask* in the state key. For each popped state, expand applicable unused actions and update its best known cost. Stop when a goal state is removed from the queue.

### Proposition 1 (standard UCS correctness; not claimed as novel)
Assume (i) finite states/actions, (ii) nonnegative action costs, (iii) the state key contains all information determining future applicability, costs, and goal satisfaction, and (iv) transitions are deterministic as implemented. If a goal is reachable, uniform-cost search returns a minimum-cost plan.

**Proof.** Each feasible plan is a path in the finite nonnegative weighted state graph. Uniform-cost search is Dijkstra's algorithm on that graph. When a goal is first removed with current minimum distance, no lower-cost path to any goal remains in the queue, by nonnegativity and the relaxation invariant. Retaining the action-history mask prevents merging states with different future legal actions. QED.

### Proposition 2 (independent subproblems; conditional and not claimed as novel)
Suppose `n` repair subproblems have disjoint action sets, each action changes only its own subproblem, the goal is a conjunction of independent local goals, and total cost is additive. Then global optimal repair cost equals the sum of local optimum costs.

**Proof.** Any global feasible plan projects to a feasible plan for each local subproblem, so its cost is at least the sum of local optima. Concatenating independently optimal local plans is feasible by disjointness and attains the sum. QED.

**Limitation:** This separability theorem does not apply when cross-service constraints, resource coupling, or dependencies connect subproblems. It is a standard decomposition observation, not an established GoN novelty claim.

## 4. Verified initial instance
Synthetic fixture `applications/workflow_repair/fixture.json`: services ingress (alive), auth (failed), report (alive), with dependency report->auth. Repair A restarts auth (cost 3). Repair B creates auth_v2 (cost 2) and rewires report->auth_v2 (cost 1). The minimum cost is 3. An exhaustive 16-sequence certificate and an independent oracle are implemented. All figures and counts refer only to this fixture.

## 5. Synthetic scaling protocol
`applications/workflow_repair/scaling_benchmark.py` generates `n=1..4` independent failed-service subproblems with three actions each and deterministic action-order seeds `0,1,2`. Compare exhaustive search and uniform-cost search, asserting equal optimum `3n` and checking at least `2^n` minimum-cost goal plans under exhaustive enumeration. Record expansion counts, distinct UCS states, and wall-clock times; archive JSON from GitHub Actions. **This benchmark is designed for verification, not to demonstrate a new GoN advantage.** Timings are environment-dependent.

## 6. Candidate tables and figures (NOT completed results)
Table 1: problem symbols and assumptions. Table 2: repair action semantics. Table 3: verified fixture solutions. Table 4: generated-instance experiment settings. Table 5: exact vs UCS results (populate only from CI artifact). Table 6: GROOVE/GoN matched comparison (BLOCKED).
Figure 1: repair transition model. Figure 2: fixture before/after repair. Figure 3: exact oracle vs UCS state exploration. Figure 4: measured scaling (after CI). Figure 5: matched baseline (BLOCKED).
Algorithm 3: candidate novel repair-preserving reduction (NOT DEVELOPED). Algorithm 4: independent baseline validation (NOT DEVELOPED).

## 7. Threats to validity
All current examples are synthetic and largely independent; the model does not yet capture concurrency, probabilistic failures, resource constraints, or real repair logs. Standard UCS is not novel. A coarse summary `(alive_count,edge_count,birth_count)` has a counterexample and must not be used as an exact quotient. The official GROOVE Generator smoke test succeeded but the attempted unrestricted sample grammar exhausted heap; there is no matched GROOVE repair experiment. The absence of this baseline precludes performance superiority claims.

## 8. Publication gate
Before claiming Q1 readiness: (1) verify a new formal property or algorithm against prior art; (2) implement the same GoN repair instance as a valid GROOVE grammar; (3) compare equivalent goals, constraints, and costs; (4) run diverse and preferably real workloads with variance and uncertainty; (5) perform independent reproduction; (6) verify each cited bibliographic record. Bibliography: `references.bib` (existing entries; no reference-count target is a substitute for relevance).
