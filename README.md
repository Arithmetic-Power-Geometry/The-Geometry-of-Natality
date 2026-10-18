# Geometry of Natality — benchmark 001

Reproducible test of single-edge *natality gain*: the number of newly reachable vertices from a fixed source.

Run `python benchmark.py` with Python 3.9+ (standard library only). Five graph families, four sizes (12,18,24,30), and 50 deterministic seeds per cell give **1,000 graphs**.

Classical baseline evaluates all useful absent directed edges by temporarily adding each edge and executing BFS. Target-grouped evaluation computes the additional reachability from each unreachable target only once. Both solve the **same classical reachability optimization objective**.

Recorded findings: **1,000/1,000** exact optimal-gain matches; **743** graphs with nonzero gain; total target-grouped evaluation **0.014753 seconds** versus explicit exhaustive edge evaluation **0.134495 seconds** in one run. These are *not* stable speed benchmarks; graph sizes are small, and no uncertainty or independent replicates were measured.

Full measured outputs are also available in the accompanying downloadable benchmark archive. The experiment **does not establish mathematical novelty**. Next steps include SCC-condensation baselines, multi-edge budgets, scaling experiments, hard adversarial instances, and proposing a distinct invariant.
