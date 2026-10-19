"""Independent Crossref DOI-metadata audit of source-specific 23-record bibliography.

Crossref is registration-agency metadata, not direct publisher verification.
Failures, mismatches and missing fields remain explicit unresolved findings.
"""
import difflib
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

SOURCE = pathlib.Path("paper/gon_prompt15_references.bib")
OUT = pathlib.Path("research/gon_prompt16_crossref_audit.json")

def parse():
    s=SOURCE.read_text()
    blocks=re.split(r"(?m)^@",s)
    result=[]
    for block in blocks[1:]:
        m=re.match(r"\w+\s*\{\s*([^,]+),",block)
        if not m: continue
        key=m.group(1).strip()
        fields={}
        for field,value in re.findall(r"(?m)^\s*(\w+)\s*=\s*\{(.*)\}\s*,?\s*$",block):
            fields[field.lower()]=value
        result.append((key,fields))
    return result

def normalize(s):
    s=re.sub(r"\\[a-zA-Z]+\{([^}]*)\}",r"\1",s)
    s=s.replace("{","").replace("}","")
    return " ".join(re.findall(r"[a-z0-9]+",s.lower()))

def request_crossref(doi):
    url="https://api.crossref.org/works/"+urllib.parse.quote(doi,safe="/")
    req=urllib.request.Request(url,headers={"User-Agent":"GoN-Bibliography-Audit/1.0 (academic reproducibility audit)","Accept":"application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req,timeout=15) as resp:
                return json.load(resp)["message"],None
        except (urllib.error.HTTPError,urllib.error.URLError,TimeoutError) as exc:
            error=str(exc)
            if attempt<2:time.sleep(2*(attempt+1))
    return None,error

def main():
    records=parse()
    assert len(records)==23,len(records)
    results=[]
    for i,(key,f) in enumerate(records,1):
        doi=f.get("doi","").strip()
        item={"key":key,"claimed_doi":doi,"claimed_title":f.get("title"),"claimed_year":f.get("year"),"claimed_author":f.get("author"),"source":"Crossref DOI registration metadata"}
        if not doi:
            item.update(status="missing_doi")
        else:
            message,error=request_crossref(doi)
            if message is None:
                item.update(status="not_verified",error=error)
            else:
                title=(message.get("title") or [""])[0]
                date=(message.get("published") or message.get("issued") or {}).get("date-parts",[[None]])[0][0]
                authors=message.get("author") or []
                surname=authors[0].get("family","") if authors else ""
                sim=difflib.SequenceMatcher(None,normalize(f.get("title","")),normalize(title)).ratio()
                claimedyear=int(f.get("year","0")) if f.get("year","").isdigit() else None
                year_ok=(claimedyear==date) if date and claimedyear else None
                firstsurname=normalize((f.get("author","").split(" and ")[0]).split(",")[0]).split(" ")[0]
                author_ok=bool(surname and firstsurname and normalize(surname)==normalize(firstsurname))
                item.update(crossref_title=title,crossref_year=date,crossref_first_author=surname,
                            title_similarity=round(sim,3),year_match=year_ok,first_author_match=author_ok,
                            status="matched" if sim>=0.84 and year_ok and author_ok else "needs_manual_review")
        results.append(item)
        print(f"{i:02d}/23 {key}: {item['status']}",flush=True)
    summary={s:sum(x["status"]==s for x in results) for s in ("matched","needs_manual_review","not_verified","missing_doi")}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps({"generated_utc":datetime.now(timezone.utc).isoformat(),
        "method":"Crossref DOI registration metadata; NOT publisher-level verification",
        "summary":summary,"records":results},indent=2))
    print(json.dumps(summary))
if __name__=="__main__":main()
