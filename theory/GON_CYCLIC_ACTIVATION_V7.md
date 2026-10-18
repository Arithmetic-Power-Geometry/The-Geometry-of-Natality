# Geometry of Natality (GoN) V7: cyclic activation and condensation

Status: a rigorously specified cyclic prerequisite model; results are consequences of classical SCC theory, not established novel results.

## Model
Let D=(V,A) be a directed prerequisite graph, with arc u->v meaning activation of v requires activation of u. Each vertex has nonnegative integer cost c(v) and reward w(v). A feasible activated set F is predecessor-closed: v in F and u->v implies u in F. Budget B bounds sum of costs, and GoN potential Q_B maximizes sum of rewards. All nodes are optional; the model is not the rooted reachability tree model of V6. This distinction is essential.

## Theorem 7.1 (SCC all-or-none)
Every feasible F contains either all vertices of a strongly connected component or none. Proof: if one v is active, every predecessor on every directed path to v must be active; all SCC members are mutual predecessors.

## Theorem 7.2 (exact condensation reduction)
Contract each SCC C to one node of weight c(C)=sum_{v in C} c(v) and reward w(C)=sum_{v in C} w(v). The condensation is a DAG. Feasible F correspond bijectively to predecessor-closed subsets of condensation nodes, preserving total cost and reward. Proof: T7.1 and correspondence of predecessor paths.

## Corollary 7.3 (cycle threshold)
A strongly connected prerequisite component C cannot contribute any reward unless budget >=c(C), but meeting that threshold may not suffice if prerequisite components outside C must also be activated.

## Proposition 7.4 (closure under union and intersection)
The family of predecessor-closed subsets is closed under union and intersection. Proof: if a selected vertex has a predecessor, that predecessor belongs to each containing closed set. This forms a finite distributive lattice (classical order-ideal structure).

## Proposition 7.5 (hardness)
The model includes 0-1 knapsack when there are no arcs. Thus binary-encoded optimization is NP-hard by the standard knapsack special case. This is not a novel hardness result.

## Counterexample 7.6
Two vertices a,b with a->b and b->a, each cost 1 and reward 1. Budget 1 gives Q_1=0, budget 2 gives Q_2=2. The SCC must activate as a unit.

## Algorithms
Exact baseline A: enumerate all 2^n subsets, check predecessor closure and cost.
Exact baseline B: compute SCCs, enumerate all 2^q subsets of the q-node condensation DAG and check closure and cost. Both solve exactly the same objective; SCC reduction is standard.
For general DAGs, simple independent-child tree DP does not apply because subgraphs can share prerequisites.

## Limits
No new GoN-specific algorithmic advantage is established by using SCC condensation. An original contribution must go beyond this established reduction.
