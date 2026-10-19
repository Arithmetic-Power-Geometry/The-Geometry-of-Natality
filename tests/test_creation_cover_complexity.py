import unittest
from experiments.research_gate.creation_cover_complexity import (
    Template,Instance,exhaustive_graph,subset_dp,greedy_newly_covered,
    installed_graph,reached_by_graph,ledger,sweep)
class CreationCoverTests(unittest.TestCase):
    def test_explicit_graph_semantics(self):
        p=Instance(2,(Template(frozenset({0,1}),3),))
        v,e=installed_graph(p,(0,))
        self.assertEqual(len(v),4)
        self.assertEqual(len(e),3)
        self.assertTrue(reached_by_graph(p,(0,)))
        self.assertFalse(reached_by_graph(p,()))
    def test_falsification_ledger(self):
        d=ledger()
        self.assertEqual(d["H1"]["heuristic_cost"],2)
        self.assertEqual(d["H1"]["optimal_cost"],1)
        self.assertEqual(d["H2"]["status"],"false")
        self.assertEqual(d["H3"]["status"],"true_conditional_standard")
    def test_complete_finite_search(self):
        r=sweep()
        self.assertEqual(r["checked"],9261)
        self.assertEqual(r["status"],"exact_match")
    def test_unreachable_and_zero(self):
        p=Instance(2,(Template(frozenset({0}),0),))
        self.assertIsNone(exhaustive_graph(p)["cost"])
        self.assertIsNone(subset_dp(p)["cost"])
    def test_overlapping_cover(self):
        p=Instance(3,(Template(frozenset({0,1}),1),
                      Template(frozenset({1,2}),1),
                      Template(frozenset({0,2}),5)))
        self.assertEqual(exhaustive_graph(p)["cost"],2)
        self.assertEqual(subset_dp(p)["cost"],2)
if __name__=="__main__":unittest.main()
