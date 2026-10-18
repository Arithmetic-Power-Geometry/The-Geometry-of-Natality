# GoN V11 — observational equivalence and the limits of detecting birth

Status: formal identification result and baseline comparison; novelty NOT established.

## Model
A hidden finite-state environment is observed through a history of visible labels and action outcomes. Two semantics are considered:
(B) a fresh state is created only when a birth action is executed;
(R) the same labelled state exists beforehand but is initially hidden, and an action reveals it.
An observation trace records available action labels, visible states, visible transitions, rewards and costs, but NOT a trusted ontological birth certificate. A policy is any (possibly randomized) function of prior observed traces. Environments use matching action labels, costs, observations and rewards.

## Theorem 11.1 (birth/revelation nonidentifiability)
For every finite deterministic monotone birth-only execution tree with finitely many possible states and actions, there exists a revelation-only environment with a fixed hidden universe that produces exactly the same observable trace for every adaptive policy, provided observations reveal only currently visible states and enabled actions and the fixed environment can conceal latent states until their associated birth step.

Proof: take the finite union U of all state identities occurring anywhere in the finite birth execution tree (use history-qualified identities if necessary). Preinstall U as hidden states. For each history h, make visible exactly the identities visible at h in the birth model, and enable the same actions. Each transition in the revelation model reveals the states the birth model would create, with identical observable edges, rewards and costs. Induction on trace length establishes equality of observations after every matching action. Thus every deterministic policy has identical trace; coupling the random choices proves equality for randomized policies.

**Boundary:** This construction may require history-dependent reveal rules and a fixed preinstalled catalogue of all potential histories. It does NOT imply equivalence under a restricted local graph-rewriting grammar, an unbounded generative process, physical creation sensors, or a bounded latent-universe assumption.

## Corollary 11.2 (no trace-only test)
Under the model assumptions, no test using only the observable trace can distinguish whether a newly visible state was born or merely revealed, even with arbitrary adaptive action choice. Proof: identical trace distributions imply identical test-output distributions.

## Proposition 11.3 (identification with trusted certificates)
If every newly visible state carries a trusted, sound and complete birth-vs-revelation certificate, the distinction becomes observable. Proof: read the certificate. This is an information assumption, not an algorithmic advance.

## Falsification targets
- Restrict revelation to memoryless local graph rules; seek a smallest birth process without equivalent reveal process.
- Require bounded hidden-universe cardinality independent of action horizon; seek a lower bound.
- Study partially observed unbounded creation with a specified generative grammar and compare against established rewriting and adaptive planning.

## Related work
Graph rewriting already handles creation and rule composition: Kosiol and Taentzer (2023), DOI 10.1016/j.jlamp.2022.100820.
Adaptive stochastic optimization handles partial observations: Golovin and Krause (2011), DOI 10.1613/JAIR.3278.
These sources make it inappropriate to claim that graph creation or adaptive observation is new. The trace-equivalence construction is elementary and its priority has NOT been checked exhaustively.
