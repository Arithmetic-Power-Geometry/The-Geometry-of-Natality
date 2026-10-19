# Prompt 2 — exact finite orbit key (research-stage implementation)

## Mathematical contract
A state consists of six multisets of typed records: active nodes, edges,
action history, attributes (including identity-specific costs), forbidden
conditions, and resource constraints. Identity occurrences MUST be wrapped
in `Ref`. Fixed identities are never permuted. Fresh identities are partitioned
into disjoint complete role pools. The acting group is the direct product of
symmetric groups on those pools, including unallocated fresh identities.
The action is simultaneous substitution of each `Ref` in every state field.

For a fixed certified group, define `E_g(s)` as the sorted tuple encoding
after applying permutation `g`, and `K(s)=min_g E_g(s)`. Then
`K(s)=K(t)` iff there exists a group element `g` with `g(s)=t`.
Proof: if equal, choose minimizers `g,h`; then `t=h^{-1}g(s)`.
The converse follows because group action permutes the same orbit.
This is a standard finite-group canonicalization fact, not novel theory.

## Important soundness boundary
`Certificate` is an explicit trusted assertion, not an automatic verification
of arbitrary transition/goal/cost Python code. The module refuses absent
certifications and opaque data but cannot detect a lying certificate, hidden
global state, or unmodeled external identity-sensitive semantics.
Only use quotient UCS after proving transition, goal, cost, constraints and
allocation equivariance for the concrete declarative action grammar.
This stage is an exact orbit-key oracle, NOT a certified quotient planner.

## Tests and negative controls
`tests/test_exact_orbit_key.py` checks exhaustive iff-orbit over 64 small
states (4096 ordered pairs), symmetry/reflexivity/transitivity, simultaneous
renaming of action history and negative conditions, fixed identities, distinct
roles, identity-specific costs, guards, shared resource values, unsupported
objects, oversized pools and missing certification flags.
CI is configured on branch and path changes; check the GitHub Actions run
before declaring remote verification success.

## Limits
Maximum eight fresh names by default; factorial runtime; all state fields
must be tuple records with `Ref` identities; certificate flags are assumptions.
No state-space speedup, novelty or real-world claim follows from this test.
The older `fresh_name_quotient_prototype.py` remains historical and is not
used as a verified Algorithm 4. Its literal backslash-n syntax error should
be repaired or explicitly deprecated in a separate compatibility change.

## Prompt 3 prerequisites
Define a closed declarative action grammar with explicit equivariance proof;
then integrate quotient UCS, concrete representative plan reconstruction,
full replay, and matched ordinary UCS. Add counterexamples where the grammar
is not equivariant. Report state expansions, generated states, canonicalization
cost and memory on identical instances.
