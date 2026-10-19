"""Independent concrete trace checker; does not import planner transition/goal."""
from experiments.research_gate.exact_orbit_key import Ref

def verify(g,plan,claimed_cost):
    active=set()
    wired=set()
    used=set()
    restored=False
    total=0
    names=set(g.names)
    costs=dict(g.identity_costs)
    for action in plan:
        if not isinstance(action,tuple) or not action:
            raise AssertionError("malformed action")
        kind=action[0]
        if kind=="restore":
            if action!=("restore",) or restored:
                raise AssertionError("invalid restore")
            restored=True
            weight=g.restore_cost
        elif kind=="create":
            if len(action)!=2 or not isinstance(action[1],Ref):
                raise AssertionError("invalid creation")
            name=action[1].name
            if name not in names or name in active or len(active)>=g.capacity:
                raise AssertionError("creation not applicable")
            active.add(name)
            weight=costs.get(name,g.create_cost)
        elif kind=="rewire":
            if len(action)!=2 or not isinstance(action[1],Ref):
                raise AssertionError("invalid rewire")
            name=action[1].name
            if name not in active or name in wired or (g.fixed_preferred and name!=g.fixed_preferred):
                raise AssertionError("rewire not applicable")
            wired.add(name)
            weight=g.rewire_cost
        else:
            raise AssertionError("unknown operation")
        if action in used:
            raise AssertionError("repeated action")
        used.add(action)
        total+=weight
        if total>g.budget:
            raise AssertionError("budget violation")
    if not (restored or len(wired)>=g.target):
        raise AssertionError("goal not reached")
    if total!=claimed_cost:
        raise AssertionError("cost mismatch")
    return {"cost":total,"restored":restored,"active":tuple(sorted(active)),
            "wired":tuple(sorted(wired))}

