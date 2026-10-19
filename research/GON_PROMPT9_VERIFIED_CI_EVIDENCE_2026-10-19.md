# Prompt 9 — verified independent audit and bounded rerun evidence
Date: 2026-10-19
Status: **CI PASS; original artifact independently checked; 1,440 isolated trials verified**

## GitHub verification
- Tested code SHA: `87b70d1f436b253b68c052750b1bc2d0b8caeb0e`
- Successful CI: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39208415337
- All job steps successful: compile and tests; retrieve original Prompt 8 artifact; independent original audit; isolated 20-repetition rerun; independent rerun audit; count/resource assertions; artifact upload.
- Artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39208415337/artifacts/12166458810
- Independently downloaded artifact ZIP SHA256: `39f19efbc53df88babddfe4866a83165775a441df60affed08073d086aaf63ef`, matching GitHub artifact metadata.
- Archive contents: `prompt8_independent_audit.json`, `prompt8_paired_differences.svg`, `prompt9_results.json`, `prompt9_independent_audit.json`, `prompt9_paired_differences.svg`.

## Original artifact audit
- Original Prompt 8 ZIP checksum independently matched `94c9c582933ab68b5031bd2e1a5501273d64b0a2c7fda8c5394a1b17e285ac8c`.
- Original raw JSON: 36 matched cells, 36 negative controls, 1,440 successful unique trials; no duplicate (instance,algorithm,repetition) keys.
- Original 36 median paired differences independently recomputed; maximum discrepancy 0 seconds.
- Frozen manifest content hash: `6684f407eb332d9ed4a87799177c286c04636fdd85445b350adea675ca567e84`.

## Isolated resource-limited rerun
- 36 matched cells, 36 refusal cells, 1,440 measured trials, **1,440 successful, 0 censored**.
- 60-second `subprocess.run` timeout per trial; Linux `RLIMIT_AS=2*1024**3` (2 GiB virtual address-space cap); process exit code recorded; process launch time recorded separately from in-process solver timing.
- 3 warmups, 20 paired measured repetitions per algorithm per matched instance. Replayed plans and checked exact independent oracle costs before timing. Frozen generator and compatibility unchanged.
- Independent audit confirms all expected trial keys, costs, status and pairing.

## Recalculated descriptive median paired differences
Sign: first algorithm minus second algorithm, median over nine instance-level medians per stratum.

| Stratum | Original Prompt 8 | Isolated Prompt 9 | First vs second |
|---|---:|---:|---|
| fresh_symmetric | -3.442 ms | **-3.851 ms** | plain UCS vs quotient UCS |
| independent | +0.344 ms | **+0.743 ms** | full UCS vs decomposition |
| history_local | +0.359 ms | **+0.740 ms** | full UCS vs decomposition |
| negative_local | +0.193 ms | **+0.427 ms** | full UCS vs decomposition |

A negative value indicates the second algorithm is slower. A positive value indicates it is faster. These are synthetic small-instance, CI-host descriptive comparisons. Do not interpret their magnitude as externally valid speedups.

## Integrity and limits
- Results JSON contains all raw measurements, pairwise median/IQR/bootstrap uncertainty and environmental metadata; SVG figures are derived from independently audited JSON.
- Memory cap is address-space, not RSS; `tracemalloc` peak is Python allocation, not process memory.
- Bootstrap resampling of within-instance trials does not support inference over unseen graph topologies.
- No matched GROOVE baseline, operational network traces, general coupled graph interpreter, larger benchmark or novel structural theorem.
- Prompt 9 experimental reproducibility gate **PASSED**; selective-Q1 manuscript readiness **NOT established**.

## Prompt 10 readiness
Perform a manuscript claim-to-evidence reconciliation, formal assumption audit, independent reference verification and submission-package build. The manuscript must explicitly report quotient slowdown, conservative decomposition scope, absence of matched external baselines and unresolved originality. Do not manufacture novelty or upgrade exploratory CI timings into general performance claims.
