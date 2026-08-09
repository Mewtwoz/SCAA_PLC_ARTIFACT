#!/usr/bin/env python3
"""Verify a separately acquired PLC-BEAD snapshot without copying it.

Evidence label: DERIVED_EVIDENCE
"""
import argparse, csv, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()
def rows(path):
    with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
p=argparse.ArgumentParser();p.add_argument("plcbead_root",type=Path);a=p.parse_args()
cards={r["sample_id"]:r for r in rows(ROOT/"data/current/ALL_POPULATION_EVIDENCE_CARDS.csv")}
manifest=rows(ROOT/"data/config/PLCBEAD_MANIFEST.csv")
missing=[];mismatch=[]
for row in manifest:
    sid=Path(row["binary_name"]).stem
    path=a.plcbead_root/"Binary/All_PLC_Program_Binaries"/row["binary_name"]
    if not path.exists():missing.append(str(path));continue
    if digest(path)!=cards[sid]["binary_sha256"]:mismatch.append(sid)
print(f"checked={len(manifest)-len(missing)} missing={len(missing)} mismatch={len(mismatch)}")
for value in missing[:20]:print("MISSING",value)
for value in mismatch[:20]:print("MISMATCH",value)
raise SystemExit(0 if not missing and not mismatch else 1)
