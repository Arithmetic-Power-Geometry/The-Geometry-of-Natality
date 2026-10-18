"""GoN V12: bounded latent capacity, finite-horizon trace checks.
Python standard library only. Tests elementary counting theorem and tight construction.
"""
import itertools,json
from pathlib import Path

def birth_trace(actions,n0=1):
    visible=list(range(n0));next_id=n0;trace=[]
    for action in actions:
        if action:
            visible.append(next_id);next_id+=1
        trace.append(tuple(visible))
    return tuple(trace)

def reveal_trace(actions,n0=1,latent=0):
    visible=list(range(n0));next_id=n0;trace=[]
    for action in actions:
        if action:
            if next_id>=n0+latent:
                return None
            visible.append(next_id);next_id+=1
        trace.append(tuple(visible))
    return tuple(trace)

def run():
    cases=0;capacity_cases=0
    for horizon in range(0,11):
        for actions in itertools.product((0,1),repeat=horizon):
            births=sum(actions)
            actual=birth_trace(actions)
            for latent in (births,max(0,births-1)):
                observed=reveal_trace(actions,latent=latent)
                assert (observed==actual)==(latent>=births)
                capacity_cases+=1
            cases+=1
    assert sum(2**i for i in range(11))==2047
    assert reveal_trace((1,)*5,latent=4) is None
    assert reveal_trace((1,)*5,latent=5)==birth_trace((1,)*5)
    summary={'histories_checked':cases,'capacity_checks':capacity_cases,'max_horizon':10,'failures':0,'claim':'tight finite latent-universe cardinality bound; no novelty claim'}
    (Path(__file__).parent/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
