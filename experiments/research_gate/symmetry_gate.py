"""GoN: adversarial test of exponential unfolding against classical count abstraction."""
import json

def run(n):
    # n independently executable one-time birth actions create distinguishable children.
    explicit={0}
    for i in range(n):
        explicit |= {m | (1<<i) for m in tuple(explicit)}
    assert len(explicit)==2**n
    counts={m.bit_count() for m in explicit}
    assert counts==set(range(n+1))
    # Count abstraction is unsound for queries about a particular child's identity.
    if n>=2:
        assert (1).bit_count()==(2).bit_count() and bool(1&1)!=bool(2&1)
    return {"actions":n,"explicit_states":len(explicit),"count_quotient_states":len(counts),"compression_ratio":round(len(explicit)/len(counts),4)}

if __name__=='__main__':
    rows=[run(n) for n in range(1,17)]
    print(json.dumps({"instances":len(rows),"failures":0,"rows":rows,"finding":"classical count abstraction explains compression; no GoN novelty"},indent=2))
