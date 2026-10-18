"""Standard-library independent checks for the formal examples and axioms."""
import itertools
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from benchmark import reach

def gain(n,base,added):
    a=[set() for _ in range(n)]
    for u,v in base|added:a[u].add(v)
    before=[set() for _ in range(n)]
    for u,v in base:before[u].add(v)
    return len(reach(a,0))-len(reach(before,0))

def potential(n,base,k):
    missing=[(u,v) for u in range(n) for v in range(n) if u!=v and (u,v) not in base]
    return max((gain(n,base,set(edges)) for j in range(k+1) for edges in itertools.combinations(missing,j)),default=0)

class NatalityTests(unittest.TestCase):
    def test_distinguishing_pair(self):
        a={(1,2),(2,3),(3,4)}
        b={(1,2),(2,1),(3,4)}
        self.assertEqual(potential(5,a,1),4)
        self.assertEqual(potential(5,b,1),2)
        self.assertEqual(gain(5,a,set()),0)
    def test_non_submodularity(self):
        e1={(0,1)};e2={(1,2)}
        self.assertEqual((gain(3,set(),e1),gain(3,set(),e2),gain(3,set(),e1|e2)),(1,0,2))
    def test_exhaustive_n3(self):
        arcs=[(u,v) for u in range(3) for v in range(3) if u!=v]
        for bits in range(1<<len(arcs)):
            base={e for i,e in enumerate(arcs) if bits>>i&1}
            a=[set() for _ in range(3)]
            for u,v in base:a[u].add(v)
            r=reach(a,0)
            p1=potential(3,base,1)
            predicted=max((len(reach(a,v)) for v in range(3) if v not in r),default=0)
            self.assertEqual(p1,predicted)
            self.assertLessEqual(p1,3-len(r))
if __name__=='__main__':unittest.main()
