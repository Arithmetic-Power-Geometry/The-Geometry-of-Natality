# The Geometry of Natality

**Creation Obligations, Attainable Futures, and Costed Structural Transformation**

Mohammad Amir Khusru Akhtar  
Usha Martin University, Ranchi, Jharkhand, India  
amir@umu.ac.in

[Preprint (Zenodo)](https://doi.org/10.5281/zenodo.23456986) · [Citation](CITATION.cff) · [Code license](LICENSE)

## Overview

This repository accompanies the preprint *The Geometry of Natality: Creation Obligations, Attainable Futures, and Costed Structural Transformation* (2026). The study examines finite, costed dependency systems in which recovery may restore an existing component or create a replacement and redirect dependencies. Restoration, creation, and rewiring are separate actions with explicit prerequisites, costs, and admissibility conditions.

The manuscript develops a description of budgeted attainable futures, pairwise interactions between optional creation capabilities, minimal creation obligations, and obstruction sets. Its formal results are instances of established reachability, shortest-path, set-function, hypergraph-transversal, decomposition, and symmetry principles. Neither graph rewriting nor fresh-name generation is claimed as a new formalism.

## Main results and evidence

The preprint reports:

- A budget-interval expression for changes in attainable observations, together with a signed interaction decomposition distinguishing joint-only outcomes from overlap.
- A hitting-set characterization of minimal sets of creation capabilities whose removal prevents goal attainment.
- An exact synthetic repair fixture with three single-use actions: restart authentication (cost 3), create a replacement (cost 2), and rewire reporting (cost 1). Both restart and create-then-rewire attain the recovery goal at cost 3.
- Agreement between exhaustive enumeration and uniform-cost search on the fixture and a 12-run independent-group scaling experiment (four graph sizes, three action-order seeds per size).
- A guarded cost-decomposition identity under local independence and a fresh-name orbit-quotient result under equivariance. These are conditional statements; shared constraints and name-dependent behavior can invalidate the respective reductions.
- Additional bounded interaction, hypergraph, and three-relay graph-grammar checks described in the archived preprint.

The preprint gives the detailed experimental counts, formal hypotheses, proof boundaries, and limitations. Repository materials are organized by experiment; some material reflects earlier exploratory formulations and must not be treated as a replacement for the preprint.

## Repository organization

| Location | Contents |
| --- | --- |
| [`applications/workflow_repair/`](applications/workflow_repair/) | Synthetic three-service repair fixture, exhaustive checks, independent oracles, scaling and guarded decomposition scripts |
| [`experiments/research_gate/`](experiments/research_gate/) | Additional bounded verification scripts, regression evidence and documented experiments |
| [`experiments/v4/`](experiments/v4/) through [`experiments/v15/`](experiments/v15/) | Historical research experiments and their recorded outputs |
| [`theory/`](theory/) | Development notes, formal investigations and earlier research assessments |
| [`paper/`](paper/) | Earlier working manuscript material; not the deposited Version V1 |
| [`references.bib`](references.bib) | Working bibliography; consult the deposited preprint for the final cited reference list |
| [`.github/workflows/`](.github/workflows/) | Automated experiment and regression workflows |

The published Version V1 should be cited from Zenodo. A historical README, draft, or research note may describe an earlier scope or unresolved question and does not supersede the deposited paper.

## Reproducing the workflow-repair checks

The repair scripts use Python. Run the relevant commands from the repository root:

```bash
python applications/workflow_repair/verify_fixture.py
python applications/workflow_repair/compare_independent_oracles.py
python applications/workflow_repair/optimality_certificate.py
python applications/workflow_repair/scaling_benchmark.py
python applications/workflow_repair/decomposition_research.py
```

The Python scripts and recorded results document their own case definitions and output formats. The historical single-edge reachability benchmark can be run separately with `python benchmark.py`; it studies a different, classical edge-addition objective and is not evidence of a new graph-transformation method.

## Scope of validation

The reported repair and scaling data are synthetic. Deterministic action-order seeds are not independent network samples. Exhaustive search and uniform-cost search are classical exact methods and count work differently. The separate graph-grammar evidence described in the preprint does not constitute a matched, directly exported GROOVE-versus-planner cost benchmark for the three-service repair fixture. Neither practical superiority nor asymptotic improvement is claimed. See Sections 12–13 of the preprint for the specific GROOVE checks and the outstanding validation work.

## Citation

Akhtar, M. A. K. (2026). *The Geometry of Natality: Creation Obligations, Attainable Futures, and Costed Structural Transformation* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23456986

Machine-readable citation metadata are provided in [`CITATION.cff`](CITATION.cff).

## Copyright and licensing

Copyright © 2026 Mohammad Amir Khusru Akhtar.

Source code in this repository is licensed under the Apache License, Version 2.0; see [`LICENSE`](LICENSE). The Apache license does **not** grant a license to the preprint manuscript, its scholarly text, or third-party material. Copyright and redistribution of those materials remain subject to their respective terms. In particular, the preprint is separately deposited with its own record-level rights information.
