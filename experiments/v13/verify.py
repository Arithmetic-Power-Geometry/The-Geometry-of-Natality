"""GoN V13: exhaustive finite-width slot bound verification (stdlib)."""
import itertools,json
from pathlib import Path

def born_patterns(bits,width,n0=1):
    live=[];out=[];t=0
    for bit in bits:
        if bit:
            live.append(('fresh',t));t+=1
            live=live[-width:] if width else []
        visible=list(range(n0))+live
        out.append(len(visible)==len(set(visible)))
    return out,t

def emulate(bits,width,slots,n0=1):
    live=[];out=[];t=0
    for bit in bits:
        if bit:
            t+=1
            if width:
                if len(live)==width:live.pop(0)
                available=next((x for x in range(n0,slots) if x not in live),None)
                if available is None:return None,t
                live.append(available)
        visible=list(range(n0))+live
        out.append(len(visible)==len(set(visible)))
    return out,t

def run():
    checks=0;histories=0
    for horizon in range(0,9):
        for bits in itertools.product((0,1),repeat=horizon):
            histories+=1
            for width in range(0,5):
                _,births=born_patterns(bits,width)
                required=1+min(width,births)
                for slots in (required,max(0,required-1)):
                    observed,_=emulate(bits,width,slots)
                    # At zero births, even n0=1 initial persistent state is necessary.
                    success=observed is not None and slots>=1
                    assert success==(slots>=required),(horizon,bits,width,slots)
                    checks+=1
    summary={'histories':histories,'capacity_checks':checks,'max_horizon':8,'widths':[0,1,2,3,4],'failures':0,'novelty':'not established'}
    (Path(__file__).parent/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
