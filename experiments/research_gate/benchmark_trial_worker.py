"""Isolated one-trial worker; Linux resource cap set by parent."""
import argparse,json
from experiments.research_gate.benchmark_v1 import manifest,verify
from experiments.research_gate.benchmark_runner_v1 import decode,measured
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--cell",type=int,required=True)
    p.add_argument("--algorithm",required=True)
    a=p.parse_args()
    frozen=manifest();verify(frozen)
    row=frozen["instances"][a.cell]
    result=measured(decode(row),a.algorithm)
    print(json.dumps(result,sort_keys=True))
if __name__=="__main__":main()
