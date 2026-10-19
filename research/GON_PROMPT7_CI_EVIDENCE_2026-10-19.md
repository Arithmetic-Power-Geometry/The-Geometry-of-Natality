# Prompt 7 — frozen benchmark CI evidence
Date: 2026-10-19

- CI workflow: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39207045536
- Tested commit: `ac8e21250f9a6351a450138c5bfaec9a5e7b27c4`
- GitHub Actions jobs API: **completed SUCCESS**. Compilation, deterministic/mutation tests, JSON export and artifact upload all succeeded.
- Manifest artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39207045536/artifacts/12165579625
- GitHub-reported artifact SHA256: `a8254cde104d0155710b7a10f884dda47d9f4d51d2a1e9b81f991555db9f444c`
- 72 synthetic instance records: 8 strata x 3 seeds x 3 sizes.
- Generator `experiments/research_gate/benchmark_v1.py`; tests `tests/test_benchmark_v1.py`.
- Protocol `research/GON_PROMPT7_FROZEN_BENCHMARK_PROTOCOL_2026-10-19.md`.
- **No main comparative experiment was executed**. No external network logs or matched GROOVE baseline. This CI validates manifest reproducibility and compatibility annotations only.
- The CI artifact is an exported JSON snapshot. GitHub artifact SHA256 is the ZIP archive digest, not necessarily the internal JSON manifest SHA256; use the `manifest_sha256` field for JSON content identity.
- Next step: Prompt 8 implements runner against the frozen cells without changing the generator.
