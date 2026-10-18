"""Exact two-world GoN information-limit checks, Python stdlib."""
import json
from fractions import Fraction
from pathlib import Path
def reward(world,action):
    return int((world==0 and action==0) or (world==1 and action==1))
def main():
    for action in (0,1):
        assert min(reward(0,action),reward(1,action))==0
    for numerator in range(101):
        p=Fraction(numerator,100)
        worst=min(p,1-p)
        assert worst<=Fraction(1,2)
    assert min(Fraction(1,2),1-Fraction(1,2))==Fraction(1,2)
    assert all(reward(w,w)==1 for w in (0,1))
    out={'deterministic_policies_checked':2,'randomized_grid_points_checked':101,'randomized_minimax_value':'1/2','clairvoyant_value':'1','observation_enabled_value':'1','failures':0,'novelty':'not established'}
    (Path(__file__).parent/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
