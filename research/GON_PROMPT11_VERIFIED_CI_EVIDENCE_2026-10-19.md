# Prompt 11 — verified GitHub CI evidence
Date: 2026-10-19

- Successful workflow: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39210667982
- Tested commit: `5ba5754b3dd6d06521e1182a55ca82ad496feec4`
- Jobs API confirms all steps success: checkout, Python setup, compile, five independent tests, deterministic falsification JSON, assertions, artifact upload.
- Artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39210667982/artifacts/12167641064
- GitHub ZIP SHA256: `f40b02c151cbd64f550b8f7924c026bd6eb312f39e9a5eaf38fdf42c3265a1fb`.
- Deterministic test scope: 9,261 complete three-terminal three-template instances with nonempty cover sets and costs 0/1/2; independent directed-graph subset enumeration and exact subset-mask Dijkstra agree, including unreachable cases.
- H1 and H2 counterexamples retained. H3 equivalence proof is conditional and standard Set Cover, not a novel contribution.
- External baseline **not implemented**. The graph traversal exhaustive oracle is independent of subset-DP, but both are in-repository. No GROOVE/third-party MILP matched evaluation.
- Novelty gate **NOT PASSED**; external baseline gate **NOT PASSED**; bounded internal verification gate **PASSED**.
- New report commit follows tested CI code, and is not itself retested because it only records evidence.
