# GoN application candidate: identity-sensitive workflow recovery

**Status: specification and fixture only. NOT a real-world dataset, not a GROOVE comparison, not Q1 evidence.** This candidate is motivated by software workflow recovery, but the fixture is synthetic.

## Operational setting
A workflow has named services and directed dependency edges. A service is *usable* only if it is alive and every predecessor dependency is usable. A repair step may create a new service identity and install edges, or may rewire an existing dependency. Each step has a positive integer cost. The goal is to make a specified output service usable within budget, while preserving a forbidden-dependency invariant. The environment may impose identity-specific allowlists; thus quotienting by counts is generally unsound.

For the initial restricted fixture below, all services and available repair actions are explicitly known; therefore this is **ordinary finite deterministic planning**. It does not claim open-ended generativity.

## Exact fixture
Services: ingress (alive), auth (dead), report (alive).
Dependency: report requires auth.
Available actions:
- restart_auth: cost 3, changes auth to alive.
- create_auth_replacement: cost 2, creates distinct identity auth_v2 (alive) but does not rewire report.
- rewire_report: cost 1, requires auth_v2 to exist, removes report->auth and adds report->auth_v2.
Budget 3. Goal: report usable. Both restart_auth (cost 3) and create_auth_replacement+rewire_report (cost 3) are valid; the replacement alone does not solve the task. Forbidden edge ingress->report must remain absent.

## Why this is an adversarial gate
- A birth-only metric wrongly rewards create_auth_replacement even when the report remains unusable.
- Count-only abstraction cannot distinguish replacement from a dependency-correct repair.
- Standard graph rewriting can express the changes, so no novelty is inferred.

## Requirements before any publication claim
1. Obtain a genuine workflow/incident corpus with license, provenance and repeatable failure/recovery traces.
2. Encode the same semantics in GROOVE, with explicit typed graph rules and identity constraints; verify trace/goal equivalence, not just similar diagrams.
3. Compare the GoN candidate against GROOVE and an independent exact planner with identical budgets and hardware.
4. Pre-register a nontrivial, falsifiable claim before evaluating held-out instances.
5. If the task reduces to ordinary planning with no meaningful advantage, close the novelty gate.

References: https://groove.cs.utwente.nl/ and https://groove.cs.utwente.nl/manual.html .
