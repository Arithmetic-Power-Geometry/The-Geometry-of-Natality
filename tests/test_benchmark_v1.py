import copy,unittest
from experiments.research_gate.benchmark_v1 import (
    manifest,verify,make,STRATA,SEEDS,digest)
class FrozenBenchmarkTests(unittest.TestCase):
    def test_reproducibility(self):
        a=manifest();b=manifest()
        self.assertEqual(a,b)
        self.assertTrue(verify(a))
        self.assertEqual(len(a["instances"]),72)
    def test_mutation_detected(self):
        a=manifest()
        a["instances"][0]["instance"]["problem"]["budget"]=999
        with self.assertRaises(AssertionError):verify(a)
    def test_strata_and_seeds(self):
        a=manifest()
        self.assertEqual(set(x["stratum"] for x in a["instances"]),set(STRATA))
        self.assertEqual(set(x["seed"] for x in a["instances"]),set(SEEDS))
        self.assertEqual(len(set(x["instance_sha256"] for x in a["instances"])),72)
    def test_negative_compatibility(self):
        for row in manifest()["instances"]:
            m=row["compatibility"]
            self.assertEqual(m["groove"],"unverified")
            if row["stratum"]=="identity_cost":
                self.assertEqual(m["quotient_ucs"],"must_refuse")
            if row["stratum"]=="shared_restart":
                self.assertEqual(m["decomposition"],"must_refuse")
    def test_topology_hash(self):
        for row in manifest()["instances"]:
            self.assertEqual(digest(row["topology"]),row["topology_sha256"])
if __name__=="__main__":unittest.main()
