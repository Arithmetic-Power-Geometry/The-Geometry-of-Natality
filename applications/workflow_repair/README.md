# Dependency-repair fixture

This directory contains the synthetic workflow-recovery instance and exact verification scripts used in *The Geometry of Natality: Creation Obligations, Attainable Futures, and Costed Structural Transformation* (Akhtar, 2026). The deposited manuscript is available at https://doi.org/10.5281/zenodo.23456986.

## Repair model

A dependency edge `u -> v` means that service `u` requires service `v`. The initial graph contains an operational ingress service, a failed authentication service, and an operational reporting service that depends on authentication. Recovery is defined by the reporting service becoming usable. The experimental action set is finite, deterministic and single-use.

| Action | Cost | Prerequisite | Effect |
| --- | ---: | --- | --- |
| Restart authentication | 3 | None | Marks the existing authentication service operational |
| Create replacement | 2 | None | Creates an operational authentication replacement with a distinct identity |
| Rewire reporting | 1 | Replacement created | Redirects the reporting dependency from the failed authentication service to its replacement |

The global budget is 3. Restarting the original service or creating the replacement and rewiring the dependent both meet the goal at total cost 3. Creating the replacement alone does not make reporting usable. The fixture also excludes forbidden dependencies as specified in [`fixture.json`](fixture.json). A cyclic dependency is treated as unusable by the fixture oracle; this is an experimental convention rather than a general rule for dependency networks.

## Verification

Run from the repository root:

```bash
python applications/workflow_repair/verify_fixture.py
python applications/workflow_repair/compare_independent_oracles.py
python applications/workflow_repair/optimality_certificate.py
python applications/workflow_repair/scaling_benchmark.py
python applications/workflow_repair/decomposition_research.py
```

The exhaustive certificate considers 16 ordered subsets of the three named actions. Four pass the action-applicability and budget checks, and two reach the goal with minimum cost 3. Uniform-cost search independently recovers the same optimum.

The synthetic scaling study uses independent groups of the same repair problem. For groups `n = 1, 2, 3, 4` and three deterministic action-order seeds per size, exhaustive enumeration and uniform-cost search agree on the optimal cost `3n`. Reported search-work counts are not equivalent runtime or memory measurements. The decomposition checks use eight group counts and three action-order seeds; full-state cross-checks were performed for `n <= 4`.

## Model and comparison boundaries

The repair fixture is not an operational incident dataset. Graph transformations can encode the same operations; the model does not claim a representational impossibility for GROOVE or other graph-rewriting systems. The repository's GROOVE translation material is a specification and baseline protocol, not an executed matched comparison for this fixture. The three-relay GROOVE grammar reported separately in the preprint is a distinct experiment and should not be conflated with a GROOVE implementation of this recovery example.

The decomposition identity requires action and goal independence, with the global additive budget enforced after summing unbudgeted local optima. Shared restart capacity, cross-group dependencies or action costs that depend on other groups invalidate that decomposition certificate. Fresh-name quotient search is justified only under explicit identity-permutation equivariance. These qualifications are developed in Sections 9–13 of the deposited manuscript.

## Related records

- [Main repository overview](../../README.md)
- [Research freeze and earlier verification evidence](../../research/GON_RESEARCH_FREEZE_FOR_MANUSCRIPT_2026-10-18.md)
- [Deposited preprint V1](https://doi.org/10.5281/zenodo.23456986)
