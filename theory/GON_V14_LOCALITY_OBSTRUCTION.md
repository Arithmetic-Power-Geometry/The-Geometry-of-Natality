# Geometry of Natality (GoN) V14 — locality obstruction under bounded observation

**Research status:** a precise separation for a deliberately restricted emulator class. No claim of original priority.

## Operational semantics
A birth system has a persistent visible root s and two actions: birth and query. Every birth creates a fresh persistent child of s and assigns it a globally unique identity. Query returns the number of distinct children of s. An emulator starts with root s and at most K latent child slots. It may reveal an unused slot on birth but may neither create new slots nor reuse an occupied slot while the child remains persistent. The observation channel includes the exact query response; action availability and cost are identical.

## Theorem 14.1 (query separation)
For every K>=0, the birth system and the K-slot revelation emulator are observationally distinguishable by a trace of K+1 births followed by query. The birth system returns K+1. The emulator can have at most K persistent distinct children and cannot return K+1 while preserving truthful query semantics.

Proof: induction on successful births yields K+1 distinct persistent children in the birth system. In the emulator the child set is a subset of K preinstalled slots. The query responses differ, or the emulator refuses an action that the birth system permits, which is itself an observable difference.

## Proposition 14.2 (tightness for finite horizon)
For any horizon T<=K, the emulator can reproduce all birth/query traces containing at most T births: reveal one unused child slot on each birth, and report the current count. Proof by induction on action history.

## Proposition 14.3 (bounded-window contrast)
If the query reports only the number of *currently active* children, children expire after w subsequent births, and the observer cannot compare expired identities, then K=w reusable child slots suffice for arbitrary birth sequences. This is V13's window abstraction in a rooted-graph action grammar.

## Limitation
Theorem 14.1 is an elementary capacity/pigeonhole argument and restates V12 in a graph-query language. Calling it a novel locality lower bound would be misleading: it relies on the number of persistent children, not on a sophisticated graph-locality barrier. The model does not yet prove a stronger result for local rewriting systems with unlimited hidden slots, bounded-memory controllers or expressive queries.

## Next nontrivial gate
Find a pair of systems with **equal latent capacity** and **equal total visible-state counts** whose observational behavior differs solely because of local rule constraints. Construct minimal counterexamples, then compare against graph rewriting, bisimulation and finite-state abstraction. Until then GoN remains foundational, not a validated Q1 contribution.
