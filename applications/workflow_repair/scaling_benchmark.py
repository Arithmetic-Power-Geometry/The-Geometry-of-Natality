"""GoN: synthetic repair scaling, exhaustive search versus exact uniform-cost search.

All state keys retain used-action history. Costs are nonnegative. These are
standard exact search techniques, NOT claimed as a new GoN algorithm.
"""
import argparse, heapq, itertools, json, random, time
from pathlib import Path

def make_instance(n, seed):
    rng=random.Random(seed)
    return {"n":n,"seed":seed,"restart_costs":[3]*n,
            "create_costs":[2]*n,"rewire_costs":[1]*n,
            "action_order":rng.sample(list(range(3*n)),3*n)}

def transition(state, action, instance):
    modes,used=state
    if used & (1<<action):return None
    i,kind=divmod(action,3)
    m=list(modes)
    if kind==0:
        if m[i] not in (0,2):return None
        m[i]=3 if m[i]==2 else 1
        cost=instance['restart_costs'][i]
    elif kind==1:
        if m[i] not in (0,1):return None
        m[i]=2 if m[i]==0 else 3
        cost=instance['create_costs'][i]
    else:
        if m[i]!=2:return None
        m[i]=4
        cost=instance['rewire_costs'][i]
    return (tuple(m),used|(1<<action)),cost

def goal(state):return all(m in (1,3,4) for m in state[0])

def exhaustive(instance):
    n=instance['n'];start=((0,)*n,0)
    stack=[(start,0)];explored=0;best=None;winning=0
    while stack:
        state,cost=stack.pop();explored+=1
        if goal(state):
            if best is None or cost<best:best=cost;winning=1
            elif cost==best:winning+=1
            continue
        for action in instance['action_order']:
            result=transition(state,action,instance)
            if result:
                nxt,delta=result
                stack.append((nxt,cost+delta))
    return {'cost':best,'expanded':explored,'optimal_plan_count':winning}

def uniform_cost(instance):
    n=instance['n'];start=((0,)*n,0)
    pq=[(0,0,start)];dist={start:0};serial=0;expanded=0
    while pq:
        cost,_,state=heapq.heappop(pq)
        if cost!=dist[state]:continue
        expanded+=1
        if goal(state):return {'cost':cost,'expanded':expanded,'unique_states':len(dist)}
        for action in instance['action_order']:
            result=transition(state,action,instance)
            if result:
                nxt,delta=result;newcost=cost+delta
                if newcost<dist.get(nxt,float('inf')):
                    dist[nxt]=newcost;serial+=1
                    heapq.heappush(pq,(newcost,serial,nxt))
    return {'cost':None,'expanded':expanded,'unique_states':len(dist)}

def run(max_n=4):
    rows=[]
    for n in range(1,max_n+1):
        for seed in (0,1,2):
            inst=make_instance(n,seed)
            t=time.perf_counter();exact=exhaustive(inst);t1=time.perf_counter()-t
            t=time.perf_counter();ucs=uniform_cost(inst);t2=time.perf_counter()-t
            assert exact['cost']==ucs['cost']==3*n,(inst,exact,ucs)
            assert exact['optimal_plan_count']>=2**n
            rows.append({'n':n,'seed':seed,'actions':3*n,'exact':exact,'ucs':ucs,
                         'exact_seconds':round(t1,6),'ucs_seconds':round(t2,6)})
    return {'scope':'synthetic independent-service repair; no GROOVE comparison',
            'method':'uniform-cost search with exact state/history keys',
            'theorem_status':'standard UCS correctness, not novel GoN theorem',
            'rows':rows}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--max-n',type=int,default=4)
    parser.add_argument('--output',default='applications/workflow_repair/scaling_results.json')
    args=parser.parse_args()
    if not 1<=args.max_n<=5:parser.error('max-n must be 1..5')
    result=run(args.max_n)
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'instances':len(result['rows']),'rows':result['rows']},indent=2))
