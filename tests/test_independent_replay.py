import unittest
from experiments.research_gate.certified_repair_ucs import Grammar,search
from experiments.research_gate.independent_replay import verify

class IndependentReplayTests(unittest.TestCase):
    def test_all_reported_plans(self):
        for n in range(1,5):
            for target in range(1,min(n,3)+1):
                for cost in (0,1,3):
                    g=Grammar(names=tuple("r"+str(i) for i in range(n)),
                              target=target,restore_cost=cost,budget=12)
                    for quotient in (False,True):
                        result=search(g,quotient)
                        self.assertIsNotNone(result["cost"])
                        self.assertEqual(verify(g,result["plan"],result["cost"])["cost"],result["cost"])
    def test_corrupt_plan_rejected(self):
        g=Grammar()
        for plan,cost in [((("rewire",),),1),((("restore",),),2),
                          ((("restore",),("restore",)),6)]:
            with self.assertRaises(AssertionError):verify(g,plan,cost)

if __name__=="__main__":unittest.main()
