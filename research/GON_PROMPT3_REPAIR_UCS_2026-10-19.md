# Prompt 3 — certified finite repair UCS and concrete replay

Date: 2026-10-19. Research-stage evidence; no claim of Q1 novelty.

## Implemented grammar
`experiments/research_gate/certified_repair_ucs.py` defines a closed finite grammar with:
- a fixed service and one exchangeable role pool of up to eight fresh replica identities;
- creation of an unused replica, rewiring from fixed service to an active replica, or restoring the fixed service;
- nonnegative integer per-operation costs, global capacity, cumulative cost budget, and goal (restore or at least target wired replicas);
- used-action history retained as identity-bearing records, even though the grammar's current applicability rules do not consume that history;
- explicit negative application conditions: no duplicate create, no duplicate rewire, no create past capacity;
- uniform costs and no name-dependent guards in quotient mode. Identity-specific costs and fixed-name preferences may be run by ordinary UCS, but quotient mode refuses them. Opaque guard flags also cause refusal.

The `cert(g)` flags are supported by inspection of this closed grammar, not by certification of arbitrary callbacks. `step` enumerates all names in the complete role pool and applies uniform rules. Renaming commutes with each operation, preserves costs, capacity and goal. Initial state is invariant. A feasible path is therefore mapped to a same-cost feasible path. Finite Dijkstra/UCS on exact orbits preserves optimal cost.

## Algorithm and replay
Plain UCS uses full typed `State` keys. Quotient UCS uses Prompt 2 `canonical_key`. Queue items retain concrete state and complete action trace; an orbit's accepted representative is always the one actually expanded, so the stored concrete plan can be replayed without composing arbitrary representative action labels. On goal return, `replay` independently executes the plan from the initial state, checks applicability, cumulative budget and final goal, and verifies cost. Zero-cost actions are safe because relaxations require strictly lower distance and the finite graph has finite actions.

An independent depth-first full trace enumeration `exhaustive` checks small instances. This is not an independent external planner or matched GROOVE baseline.

## Test matrix
`tests/test_certified_repair_ucs.py` checks matched plain UCS, orbit UCS, exhaustive costs; plan replay; zero costs/ties; capacity/budget; history renaming; negative conditions; identity-specific cost and fixed-name/opaque-guard refusal. The Cartesian product varies n=1..3, target=1..2, capacity=1..3, budgets 0/2/4/7, creation cost 0/1/2, rewiring cost 0/1 and restoration cost 0/2/4. Excludes target>n.

## Limitations
- One role pool and restricted declarative grammar only; not a general graph rewriting language.
- No identity-dependent resource policies, global arbitrary guards or dynamic grammar discovery.
- Prompt 2 canonicalization is factorial in role-pool size and limited to eight fresh identities.
- No established symmetry baseline, no matched GROOVE grammar, no real dependency network.
- The standard symmetry reduction proof is not a new GoN theorem.
- Counts of expansions, generated successors, distinct keys, canonicalization calls, wall time and peak Python-traced memory are instrumented, but any speedup must be measured, not presumed.
- For multi-run timing uncertainty, matched benchmark protocol and independent baseline, use Prompt 4/8; single demonstration is not a publication performance claim.

## Reproduce
```bash
python -m py_compile experiments/research_gate/certified_repair_ucs.py tests/test_certified_repair_ucs.py
python -m unittest discover -s tests -p test_certified_repair_ucs.py -v
python -m experiments.research_gate.certified_repair_ucs
```
CI workflow: `.github/workflows/gon-certified-repair-ucs.yml`. Check actual run conclusion; source presence alone is not successful CI.
