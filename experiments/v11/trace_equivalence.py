"""GoN V11: check observational equivalence of birth and preinstalled reveal semantics.
This verifies a finite illustrative family, not the general theorem.
"""
import itertools,json
from pathlib import Path
def birth_trace(actions):
    visible={0};history=[]
    for i,a in enumerate(actions):
        if a:
            visible.add(i+1)
        history.append(tuple(sorted(visible)))
    return tuple(history)
def reveal_trace(actions):
    hidden=set(range(1,len(actions)+1));visible={0};history=[]
    for i,a in enumerate(actions):
        if a:
            hidden.remove(i+1);visible.add(i+1)
        history.append(tuple(sorted(visible)))
    return tuple(history)
def run():
    count=0
    for n in range(0,11):
        for actions in itertools.product((0,1),repeat=n):
            assert birth_trace(actions)==reveal_trace(actions)
            count+=1
    result={'max_horizon':10,'action_histories_checked':count,'failures':0,'scope':'finite action histories, trace-only observation, preinstalled hidden states','novelty':'not established'}
    (Path(__file__).parent/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':run()
