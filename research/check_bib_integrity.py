"""GoN bibliography integrity: local deterministic checks; no online verification claim.

Use: python research/check_bib_integrity.py
"""
from collections import Counter
from pathlib import Path
import re
import sys

bib = Path(__file__).resolve().parents[1] / "references.bib"
s = bib.read_text(encoding="utf-8")
entries = re.findall(r"(?m)^@(\w+)\s*\{\s*([^,\s]+)\s*,", s)
dois = re.findall(r"(?m)^\s*doi\s*=\s*\{([^}]+)\}", s, re.I)
keys = [k for _, k in entries]
dups = [k for k,n in Counter(keys).items() if n>1]
duplicate_dois = [d for d,n in Counter(x.lower() for x in dois).items() if n>1]
errors = []
if dups: errors.append("duplicate keys: "+repr(dups))
if duplicate_dois: errors.append("duplicate DOI fields: "+repr(duplicate_dois))
if 'K{\\\\\"o}nig' in s: errors.append("malformed BibTeX umlaut escaping")
if "doi = {10.1007/b100934}" in s: errors.append("proceedings DOI assigned to paper")
if "doi = {10.1007/978-3-540-30203-2_17}" not in s: errors.append("correct Rensink et al. paper DOI missing")
print(f"GoN bibliography: {len(entries)} entries; {len(dois)} DOI fields")
for error in errors: print("FAIL:",error,file=sys.stderr)
if errors: sys.exit(1)
print("PASS: local duplicate and known-error checks (not publisher metadata validation)")
