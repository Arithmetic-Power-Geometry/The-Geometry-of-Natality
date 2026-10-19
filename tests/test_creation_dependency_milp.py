import unittest
from experiments.research_gate.creation_dependency_milp import *
class Prompt12(unittest.TestCase):
    def test_negative_guard(self):
        self.assertIn("C3",counterexamples())
    def test_prerequisite_cost(self):
        p=Model(1,(Relay(frozenset(),5),Relay(frozenset({0}),1,frozenset({0})),Relay(frozenset({0}),3)),2)
        self.assertEqual(exhaustive(p)["cost"],3)
        self.assertEqual(external_milp(p)["cost"],3)
    def test_infeasible(self):
        p=Model(1,(Relay(frozenset({0}),1),),0)
        self.assertIsNone(exhaustive(p)["cost"])
        self.assertIsNone(external_milp(p)["cost"])
    def test_full_matched_sweep(self):
        r=sweep()
        self.assertEqual(r["checked"],4096)
        self.assertTrue(r["all_costs_match"])
if __name__=="__main__":unittest.main()
