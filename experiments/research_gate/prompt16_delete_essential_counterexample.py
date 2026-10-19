"""Falsify delete-free terminal-reachability conjecture under live capacity and guards.

Finite two-name relay instance:
  initial live name 0, name 0 permanently used;
  capacity 1; link from name 0 to terminal forbidden;
  name 1 can be created, linked; unit-cost actions.
A successful plan necessarily deletes name 0 before creating name 1.
"""
import heapq
import itertools
import json

def successors(state,allow_delete=True):
    used,live,linked=state
    if 1 not in used and len(live)<1:
        yield "create(1)",(used|frozenset({1}),live|frozenset({1}),linked)
    if 1 in live and 1 not in linked:
        yield "link(1,T)",(used,live,linked|frozenset({1}))
    if 1 in linked:
        yield "unlink(1,T)",(used,live,linked-frozenset({1}))
    if allow_delete:
        for name in sorted(live):
            if name not in linked:
                yield f"delete({name})",(used,live-frozenset({name}),linked)

def solve(allow_delete=True):
    start=(frozenset({0}),frozenset({0}),frozenset())
    q=[(0,0,start,())]
    seen={}
    counter=itertools.count(1)
    while q:
        cost,_,s,plan=heapq.heappop(q)
        if cost>=seen.get(s,10**9):continue
        seen[s]=cost
        if 1 in s[2]:
            return cost,plan,len(seen)
        for a,t in successors(s,allow_delete):
            heapq.heappush(q,(cost+1,next(counter),t,plan+(a,)))
    return None,(),len(seen)

if __name__=="__main__":
    full=solve(True)
    delete_free=solve(False)
    assert full[0]==3,full
    assert full[1]==("delete(0)","create(1)","link(1,T)"),full
    assert delete_free[0] is None,delete_free
    print(json.dumps({"hypothesis":"delete-free terminal repair always suffices",
        "status":"falsified","full":{"cost":full[0],"plan":full[1],"states":full[2]},
        "delete_free":{"cost":None,"states":delete_free[2]},
        "assumptions":"one-shot names; live capacity 1; name 0 terminal link forbidden; nonnegative unit costs"},indent=2))
