"""GoN: state-equivalence falsification test for candidate natality signatures.

A *candidate signature* is valid for exact reachability only if states with
the same signature agree on goal reachability. This program constructs a
counterexample for the tempting summary (alive count, edge count, birth count).
This is a negative result for this candidate, not a GoN novelty theorem.
"""
from collections import deque
import json

def reachable_goal(alive, edges):
    # report can reach an alive dependency via directed edge
    return ('report','auth') in edges and 'auth' in alive

def summary(alive,edges,birth_count):
    return (len(alive),len(edges),birth_count)

def main():
    a={'alive':{'report','auth'},'edges':{('report','auth')},'birth_count':0}
    b={'alive':{'report','ingress'},'edges':{('report','auth')},'birth_count':0}
    assert summary(**a)==summary(**b)
    assert reachable_goal(a['alive'],a['edges']) is True
    assert reachable_goal(b['alive'],b['edges']) is False
    print(json.dumps({
      'candidate_signature':'(alive_count, edge_count, birth_count)',
      'same_signature':True,
      'goal_reachability_agrees':False,
      'conclusion':'candidate is not a sound exact quotient for this goal',
      'new_go_novelty':False,
      'groove_executed':False,
      'q1_ready':False
    },indent=2))
if __name__=='__main__':main()
