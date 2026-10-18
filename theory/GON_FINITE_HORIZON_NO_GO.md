# GoN finite-horizon no-go: action-type creation alone does not establish expressivity

**Decision: NEGATIVE NOVELTY GATE. Do not label this V16.**

## Question
Can a finite-horizon system that creates new action *types* be shown more expressive than ordinary transition systems merely because the action catalogue changes?

## Precise setup
A finite branching, finitely described generative operational semantics has configurations c, an initial c0, an effective transition relation c --a--> c', and a finite bound H on the number of transitions. Configurations may contain graphs, created vertices, and rewrite rules that themselves create or delete rule schemas. The rule catalogue is part of the configuration. Assume the set of configurations reachable in <=H steps is finite (e.g. each step has finitely many successors, with finite branching from c0). Let observations be any deterministic function o(c,a,c') of a transition; the observable alphabet may be infinite but the reachable H-truncated transition graph is finite.

## Theorem (finite-horizon compilation)
Every such generative system has an ordinary finite labelled transition system whose observable traces through H steps are exactly those of the original system.

**Construction.** Breadth-first enumerate all configurations reachable from c0 in <=H steps, retaining distinct configurations and their transition labels. Add a depth coordinate to states: (c,d), 0<=d<=H. For each generative step c --a--> c', add ((c,d), o(c,a,c'), (c',d+1)) for d<H. The initial state is (c0,0). This graph is finite by finite branching and H. Induction on d gives a trace-preserving bijection between original executions and compiled paths when transitions are kept with multiplicity; the trace *sets* agree without that qualification.

## Consequences
1. New action-type generation does not by itself evade finite-state compilation for bounded horizons.
2. Compilation can be exponentially or worse larger than a compact generative description. This theorem says nothing about succinctness, runtime, memory, decidability at unbounded horizon, or equivalence to a *particular* restricted planning language.
3. Unbounded branching, noncomputable transition relations, or unbounded horizons invalidate this finite-enumeration conclusion.
4. The result is standard state-space unfolding, not a GoN originality claim.
5. The correct research direction is a provable succinctness/complexity separation for an explicit restricted model, or an empirically meaningful planner with matched baselines, not the mere existence of new rule types.

## Adversarial witness
A two-step system starts with one action 'invent'. Executing it installs a new action type 'use', which was absent initially; 'use' then reaches a terminal state. Its trace language through horizon 2 is {empty, invent, invent/use} (prefix closed). An ordinary three-state LTS reproduces the traces exactly. This refutes the assertion that 'new action type' implies non-compilability.

## Q1 gate
NO. The research hypothesis 'GoN is original because new actions can emerge' fails this finite-horizon expressivity test. A more specific resource-bounded question must be formulated before further claims.
