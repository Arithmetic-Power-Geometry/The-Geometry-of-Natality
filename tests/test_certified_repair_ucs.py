"""Adversarial and exhaustive finite repair-planning checks."""
import itertools
import unittest
from experiments.research_gate.exact_orbit_key import UnsafeQuotient
from experiments.research_gate.certified_repair_ucs import (
    Grammar, start, actions, step, replay, search, exhaustive, cert, goal)
from experiments.research_gate.exact_orbit_key import canonical_key

class RepairUCSTests(unittest.TestCase):
    def test_matched_oracles_and_replay(self):
        cases=0
        for n,target,capacity,budget,create,rewire,restore in itertools.product(
            (1,2,3),(1,2),(1,2,3),(0,2,4,7),(0,1,2),(0,1),(0,2,4)):
            if target>n:continue
            g=Grammar(tuple("r"+str(i) for i in range(n)),create,rewire,
                      restore,target,capacity,budget)
            plain=search(g);quotient=search(g,True);oracle=exhaustive(g)
            self.assertEqual(plain["cost"],oracle["cost"])
            self.assertEqual(quotient["cost"],oracle["cost"])
            if quotient["cost"] is not None:
                replay(g,quotient["plan"],quotient["cost"])
                replay(g,plain["plan"],plain["cost"])
            cases+=1
        self.assertGreaterEqual(cases,500)

    def test_symmetric_state_reduction(self):
        g=Grammar(names=("a","b","c","d"),target=3,restore_cost=50)
        p=search(g);q=search(g,True)
        self.assertEqual(p["cost"],q["cost"])
        self.assertLessEqual(q["expanded"],p["expanded"])

    def test_non_equivariant_cost_refused(self):
        g=Grammar(identity_costs=(("replica_a",0),))
        with self.assertRaises(UnsafeQuotient):search(g,True)
        self.assertEqual(search(g)["cost"],exhaustive(g)["cost"])

    def test_non_equivariant_guard_refused(self):
        for g in (Grammar(fixed_preferred="replica_a"),
                  Grammar(opaque_guards=True)):
            with self.assertRaises(UnsafeQuotient):search(g,True)

    def test_zero_cost_and_ties(self):
        for g in (Grammar(create_cost=0,rewire_cost=0,restore_cost=0),
                  Grammar(create_cost=1,rewire_cost=1,restore_cost=2)):
            self.assertEqual(search(g)["cost"],search(g,True)["cost"])
            self.assertEqual(search(g)["cost"],exhaustive(g)["cost"])

    def test_capacity_and_budget(self):
        for g in (Grammar(target=2,capacity=1,budget=2,restore_cost=10),
                  Grammar(target=2,capacity=2,budget=0,restore_cost=10)):
            self.assertEqual(search(g)["cost"],exhaustive(g)["cost"])
            self.assertEqual(search(g,True)["cost"],exhaustive(g)["cost"])

    def test_negative_application_conditions(self):
        g=Grammar(names=("a","b"),capacity=1,restore_cost=10)
        s=start();a=("create",next(x[0][1] for x in actions(s,g) if x[0][0]=="create"))
        t=step(s,a,g)
        self.assertFalse(any(label[0]=="create" for label,_ in actions(t,g)))
        self.assertEqual(search(g)["cost"],search(g,True)["cost"])

    def test_history_canonicalized(self):
        g=Grammar(names=("a","b"))
        s=start()
        x=step(s,("create",next(a[0][1] for a in actions(s,g) if a[0][0]=="create")),g)
        y=step(s,("create",next(a[0][1] for a in actions(s,g) if a[0][0]=="create" and a[0][1]!=x.active[0])),g)
        self.assertEqual(canonical_key(x,cert(g)),canonical_key(y,cert(g)))

    def test_bad_replay(self):
        g=Grammar()
        with self.assertRaises(AssertionError):replay(g,(("rewire",),),1)
        with self.assertRaises(AssertionError):replay(g,(("restore",),),999)

if __name__=="__main__":unittest.main()
