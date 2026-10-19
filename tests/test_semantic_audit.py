import unittest
from experiments.research_gate.semantic_audit import (
    audit,reference_successors,reachable,counterexample_non_equivariant)
from experiments.research_gate.certified_repair_ucs import Grammar,search
from experiments.research_gate.exact_orbit_key import UnsafeQuotient

class SemanticAuditTests(unittest.TestCase):
    def test_exhaustive_transition_commutation(self):
        for n in range(1,4):
            for capacity in range(n+1):
                g=Grammar(names=tuple("r"+str(i) for i in range(n)),
                          capacity=capacity,target=min(n,2),restore_cost=9)
                result=audit(g)
                self.assertGreater(result["state_permutation_checks"],0)

    def test_zero_cost_and_unreachable(self):
        for g in (
            Grammar(names=("a","b"),create_cost=0,rewire_cost=0,
                    restore_cost=0,target=2),
            Grammar(names=("a","b"),create_cost=0,rewire_cost=0,
                    restore_cost=9,target=2,capacity=1,budget=0),
            Grammar(names=("a","b"),create_cost=1,rewire_cost=0,
                    restore_cost=9,target=2,capacity=2,budget=2)):
            self.assertEqual(audit(g)["plain_cost"],audit(g)["quotient_cost"])

    def test_name_sensitive_counterexample_and_refusal(self):
        witness=counterexample_non_equivariant()
        self.assertEqual(witness["names"],2)
        self.assertNotEqual(witness["cost_a"],witness["cost_b"])
        for g in (Grammar(identity_costs=(("replica_a",0),)),
                  Grammar(fixed_preferred="replica_a"),
                  Grammar(opaque_guards=True)):
            with self.assertRaises(UnsafeQuotient):
                search(g,True)

    def test_independent_reference_has_expected_edges(self):
        g=Grammar(names=("a",),capacity=1)
        states,edges=reachable(g)
        self.assertGreaterEqual(len(states),4)
        self.assertGreater(edges,0)

if __name__=="__main__":unittest.main()
