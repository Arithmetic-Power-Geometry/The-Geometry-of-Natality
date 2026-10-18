# GoN decomposition research gate

**Research objective:** determine precisely when component-wise minimum-cost repair planning is exact, and document failure modes. This is NOT a new GoN theorem.

## Exactness theorem (under stated assumptions)
Let the global state be a product of local states. Assume actions each affect one local state only; action applicability, cost, and effect depend only on that local state; the goal is the conjunction of local goals; no global budget coupling except an additive total-cost cap; and no global forbidden configurations. Then the minimum total cost equals the sum of local minimum costs, and concatenating local optimal plans gives an optimal global plan.

**Proof:** Project any global feasible plan onto each local action set. Its projection remains locally feasible, and the total cost is the sum of projected costs, hence no global plan can beat the sum of local optima. Conversely, concatenate local optimal plans; noninterference makes all steps applicable and the global goal true, attaining the lower bound.

## What breaks the proof
A shared capacity constraint allowing at most one restart across two components invalidates a plan that independently restarts both components. A mere equality of numerical minimum costs does not prove a returned plan feasible. Coupled dependencies, shared budgets with nonlinear costs, global safety invariants, and cross-component action preconditions likewise invalidate the simple projection argument.

## Implemented experiment
`applications/workflow_repair/decomposition_research.py` verifies 24 independent-component instances (n=1..8, three action-order seeds), compares n<=4 against full-state uniform-cost search, and rejects a deliberately coupled case. CI stores `decomposition_results.json`. The 24 tests use one synthetic model family, not 24 independent real-world systems.

## Scientific interpretation
This demonstrates an **exact implementation of a standard decomposition method**, with a documented applicability boundary. It does not establish that GoN has a novel algorithm. No matched GROOVE grammar or realistic coupled-workload performance benchmark has been completed. For publication, a nontrivial sound reduction beyond standard separability, independent validation on coupled systems, and relevant prior-art comparison remain necessary.
