# Geometry of Natality (GoN) V13 — Observation-memory frontier

Status: exact finite-model result; classical register reuse/capacity phenomenon, not established original research.

## Motivation
V12 proves that persistent globally identifiable states require n0+T distinct latent identities to emulate T births. The premise matters. Here the observation channel remembers only a moving window of w newly born states, and permits recycling identifiers after they leave that window.

## Model
At each successful birth step t a new state is created and receives a globally unique *true* identity z_t. An observer sees only the most recent min(w,t) live states, with equality tests among currently visible identities. On expiry a state disappears permanently from the visible world. There is no trusted record of its old identifier, and no action can access an expired state. A revelation emulator has N reusable slots. On a successful action it allocates an unused slot, reveals it, and retires the slot for the state leaving the window. A trace is a sequence of visible equality patterns, not raw globally stable identifiers. The initial persistent states are excluded from the window and need n0 permanently reserved slots.

## Theorem 13.1 (sharp active-width bound)
For T successful births, a revelation emulator reproduces all equality-pattern traces if and only if it has at least n0+min(w,T) slots, assuming n0 persistent initially visible states and that every live new state is distinguishable from every other live state and the persistent states.

Necessity: at step min(w,T), n0+min(w,T) distinct states are simultaneously visible and require distinct slots. Sufficiency: reserve n0 persistent slots; use a ring of min(w,T) slots for births, reusing each slot only after the previous occupant has expired. Equality patterns of simultaneously visible states match exactly.

## Corollary 13.2 (finite-memory collapse)
For fixed w, arbitrarily many births can be simulated with n0+w reusable slots, if observation cannot link expired identities to new identities. Thus the unbounded-horizon impossibility of V12 does not survive this change of observation semantics.

## Theorem 13.3 (trusted lifetime identifiers restore the V12 bound)
If the observer can query equality of a new state's identifier against every identifier seen at any prior time and the emulator cannot alter identifiers, the T births require n0+T globally distinct slots. Proof: any reuse produces a detectable repeated identifier, contradicting the birth trace.

## Important qualification
A reusable-slot emulator is NOT a fixed persistent-state revelation emulator under V12 assumptions. Slot recycling changes the model. Equality-pattern observations quotient away global identity; raw integer-labelled traces do not coincide when a slot is reused. This is a theorem about *observation resources*, not a proof that genuine creation equals revelation in every semantics.

## Publication priority
The ring-slot construction is elementary and resembles register allocation, nominal automata and bounded-memory state abstraction. Do not claim novelty without a detailed formal-language and graph-transformation prior-art audit. The contribution here is a precise, testable boundary between V12 and V13.
