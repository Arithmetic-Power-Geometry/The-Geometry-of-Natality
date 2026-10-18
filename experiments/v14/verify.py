"""GoN V14 exhaustive finite action traces: birth vs bounded reveal.
A query exposes persistent child count; rejection is observable.
"""
import itertools,json
from pathlib import Path
def execute(actions,capacity=None):
    count=0;trace=[]
    for action in actions:
        if action=='B':
            if capacity is not None and count>=capacity:
                trace.append(('rejected',count))
            else:
                count+=1;trace.append(('born',count))
        else:
            trace.append(('query',count))
    return tuple(trace)
def run():
    histories=0;checks=0;failures=0
    for capacity in range(0,7):
        for horizon in range(0,9):
            for actions in itertools.product(('B','Q'),repeat=horizon):
                histories+=1
                births=actions.count('B')
                same=(execute(actions)==execute(actions,capacity))
                expected=(births<=capacity)
                assert same==expected,(capacity,actions)
                checks+=1
        witness=('B',)*(capacity+1)+('Q',)
        assert execute(witness)!=execute(witness,capacity)
    result={'capacities':list(range(7)),'max_horizon':8,'histories_checked':histories,'exact_matches_or_separations_checked':checks,'failures':failures,'scope':'finite fixed-slot rooted-star emulator','novelty':'not established'}
    (Path(__file__).parent/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':run()
