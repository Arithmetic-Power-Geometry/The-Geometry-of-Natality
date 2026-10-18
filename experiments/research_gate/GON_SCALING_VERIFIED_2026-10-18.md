# GoN scaling evidence — verified GitHub Actions run

Run: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39150863378
Evidence artifact: `gon-independent-oracle-evidence` (GitHub artifact ID 12145505260).
Implementation: `applications/workflow_repair/scaling_benchmark.py`.
Verification: job 117744053180; independent-oracle comparison, optimality certificate, scaling benchmark, and artifact upload all passed.

| Independent failed-service groups | Actions | Exhaustive expansions | UCS expansions | Verified minimum cost |
|---:|---:|---:|---:|---:|
| 3 | 9 | 3,796 | 78 | 9 |
| 4 | 12 | 314,217 | 399 | 12 |

Three action-order seeds (0, 1, 2) were tested for each size n=1,2,3,4, yielding 12 instances. The two methods agree on optimal cost 3n on all 12. The quoted expansion counts are deterministic for these seeds, but **are not GROOVE results**. The measured advantage over naive exhaustive enumeration is expected for standard uniform-cost search, and **does not establish a novel GoN reduction**. This family consists of independent repair groups; no external data, concurrent changes, or coupled constraints have been tested. Raw per-instance JSON is available in the linked CI artifact. Avoid claiming publication-level statistical generalization from these observations.

**Next evidence gate:** actual GoN repair grammar under GROOVE with matched state semantics, then a substantive reduction theorem and controlled comparison. Current Q1 originality status: NOT established.
