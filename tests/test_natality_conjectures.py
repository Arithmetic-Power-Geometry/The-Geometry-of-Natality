import unittest
from itertools import product
from experiments.research_gate.natality_conjectures import (
    brute,greedy,search_counterexamples,proof_witness)
class ConjectureTests(unittest.TestCase):
    def test_counterexample_ledger(self):
        d=search_counterexamples()
        self.assertIsNotNone(d["failures"]["H1"])
        self.assertIsNotNone(d["failures"]["H2"])
        self.assertIsNone(d["failures"]["H3"])
    def test_theorem_three_exhaustive(self):
        for n in (1,2,3):
            for entries in product(product(range(3),repeat=3),repeat=n):
                for k in range(n+1):
                    self.assertEqual(proof_witness(entries,k),brute(entries,k)[0])
    def test_strict_capacity_gap(self):
        x=((1,2,1),(1,2,1))
        self.assertEqual(brute(x,1)[0],4)
        self.assertEqual(greedy(x,1)[0],4)
    def test_heterogeneous_savings(self):
        x=((2,3,3),(1,1,1))
        self.assertEqual(greedy(x,1)[0],4)
if __name__=="__main__":unittest.main()
