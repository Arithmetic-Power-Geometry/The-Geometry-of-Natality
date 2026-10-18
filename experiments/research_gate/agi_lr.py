"""GoN G0/G3 gate: exact deterministic action-discovery baseline (stdlib)."""
from functools import lru_cache
import random,json

def available(items,mask):
    return [i for i,a in enumerate(items) if not mask>>i&1 and (a["parent"] is None or mask>>a["parent"]&1)]

def oracle(items,budget):
    @lru_cache(None)
    def dp(mask,left):
        best=(0,())
        for i in available(items,mask):
            a=items[i]
            if a["cost"]<=left:
                v,p=dp(mask|1<<i,left-a["cost"])
                if a["reward"]+v>best[0]:best=(a["reward"]+v,(i,)+p)
        return best
    value,path=dp(0,budget)
    return {"reward":value,"path":list(path),"states":dp.cache_info().currsize}

def exhaustive(items,budget):
    best=[0]
    def visit(mask,left,value):
        best[0]=max(best[0],value)
        for i in available(items,mask):
            a=items[i]
            if a["cost"]<=left:visit(mask|1<<i,left-a["cost"],value+a["reward"])
    visit(0,budget,0)
    return best[0]

def greedy(items,budget):
    mask=0;value=0
    while True:
        opts=[i for i in available(items,mask) if items[i]["cost"]<=budget]
        if not opts:break
        i=max(opts,key=lambda i:(items[i]["reward"]/items[i]["cost"],-i))
        a=items[i];mask|=1<<i;budget-=a["cost"];value+=a["reward"]
    return value

def main():
    witness=[{"parent":None,"cost":1,"reward":1},{"parent":0,"cost":1,"reward":5},{"parent":None,"cost":1,"reward":3}]
    assert oracle(witness,2)["reward"]==6 and greedy(witness,2)==4
    wins=ties=0
    for seed in range(120):
        rng=random.Random(seed);n=rng.randint(4,10)
        items=[{"parent":None if i==0 or rng.random()<.38 else rng.randrange(i),"cost":rng.randint(1,3),"reward":rng.randint(0,9)} for i in range(n)]
        budget=rng.randint(2,9)
        opt=oracle(items,budget)["reward"]
        assert opt==exhaustive(items,budget)
        g=greedy(items,budget)
        assert g<=opt
        wins+=opt>g;ties+=opt==g
    result={"instances":120,"oracle_matches_exhaustive":120,"optimal_better_than_greedy":wins,"ties":ties,"failures":0,"witness":{"optimal":6,"greedy":4},"novelty":"not established"}
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
