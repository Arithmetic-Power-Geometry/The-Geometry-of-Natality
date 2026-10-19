import unittest
from experiments.research_gate.dynamic_repair_p13 import *
class DynamicRepair(unittest.TestCase):
    def test_history_no_reuse(self):
        p=Problem(1,1,1)
        s=State(frozenset(),frozenset(),frozenset({0}))
        self.assertEqual(list(actions(p,s)),[])
    def test_action_time_nac(self):
        p=Problem(2,1,2,forbid_pair=(0,1))
        s=State(frozenset({0}),frozenset(),frozenset({0}))
        self.assertFalse(any(a[0]=="create" for a,_,_ in actions(p,s)))
    def test_deletion_retains_history(self):
        p=Problem(1,1,1)
        s=State(frozenset({0}),frozenset({(0,0)}),frozenset({0}))
        deleted=[ns for a,ns,c in actions(p,s) if a[0]=="delete"]
        self.assertEqual(deleted[0].used,frozenset({0}))
        self.assertEqual(deleted[0].links,frozenset())
    def test_independent_external_solver(self):
        p=Problem(2,2,1)
        self.assertEqual(dijkstra(p)["cost"],3)
        self.assertEqual(independent_graph(p)["cost"],3)
    def test_sweep(self):
        d=sweep()
        self.assertTrue(d["matched"])
        self.assertGreater(d["checked"],100)
if __name__=="__main__":unittest.main()
