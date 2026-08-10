#!/usr/bin/env python3
"""One-command integrity and result-surface validation.

Evidence label: DERIVED_EVIDENCE
"""
import csv, gzip, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()

def rows(path, compressed=False):
    opener=gzip.open if compressed else open
    with opener(path, "rt", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

fail=[]
for line in (ROOT/"checksums/SHA256SUMS").read_text().splitlines():
    expected, rel=line.split("  ",1)
    p=ROOT/rel
    if not p.exists() or digest(p)!=expected:
        fail.append(f"checksum:{rel}")

cards=rows(ROOT/"data/current/ALL_POPULATION_EVIDENCE_CARDS.csv")
features=rows(ROOT/"data/current/ALL_POPULATION_SAMPLE_FEATURES.csv.gz", True)
oracle=rows(ROOT/"data/current/ALL_POPULATION_SOURCE_ORACLE.csv")
unc=rows(ROOT/"data/current/ALL_POPULATION_UNCERTAINTY_LOG.csv")
flow=rows(ROOT/"data/current/RQ_POPULATION_FLOW.csv")
metrics=rows(ROOT/"data/current/FULL_POPULATION_SCHEMA_METRICS.csv")
invariants=rows(ROOT/"data/current/CONTRACT_INVARIANT_RESULTS.csv")
relations=rows(ROOT/"data/cross_pipeline/RELATION_EXTRACTION_RECORDS_v2_3.csv")
cross_unc=rows(ROOT/"data/cross_pipeline/UNCERTAINTY_LOG_v2_3.csv")

slots=["ec1_function_recovery_status","ec2_core_logic_candidate_status","ec3_semantic_facts_status","ec4_state_evidence_status","ec5_relation_graph_status","ec6_uncertainty_log_status"]
def signature(card,schema):
    if schema.startswith("S2_"):return (card[slots[0]],card[slots[5]])
    if schema.startswith("S3_"):return (card[slots[0]],card[slots[3]],card[slots[5]])
    return tuple(card[x] for x in slots)
def majority(values):
    from collections import Counter
    c=Counter(values);return sorted(c,key=lambda x:(-c[x],x))[0]
card_map={r["sample_id"]:r for r in cards}
feature_map={r["sample_id"]:r for r in features}
source={r["sample_id"]:r for r in oracle if r["source_oracle_function_block"] in {"True","False"}}
tasks={
 "TOOL_OUTPUT_AVAILABILITY":[(r["sample_id"],r["fold_id"],int(r["recovery_status"]=="NM_SYMBOLS_RECOVERED")) for r in features],
 "SOURCE_FUNCTION_BLOCK_PRESENCE":[(sid,feature_map[sid]["fold_id"],int(r["source_oracle_function_block"]=="True")) for sid,r in source.items()],
}
metric_map={(r["task"],r["schema"]):r for r in metrics}
metric_replay=True
for task,items in tasks.items():
  folds=sorted({fold for _,fold,_ in items})
  for schema in ["S2_OBSERVABILITY_UNCERTAINTY","S3_EMPIRICAL_CHANNELS","S6_TYPED_SLOTS"]:
    pred={}
    for fold in folds:
      train=[x for x in items if x[1]!=fold];test=[x for x in items if x[1]==fold]
      groups={}
      for sid,_,target in train:groups.setdefault(signature(card_map[sid],schema),[]).append(target)
      lookup={key:majority(value) for key,value in groups.items()};global_value=majority(x[2] for x in train)
      for sid,_,_ in test:pred[sid]=lookup.get(signature(card_map[sid],schema),global_value)
    tp=sum(target==1 and pred[sid]==1 for sid,_,target in items);fp=sum(target==0 and pred[sid]==1 for sid,_,target in items)
    fn=sum(target==1 and pred[sid]==0 for sid,_,target in items);tn=sum(target==0 and pred[sid]==0 for sid,_,target in items)
    reported=metric_map[(task,schema)]
    metric_replay &= (tp,fp,fn,tn)==tuple(int(reported[key]) for key in ["tp","fp","fn","tn"])

checks={
 "cards":len(cards)==2431,
 "features":len(features)==2431,
 "oracle_scorable":sum(r["source_oracle_function_block"] in {"True","False"} for r in oracle)==1876,
 "uncertainty_rows":len(unc)==4176,
 "population_flow":len(flow)==5 and {r["analysis_id"] for r in flow}=={"CARD_ACCOUNTING","TOOL_OUTPUT_AVAILABILITY","SOURCE_FUNCTION_BLOCK_PRESENCE","HISTORICAL_FUNCTION_CLASSIFIER","SECOND_PIPELINE_CONTRACT_INSTANTIATION"},
 "schema_rows":len(metrics)==6 and {r["n"] for r in metrics if r["task"]=="TOOL_OUTPUT_AVAILABILITY"}=={"2431"},
 "schema_metric_replay":metric_replay,
 "invariants":len(invariants)==5 and all(r["pass"]=="True" and r["failure_count"]=="0" for r in invariants),
 "relations":len(relations)==6657,
 "cross_uncertainty":len(cross_unc)==20,
}
fail.extend(name for name,ok in checks.items() if not ok)

for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".md",".csv",".json",".py",".tex",".bib",".txt"}:
        if path.name == "run_artifact.py":
            continue
        text=path.read_text(encoding="utf-8",errors="ignore")
        if "/mnt/e/github repos/" in text or "../../_scaa_evidence_build_project" in text:
            fail.append(f"absolute_or_external_path:{path.relative_to(ROOT)}")

result={
 "status":"PASS" if not fail else "FAIL",
 "checks":checks,
 "failures":sorted(set(fail)),
 "scope":"Derived reporting analysis is self-contained; full raw extraction requires separately acquired PLC-BEAD inputs.",
 "release":"v2.0.0",
 "licenses":{"code":"BSD-3-Clause","derived_data":"CC-BY-4.0"},
 "evidence_label":"DERIVED_EVIDENCE",
}
print(json.dumps(result,indent=2))
raise SystemExit(0 if not fail else 1)
