# GoN V9 — controlled comparison protocol

## Tasks
T1 Existing-vertex accessibility: fixed graph, allowed edge additions, budget. Baselines: exact enumeration, SCC condensation, established edge-augmentation algorithms. GoN adds no claim of advantage.
T2 Prerequisite activation: fixed catalogue of items with costs/rewards and DAG constraints. Baselines: exhaustive, precedence-constrained knapsack exact methods, ILP. GoN adds no claim of advantage.
T3 Generative creation: catalogue of vertex-creating and activation actions with identity tracking and dependency constraints. Baselines: graph rewriting/transition-system exploration, generic 0-1 ILP, exact action-set enumeration.
T4 Unknown-catalogue expansion: action execution reveals potential successor actions/states; requires an explicit observation/oracle model and matched information budgets. This is a prospective research task, NOT a result.

## Fairness and preregistration
Keep identical feasible action spaces, budgets, objectives and stopping criteria for all solvers. Distinguish objective improvement from runtime improvement and from expressive modeling power. Report input construction, seed, Python version, CPU, memory, repetitions, timeouts, and uncertainty. Exact-match counts do not imply superior performance. Avoid using invented application data.

## Go/No-Go criterion
Do not write a Q1 research paper claiming superiority unless a nontrivial contribution survives prior-art review and independent replication. A book chapter may still use standard results with attribution.
