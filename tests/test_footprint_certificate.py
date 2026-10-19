import itertools
import unittest
from experiments.research_gate.footprint_certificate import (
    Component,Problem,certificate,footprint,full_ucs,decomposed,
    replay,coupling_counterexample)

class FootprintTests(unittest.TestCase):
    def test_exhaustive_matched_optimality(self):
        cases=0
        for n in (1,2,3):
            for restart,create,rewire,budget,ban in itertools.product(
                (0,2,4),(0,1),(0,2),(0,2,5,15),(False,True)):
                p=Problem(tuple(Component(restart=restart+i%2,
                         create=create,rewire=rewire,forbid_restart=ban)
                         for i in range(n)),budget=budget)
                c=certificate(p)
                self.assertTrue(c["certified"],c["reasons"])
                d=decomposed(p);f=full_ucs(p)
                self.assertEqual(d["cost"],f["cost"])
                if d["cost"] is not None:
                    self.assertEqual(replay(p,d["plan"]),d["cost"])
                cases+=1
        self.assertEqual(cases,3*3*2*2*4*2)

    def test_footprints_local_and_history(self):
        p=Problem((Component(),Component()))
        a=footprint(p,0,"rewire")
        b=footprint(p,1,"create")
        self.assertIn("c:0:history",a.guards)
        self.assertFalse(a.writes & (b.reads|b.writes|b.guards))
        self.assertIn("c:1:identity",b.allocations)

    def test_refuse_coupling(self):
        base=(Component(),Component())
        for kwargs in (dict(shared_restart_limit=1),dict(cross_edges=((0,1),)),
                       dict(global_history_guard=True),dict(shared_allocation=True),
                       dict(opaque_guard=True),dict(global_negative_condition=True)):
            p=Problem(base,**kwargs)
            self.assertFalse(certificate(p)["certified"])
            self.assertFalse(decomposed(p)["certified"])

    def test_counterexample_strict_cost_gap(self):
        c=coupling_counterexample()
        self.assertEqual(c["global_optimal_cost"],4)
        self.assertLess(c["local_unconstrained_cost"],c["global_optimal_cost"])
        self.assertTrue(c["unsafe_plan_rejected"])

    def test_local_negative_guard_and_unreachable(self):
        p=Problem((Component(forbid_restart=True,forbid_create=True),))
        self.assertIsNone(decomposed(p)["cost"])
        self.assertIsNone(full_ucs(p)["cost"])
        p=Problem((Component(forbid_restart=True,create=0,rewire=0,
                             require_create_history=True),))
        self.assertEqual(decomposed(p)["cost"],0)
        self.assertEqual(full_ucs(p)["cost"],0)

if __name__=="__main__":unittest.main()
