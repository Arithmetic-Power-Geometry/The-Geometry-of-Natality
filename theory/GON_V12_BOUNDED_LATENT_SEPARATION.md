# Geometry of Natality (GoN) V12: bounded-latent separation and capacity law

Status: exact resource separation under explicit assumptions. This is an elementary counting bound, NOT an established novel theorem.

## Setup
A birth process begins with n0 persistent, uniquely identified visible states. Over T steps, a legal birth action creates one globally fresh state, which remains visible. Its identity is included in the observable trace. The process admits a history of T consecutive successful births.

A *fixed-universe revelation emulator* begins with a preinstalled finite set U of N distinct persistent state identities, including the n0 initial visible states. Actions may reveal existing hidden states, but cannot add identities to U, reuse an identity for a different persistent state, or alter previously observed identities. An emulator must match the entire visible identity trace of the birth process for every allowed action history.

## Theorem 12.1 (capacity lower bound)
Any fixed-universe revelation emulator matching the T-birth history has N >= n0+T.
Proof: the birth history ends with n0+T simultaneously visible, pairwise distinct identities. An emulator's visible set is a subset of U. Thus |U| >= n0+T.

## Theorem 12.2 (tightness)
For the deterministic birth-only process that creates one new state per successful action, N=n0+T is sufficient to match every binary action history of length <=T.
Proof: preinstall T hidden identities, reveal the next unused identity on each successful birth action, and reveal nothing on a no-op. Identity and visibility traces match inductively. The bound is tight.

## Corollary 12.3 (unbounded-horizon separation)
No finite fixed-universe revelation emulator can reproduce all histories of an unbounded process that can repeatedly create fresh persistent identities.
Proof: for any finite N, choose T>N-n0 and invoke Theorem 12.1.

## Proposition 12.4 (resource tradeoff)
If a revelation emulator may add at most K new identities to its initial universe during execution, and starts with N states, then matching T births requires N+K >= n0+T. This counts *creation by the emulator* and no longer represents pure revelation. If each added identity has unit cost, the minimum such cost is max(0,n0+T-N), assuming sufficient available actions.

## Scope and pitfalls
1. This is a cardinality/identity resource theorem, not a computational complexity separation.
2. If old states can be deleted, identifiers recycled, identities hidden from observation, or only a bounded window is visible, the counting proof may fail.
3. The result concerns a specified class of fixed-universe revelation emulators; it does not show graph rewriting or generative systems are novel.
4. An emulator with an unbounded preinstalled universe can avoid the finite-capacity obstruction.
5. For finite horizon, the matching construction uses the same history-dependent reveal semantics as V11.

## Why it matters
V11 establishes trace indistinguishability without a latent-universe resource restriction. V12 pinpoints a sufficient resource assumption under which the equivalence fails. The distinction is operationally meaningful only if state identity and finite capacity are independently justified in an application.

## Research gate
Investigate nontrivial resource lower bounds for *local*, bounded-memory reveal grammars, with comparison against nominal automata, register automata, graph transformation and dynamic allocation semantics. Do not claim priority from elementary pigeonhole counting.
