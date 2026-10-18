# Geometry of Natality (GoN) V10: revealed possibilities, identifiability, and fair comparisons
Status: candidate research model, not a claim of new priority.

## Definition: a revelation process
At step t an agent knows an observed rooted state system O_t and action catalogue A_t. A selected admissible action a_t may (i) create new states, (ii) add edges, (iii) reveal previously unobserved states or actions, or (iv) combine these. All observations and state identities must be explicit. The observation map h_t from a hidden environment H to O_t distinguishes *revelation* (pre-existing hidden states become known) from *creation* (states do not exist before the intervention). The agent pays a stated cost and chooses actions adaptively using observed history. The objective is realized reachable reward by budget B, with an explicit policy and information filtration.

## V10 Theorem 1: indistinguishability obstruction
Suppose two hidden environments H0,H1 induce exactly the same observations and available actions through a common history, but one action a yields reward 1 only in H0 while another action b yields reward 1 only in H1. A deterministic policy with one remaining action must choose the same action in both environments, hence obtains zero reward on at least one, whereas a clairvoyant policy obtains one in each.
Proof: the policy's decision is a function of identical histories. Its selected action is a or b in both worlds; choose the world in which that action has zero payoff.
This is a standard indistinguishability/no-free-lunch argument; not independently novel.

## V10 Theorem 2: randomized minimax
Under the symmetric two-world construction, any randomized policy with one remaining action has worst-case expected reward at most 1/2. The uniform random choice achieves 1/2.
Proof: if a is chosen with probability p, expected reward is p in H0 and 1-p in H1. min(p,1-p)<=1/2, equality at p=1/2.
This is classical minimax reasoning, not independently novel.

## V10 Theorem 3: information resolves ambiguity
If an observation before choice distinguishes H0 from H1 without consuming the action budget, there exists a policy that selects the corresponding rewarded action and obtains reward 1 in either world. Proof: branch on observed world.
This quantifies the value of information in the toy model but does not establish an original algorithm.

## Evaluation contract
A fair comparison must give every adaptive baseline the same observation channel, action budget and information access. Comparing GoN against an offline solver that has less or more information without disclosure is invalid. A clairvoyant offline optimum is an upper bound, not a directly comparable online algorithm.

## Critical boundary
Online graph exploration usually optimizes travel cost while discovering a fixed unknown graph. GoN must specify when actions *actually create* vertices rather than merely discover hidden existing vertices; otherwise the models may coincide. Graph rewriting, online planning, active learning and adaptive stochastic optimization are necessary additional baselines.

## Open original targets
1. A structural invariant separating birth and revelation under observable traces.
2. A sharp regret or competitive bound for a restricted generative action grammar that is not inherited from known online exploration.
3. A practical task where creation-vs-revelation matters and a matched baseline comparison shows reproducible gains.
