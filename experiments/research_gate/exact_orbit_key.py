"""Exact finite orbit keys for *declaratively certified* identity-bearing states.

Not a general-purpose symmetry checker. A certificate is an assumption about
transition/goal/cost equivariance, NOT inferred from Python callbacks.
"""
from dataclasses import dataclass
from itertools import permutations, product
from math import factorial

class UnsafeQuotient(ValueError):
    pass

@dataclass(frozen=True, order=True)
class Ref:
    name: str

@dataclass(frozen=True)
class State:
    active: tuple = ()
    edges: tuple = ()
    used: tuple = ()
    attributes: tuple = ()
    forbidden: tuple = ()
    resources: tuple = ()

@dataclass(frozen=True)
class Certificate:
    """Every pool is a complete role class, including currently unallocated names.

    Fixed names must not appear in pools. Every identity-bearing value MUST use
    Ref, even in histories, negative guards, and resource records. No opaque
    callbacks or hidden identity tests may be present.
    """
    pools: tuple
    fixed: tuple = ()
    equivariant_transitions: bool = False
    equivariant_goal: bool = False
    equivariant_costs: bool = False
    equivariant_constraints: bool = False
    equivariant_allocation: bool = False
    no_hidden_identity_data: bool = False

FIELDS = ("active", "edges", "used", "attributes", "forbidden", "resources")

def _atom(x, rename):
    if isinstance(x, Ref):
        return ("ref", rename.get(x.name, x.name))
    if type(x) in (str, int, bool, type(None)):
        return ("lit", type(x).__name__, repr(x))
    if isinstance(x, tuple):
        return ("tuple", tuple(_atom(v, rename) for v in x))
    raise UnsafeQuotient("unsupported value: use Ref for identities and tuples for records")

def _check(state, cert, limit):
    if not isinstance(state, State) or not isinstance(cert, Certificate):
        raise UnsafeQuotient("typed State and Certificate required")
    if not all((cert.equivariant_transitions, cert.equivariant_goal,
                cert.equivariant_costs, cert.equivariant_constraints,
                cert.equivariant_allocation, cert.no_hidden_identity_data)):
        raise UnsafeQuotient("missing explicit equivariance certification")
    pools = tuple(tuple(p) for p in cert.pools)
    names = [n for p in pools for n in p]
    if any(not isinstance(n, str) for n in names) or len(set(names)) != len(names):
        raise UnsafeQuotient("pool names must be unique strings")
    if set(names) & set(cert.fixed):
        raise UnsafeQuotient("fixed identities cannot be permuted")
    if len(names) > limit:
        raise UnsafeQuotient("factorial search size limit exceeded")
    for f in FIELDS:
        values = getattr(state, f)
        if not isinstance(values, tuple):
            raise UnsafeQuotient("state fields must be tuples")
        for v in values:
            _atom(v, {})
    return pools

def _encoding(state, ren):
    return tuple(tuple(sorted(_atom(v, ren) for v in getattr(state, f)))
                 for f in FIELDS)

def orbit_encodings(state, cert, limit=8):
    """Independent exhaustive orbit oracle; intended for small states."""
    pools = _check(state, cert, limit)
    options = [list(permutations(p)) for p in pools]
    for chosen in product(*options):
        rename = {old: new for pool, perm in zip(pools, chosen)
                  for old, new in zip(pool, perm)}
        yield _encoding(state, rename)

def canonical_key(state, cert, limit=8):
    """Lexicographically minimal encoding over the entire declared group.

    For fixed cert, K(s)=K(t) iff states are in the same group orbit.
    Cost O(product |pool|! * state encoding); intended as exact oracle.
    """
    return min(orbit_encodings(state, cert, limit))

def same_orbit_oracle(a, b, cert, limit=8):
    """Independent direct orbit-membership check; does not call canonical_key."""
    _check(b, cert, limit)
    target = _encoding(b, {})
    return any(k == target for k in orbit_encodings(a, cert, limit))

def permutation_count(cert):
    result = 1
    for pool in cert.pools:
        result *= factorial(len(pool))
    return result
