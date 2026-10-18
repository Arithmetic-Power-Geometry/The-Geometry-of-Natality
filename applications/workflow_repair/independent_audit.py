"""GoN independent exhaustive audit of the synthetic workflow fixture."""
from itertools import permutations
import json

def evaluate(order, budget=3):
    alive={'ingress','report'}
    edges={('report','auth')}
    cost=0
    used=set()
    for act in order:
        if act in used:return None
        used.add(act)
        if act=='restart_auth':
            cost+=3
            alive.add('auth')
        elif act=='create_auth_replacement':
            cost+=2
            alive.add('auth_v2')
        elif act=='rewire_report':
            if 'create_auth_replacement' not in used or 'auth_v2' not in alive:return None
            cost+=1
            edges.remove(('report','auth'))
            edges.add(('report','auth_v2'))
        else:raise ValueError(act)
        if cost>budget:return None
    return {'cost':cost,'usable':all(y in alive for x,y in edges if x=='report')}

def main():
    acts=['restart_auth','create_auth_replacement','rewire_report']
    valid=[]
    considered=0
    for n in range(4):
        for p in permutations(acts,n):
            considered+=1
            r=evaluate(p)
            if r is not None:valid.append((p,r))
    winning=[(p,r) for p,r in valid if r['usable']]
    assert considered==16
    assert len(valid)==4
    assert len(winning)==2
    assert min(r['cost'] for p,r in winning)==3
    assert any(p==('restart_auth',) for p,r in winning)
    assert any(p==('create_auth_replacement','rewire_report') for p,r in winning)
    assert not evaluate(('create_auth_replacement',))['usable']
    print(json.dumps({'sequences_considered':considered,'valid_sequences':len(valid),'successful_sequences':len(winning),'minimum_cost':3,'failures':0},indent=2))

if __name__=='__main__':main()
