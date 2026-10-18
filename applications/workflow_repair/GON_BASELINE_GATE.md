# GoN application — independent oracle audit and honest comparison gate

Independent exhaustive Python enumeration of all 16 permutations of 0–3 distinct actions, 2026-10-18. Results: 4 valid sequences, 2 successful sequences, minimum cost 3, 0 failed assertions. The two successful plans are (restart_auth) and (create_auth_replacement, rewire_report). The replacement alone is not sufficient. See independent_audit.py and independent_audit_results.json.

This validates only the **synthetic fixture**, not the general solver, a novel mathematical model, or real-world efficacy.

**GROOVE status: NOT RUN.** GROOVE already supports graph rewriting, attribute handling, rule controls, state-space exploration, isomorphism detection, and model checking (https://groove.cs.utwente.nl/ and https://groove.cs.utwente.nl/manual.html). A fair comparison requires an actual executable GROOVE grammar with semantically matched rules, goals, costs and identity constraints. Do not report benchmark wins without executing that baseline.

**Research decision:** no Q1-level contribution established; do not add another numbered version. The next meaningful step requires a real incident dataset with provenance and a runnable GROOVE encoding. If no genuine novelty survives the comparison, stop the algorithmic paper claim.
