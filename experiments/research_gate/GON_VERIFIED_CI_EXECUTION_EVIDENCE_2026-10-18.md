# GoN independently observed CI execution evidence — 2026-10-18

**Observed directly via GitHub Actions API and job logs.** This document records completed experiments, not an experiment proposal.

## GROOVE binary smoke test
- Workflow: [run 39145685509](https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39145685509)
- Job: 117728919744
- Conclusion: **success**.
- Official release download step: **success**.
- Official `Generator.jar -h` step: **success**.
- Raw evidence artifact: [12142894171](https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39145685509/artifacts/12142894171).
- Interpretation: GROOVE can run in GitHub CI. **Not** a GoN grammar run or matched benchmark.

## GoN exact-oracle regression
- Workflow: [run 39147296943](https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39147296943)
- Job: 117733620442
- Conclusion: **success**.
- Independent-oracle comparison step: **success**.
- Raw evidence artifact: [12143439702](https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39147296943/artifacts/12143439702).
- Interpretation: the two synthetic-fixture oracles agree on their expected plan sets; this is not external validation.

## Research decision
**GoN Q1-ready: NO.** GROOVE installation and internal correctness are no longer untested assumptions. Remaining decisive gate: an *executed* matched GoN-vs-GROOVE grammar benchmark, with raw traces, baseline methods and real workload. Do not claim a speedup or mathematical novelty from these two successful smoke/regression runs.

## Reproducibility links
- GROOVE official source: https://github.com/nl-utwente-groove/code
- GROOVE official sample grammars: https://github.com/nl-utwente-groove/samples
