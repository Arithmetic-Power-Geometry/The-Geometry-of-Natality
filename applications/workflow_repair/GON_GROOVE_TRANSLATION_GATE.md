# GoN — workflow-repair semantic translation gate (2026-10-18)

**Outcome: translation is straightforward at the conceptual rule level; NO ORIGINALITY ESTABLISHED.** This is a *translation specification*, NOT an executable GROOVE grammar or a measured solver comparison.

## Source model
The current synthetic fixture has service nodes ingress, auth, report; a directed dependency report -> auth; auth initially dead. Costs are positive and total budget is 3. Identity labels matter. The goal is report usable. The initial available actions are restart_auth (cost 3), create_auth_replacement (cost 2), and rewire_report (cost 1, after creation).

## Translation into standard typed graph rewriting
Represent each service as a node of type Service with stable string identifier and Boolean alive flag; a directed edge 'dependsOn' from dependent to prerequisite; a global control node with integer spent and Boolean flags done_restart, done_create, done_rewire. Represent action guards with positive matches and negative application conditions.

- **restart_auth**: guard auth exists, is dead, !done_restart, spent+3<=3; update auth.alive:=true, spent:=spent+3, done_restart:=true.
- **create_auth_replacement**: guard !exists Service[id='auth_v2'], !done_create, spent+2<=3; add Service[id='auth_v2', alive=true], spent:=spent+2, done_create:=true.
- **rewire_report**: guard done_create, !done_rewire, report dependsOn auth, auth_v2 exists, spent+1<=3; delete report->auth, add report->auth_v2, spent:=spent+1, done_rewire:=true.

All rules must also preserve the forbidden edge absence ingress->report. For this fixture no rule adds that edge.

**Goal predicate:** report.alive and every dependency target of report is alive. In this fixture there are no deeper chains after rewiring; for general graphs use reachability/fixed-point semantics and explicitly reject cycles or define a well-founded interpretation.

## Observable trace correspondence (paper specification)
Define a map T from GoN configurations to typed graphs encoding the exact named services, dependencies, action flags and cost. Each of the three GoN actions has a matching rewrite rule under T. Conversely every applicable rule corresponds to its named GoN action. Therefore (assuming faithful attribute/NAC encoding and no extra rules) labelled one-step transitions correspond and the finite traces correspond by induction. This is a **conditional specification-level correspondence**, NOT verified by executing GROOVE.

A successful trace of cost 3 is restart_auth. Another is create_auth_replacement followed by rewire_report. The creation action alone is not a successful repair.

## Why this matters
The restricted GoN workflow instance is naturally expressible in established attributed graph rewriting. It is **not** evidence that GoN has greater expressivity, improved asymptotic complexity, or a superior solver. To claim those would require an actual runnable .gps grammar, a checked bisimulation or trace-equivalence test, and paired benchmark measurements. None are yet available.

## External grounding
Official GROOVE homepage: https://groove.cs.utwente.nl/
Official manual (graphs and rules; attributes; control; exploration): https://groove.cs.utwente.nl/manual.html
Official example grammars: https://github.com/nl-utwente-groove/samples

## Stop/go verdict
- Formal application motivation: **synthetic only**.
- Translation to existing method: **straightforward, conditional**.
- Executable GROOVE baseline: **not yet produced or run**.
- Empirical improvement: **none demonstrated**.
- Originality gate: **FAIL for current formulation**.
- Q1-ready: **NO**.

**Do not create GoN V16 or repeat toy validations.** Before any new theory claim, acquire a real licensed incident corpus and implement/run a matched GROOVE grammar. If the equivalence remains and no substantial improvement appears, stop the Q1 algorithm-paper direction.
