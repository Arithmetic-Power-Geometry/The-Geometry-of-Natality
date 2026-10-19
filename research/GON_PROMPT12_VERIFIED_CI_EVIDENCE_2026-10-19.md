# Prompt 12 — verified external MILP CI evidence
Date: 2026-10-19
- Successful workflow: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39210823910
- Tested SHA: `6fffbf4348b38bf9714971973e0fc09a99a10e25`.
- All steps passed: checkout, Python 3.11, external NumPy 2.2.6 / SciPy 1.15.3 installation, syntax compilation, unit tests and complete deterministic sweep, machine-readable output, assertion checks and artifact upload.
- Artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39210823910/artifacts/12167806470
- GitHub artifact SHA-256: `e81a851afd4b43760703802b801139bf1f47532232610e0f967f559e3a44e247`.
- Tested **4,096** finite models; independent graph-reachability exhaustive enumeration and external SciPy/HiGHS MILP matched optimum or infeasibility. MILP solutions are graph-replayed.
- Bounded external mathematical-programming equivalence: **PASS**. GROOVE / independently authored graph-transformation semantics: **NOT TESTED**.
- Novelty: **NOT PASSED**. Broader operational validation: **NOT PASSED**.
- Report-only commits follow the CI-tested code; do not claim the report itself was CI tested.
