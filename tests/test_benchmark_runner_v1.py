import unittest
from experiments.research_gate.benchmark_runner_v1 import run,decode,negative_control,stats
from experiments.research_gate.benchmark_v1 import manifest
class BenchmarkRunnerTests(unittest.TestCase):
    def test_frozen_small_smoke_and_exact_oracles(self):
        data=run(repetitions=1,warmup=0)
        self.assertEqual(data["counts"],{"matched_cells":36,"negative_control_cells":36,
                                         "measured_trials":72})
        self.assertEqual(len(data["comparisons"]),36)
        self.assertTrue(all(x["status"]=="correct_refusal" for x in data["negative_controls"]))
        self.assertTrue(all(x["status"]=="success" for x in data["trials"]))
    def test_all_instances_reconstruct(self):
        self.assertEqual(len([decode(x) for x in manifest()["instances"]]),72)
    def test_statistics_deterministic(self):
        pairs=[(.3,.1),(.2,.4),(.5,.2)]
        self.assertEqual(stats(pairs,17),stats(pairs,17))
if __name__=="__main__":unittest.main()
