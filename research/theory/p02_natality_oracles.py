from dataclasses import dataclass
from heapq import heappush, heappop

@dataclass(frozen=True)
class Edge:
    u: str
    v: str
    cost: int
    cap: str = ''

def futures(states, edges, B, enabled, obs, method):
    if method == 'bellman':
        d = {s:float('inf') for s in states}; d['s']=0
        for _ in range(len(states)-1):
            new=d.copy()
            for e in edges:
                if not e.cap or e.cap in enabled: new[e.v]=min(new[e.v],d[e.u]+e.cost)
            if new==d: break
            d=new
    else:
        d={'s':0}; q=[(0,'s')]
        while q:
            w,u=heappop(q)
            if w!=d[u]: continue
            for e in edges:
                if e.u!=u or (e.cap and e.cap not in enabled): continue
                nw=w+e.cost
                if nw<=B and nw<d.get(e.v,float('inf')):
                    d[e.v]=nw; heappush(q,(nw,e.v))
    return frozenset(obs[s] for s in d if d[s]<=B)

def verified(states,edges,B,enabled,obs):
    a=futures(states,edges,B,enabled,obs,'dijkstra')
    b=futures(states,edges,B,enabled,obs,'bellman')
    assert a==b,(a,b)
    return a

def values(states,edges,B,obs):
    return [len(verified(states,edges,B,c,obs)) for c in (set(),{'a'},{'b'},{'a','b'})]

def main():
    S=('s','x'); E=(Edge('s','x',1,'a'),Edge('s','x',2)); O={s:s for s in S}
    gain=[len(verified(S,E,b,{'a'},O)-verified(S,E,b,set(),O)) for b in range(3)]
    assert gain==[0,1,0]; print('C1 refuted',gain)
    S=('s','xa','xb'); E=(Edge('s','xa',1,'a'),Edge('s','xb',1,'b'))
    O={'s':'base','xa':'new','xb':'new'}
    v=values(S,E,1,O); assert v==[1,2,2,2]
    print('C2 refuted',v,'delta',v[3]-v[1]-v[2]+v[0])
    S=('s','a','b','ab')
    E=(Edge('s','a',1,'a'),Edge('s','b',1,'b'),Edge('a','ab',1,'b'),Edge('b','ab',1,'a'))
    O={s:s for s in S}
    v1=values(S,E,1,O); v2=values(S,E,2,O)
    assert v1==[1,2,2,3] and v2==[1,2,2,4]
    print('C3 refuted',v1,v2)
    S=('s','xa','xb','ya','yb')
    E=(Edge('s','xa',1,'a'),Edge('s','xb',1,'a'),Edge('xa','ya',1),Edge('xb','yb',1))
    O={'s':'base','xa':'created','xb':'created','ya':'linked','yb':'linked'}
    swap={'s':'s','xa':'xb','xb':'xa','ya':'yb','yb':'ya'}
    assert all(Edge(swap[e.u],swap[e.v],e.cost,e.cap) in E for e in E)
    for b in range(4):
        for caps in (set(),{'a'}):
            assert verified(S,E,b,caps,O)==verified(S,E,b,caps,{s:O[swap[s]] for s in S})
    bad=(Edge('s','xa',1,'a'),Edge('s','xb',3,'a'))
    assert Edge('s','xb',1,'a') not in bad
    print('C4 supported conditionally; unequal costs break swap equivariance')
    print('PASS independent Dijkstra/Bellman-Ford comparisons')
if __name__=='__main__': main()
