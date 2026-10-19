import unittest
from experiments.research_gate.benchmark_runner_isolated import worker
from experiments.research_gate.independent_benchmark_audit import audit,boot_ci,qtile
from experiments.research_gate.benchmark_runner_v1 import run
class Prompt9Tests(unittest.TestCase):
    def test_original_audit(self):
        d=run(repetitions=1,warmup=0)
        a=audit(d)
        self.assertEqual(a["audited_trials"],72)
        self.assertEqual(a["censored"],0)
    def test_tampering_rejected(self):
        d=run(repetitions=1,warmup=0)
        d["trials"].pop()
        with self.assertRaises(AssertionError):audit(d)
    def test_worker_limits(self):
        x=worker(0,"full_ucs")
        self.assertEqual(x["status"],"success")
        self.assertEqual(x["exit_code"],0)
        self.assertFalse(x["censored"])
    def test_independent_quantiles(self):
        self.assertEqual(qtile([1,2,3],.5),2)
        self.assertEqual(boot_ci([1,2,3],17),boot_ci([1,2,3],17))
if __name__=="__main__":unittest.main()
