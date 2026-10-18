"""Independent tiny exact oracle for the GoN synthetic workflow repair fixture."""
import json
from pathlib import Path

def usable(service,alive,dependencies,stack=()):
    if service in stack: return False
    return service in alive and all(usable(dep,alive,dependencies,stack+(service,)) for dep in dependencies.get(service,()))

def solve(instance):
    actions=instance['actions'];budget=instance['budget']
    initial_alive=frozenset(s['id'] for s in instance['services'] if s['alive'])
    initial_edges=frozenset(tuple(e) for e in instance['dependencies'])
    queue=[(initial_alive,initial_edges,0,())];solutions=[]
    for alive,edges,cost,path in queue:
        deps={}
        for src,dst in edges:deps.setdefault(src,[]).append(dst)
        assert not (edges & frozenset(map(tuple,instance['forbidden_dependencies'])))
        if usable('report',alive,deps):solutions.append((cost,path))
        for action in actions:
            if action['id'] in path or any(req not in path for req in action['requires']):continue
            newcost=cost+action['cost']
            if newcost>budget:continue
            a=set(alive);e=set(edges)
            if action['effect']=='restart_auth':a.add('auth')
            elif action['effect']=='create_auth_replacement':a.add('auth_v2')
            elif action['effect']=='rewire_report':
                if 'auth_v2' not in a:continue
                e.remove(('report','auth'));e.add(('report','auth_v2'))
            else:raise ValueError('unknown effect')
            queue.append((frozenset(a),frozenset(e),newcost,path+(action['id'],)))
    return sorted(solutions)

if __name__=='__main__':
    path=Path(__file__).with_name('fixture.json')
    data=json.loads(path.read_text())
    solutions=solve(data)
    assert solutions
    assert solutions[0][0]==3
    assert any(path==('restart_auth',) for _,path in solutions)
    assert any(path==('create_auth_replacement','rewire_report') for _,path in solutions)
    assert all(path!=('create_auth_replacement',) for _,path in solutions)
    print(json.dumps({'minimum_cost':3,'successful_plans':[list(p) for c,p in solutions if c==3],'fixture':'synthetic','groove_executed':False,'q1_ready':False},indent=2))
