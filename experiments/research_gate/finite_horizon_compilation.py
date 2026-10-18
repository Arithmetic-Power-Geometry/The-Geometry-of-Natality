"""GoN negative novelty test: compile a rule-generating system into an LTS."""
from collections import deque
import json

def successors(config):
    phase,rules=config
    if phase==0 and 'invent' in rules:
        return [('invent',(1,frozenset({'use'})))]
    if phase==1 and 'use' in rules:
        return [('use',(2,frozenset()))]
    return []

def compile_lts(initial,horizon):
    q=deque([(initial,0)])
    seen={(initial,0)}
    edges=[]
    while q:
        c,d=q.popleft()
        if d==horizon:continue
        for action,nxt in successors(c):
            u=(c,d);v=(nxt,d+1)
            edges.append((u,action,v))
            if v not in seen:seen.add(v);q.append(v)
    return seen,edges

def traces_generative(initial,horizon):
    traces={()}
    def rec(c,d,prefix):
        if d==horizon:return
        for a,nxt in successors(c):
            p=prefix+(a,);traces.add(p);rec(nxt,d+1,p)
    rec(initial,0,())
    return traces

def traces_lts(initial,edges):
    adj={}
    for u,a,v in edges:adj.setdefault(u,[]).append((a,v))
    traces={()}
    def rec(state,prefix):
        for a,v in adj.get(state,[]):
            p=prefix+(a,);traces.add(p);rec(v,p)
    rec((initial,0),())
    return traces

def main():
    initial=(0,frozenset({'invent'}))
    checked=0
    for horizon in range(0,12):
        states,edges=compile_lts(initial,horizon)
        assert traces_generative(initial,horizon)==traces_lts(initial,edges)
        checked+=1
    states,edges=compile_lts(initial,2)
    assert len(states)==3 and len(edges)==2
    result={'horizons_checked':checked,'horizon_range':[0,11],'witness_horizon':2,'witness_states':3,'witness_edges':2,'failures':0,'finding':'finite-horizon emergent action types compile into ordinary finite LTS','novelty':'negative gate'}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
