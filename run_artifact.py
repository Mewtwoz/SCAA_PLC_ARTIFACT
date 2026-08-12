#!/usr/bin/env python3
"""One-command integrity and derived result-surface validation.

Evidence label: DERIVED_EVIDENCE
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts/extended"))
from validate_extended_evidence import validate as validate_extended  # noqa: E402


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def rows(path: Path, compressed: bool = False) -> list[dict[str, str]]:
    opener = gzip.open if compressed else open
    with opener(path, "rt", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def stable_payloads() -> set[str]:
    excluded = {
        "ARTIFACT_MANIFEST.csv",
        "checksums/SHA256SUMS",
        "CLEAN_ROOM_VALIDATION_LOG.md",
        "RELEASE_CANDIDATE_VALIDATION.json",
    }
    return {
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
        and str(path.relative_to(ROOT)) not in excluded
    }


failures: list[str] = []
checksum_entries: dict[str, str] = {}
for line in (ROOT / "checksums/SHA256SUMS").read_text(encoding="utf-8").splitlines():
    expected, relative = line.split("  ", 1)
    checksum_entries[relative] = expected

payloads = stable_payloads()
if set(checksum_entries) != payloads:
    failures.append("checksum_manifest_file_set")
for relative, expected in checksum_entries.items():
    path = ROOT / relative
    if not path.exists() or digest(path) != expected:
        failures.append(f"checksum:{relative}")

cards = rows(ROOT / "data/current/ALL_POPULATION_EVIDENCE_CARDS.csv")
features = rows(ROOT / "data/current/ALL_POPULATION_SAMPLE_FEATURES.csv.gz", True)
oracle = rows(ROOT / "data/current/ALL_POPULATION_SOURCE_ORACLE.csv")
uncertainty = rows(ROOT / "data/current/ALL_POPULATION_UNCERTAINTY_LOG.csv")
flow = rows(ROOT / "data/current/RQ_POPULATION_FLOW.csv")
legacy_metrics = rows(ROOT / "data/current/FULL_POPULATION_SCHEMA_METRICS.csv")
invariants = rows(ROOT / "data/current/CONTRACT_INVARIANT_RESULTS.csv")
relations = rows(ROOT / "data/cross_pipeline/RELATION_EXTRACTION_RECORDS_v2_3.csv")
cross_uncertainty = rows(ROOT / "data/cross_pipeline/UNCERTAINTY_LOG_v2_3.csv")

legacy_slots = [
    "ec1_function_recovery_status",
    "ec2_core_logic_candidate_status",
    "ec3_semantic_facts_status",
    "ec4_state_evidence_status",
    "ec5_relation_graph_status",
    "ec6_uncertainty_log_status",
]


def signature(card: dict[str, str], schema: str) -> tuple[str, ...]:
    if schema.startswith("S2_"):
        return card[legacy_slots[0]], card[legacy_slots[5]]
    if schema.startswith("S3_"):
        return card[legacy_slots[0]], card[legacy_slots[3]], card[legacy_slots[5]]
    return tuple(card[name] for name in legacy_slots)


def majority(values: list[int]) -> int:
    counts = Counter(values)
    return sorted(counts, key=lambda value: (-counts[value], value))[0]


card_map = {row["sample_id"]: row for row in cards}
feature_map = {row["sample_id"]: row for row in features}
source = {
    row["sample_id"]: row
    for row in oracle
    if row["source_oracle_function_block"] in {"True", "False"}
}
source_items = [
    (sample_id, feature_map[sample_id]["fold_id"], int(row["source_oracle_function_block"] == "True"))
    for sample_id, row in source.items()
]
legacy_metric_map = {(row["task"], row["schema"]): row for row in legacy_metrics}
legacy_source_metric_replay = True
for schema in ["S2_OBSERVABILITY_UNCERTAINTY", "S3_EMPIRICAL_CHANNELS", "S6_TYPED_SLOTS"]:
    predictions: dict[str, int] = {}
    folds = sorted({fold for _, fold, _ in source_items})
    for fold in folds:
        train = [item for item in source_items if item[1] != fold]
        test = [item for item in source_items if item[1] == fold]
        groups: dict[tuple[str, ...], list[int]] = {}
        for sample_id, _, target in train:
            groups.setdefault(signature(card_map[sample_id], schema), []).append(target)
        lookup = {key: majority(value) for key, value in groups.items()}
        global_value = majority([item[2] for item in train])
        for sample_id, _, _ in test:
            predictions[sample_id] = lookup.get(signature(card_map[sample_id], schema), global_value)
    tp = sum(target == 1 and predictions[sample_id] == 1 for sample_id, _, target in source_items)
    fp = sum(target == 0 and predictions[sample_id] == 1 for sample_id, _, target in source_items)
    fn = sum(target == 1 and predictions[sample_id] == 0 for sample_id, _, target in source_items)
    tn = sum(target == 0 and predictions[sample_id] == 0 for sample_id, _, target in source_items)
    reported = legacy_metric_map[("SOURCE_FUNCTION_BLOCK_PRESENCE", schema)]
    legacy_source_metric_replay &= (tp, fp, fn, tn) == tuple(
        int(reported[key]) for key in ("tp", "fp", "fn", "tn")
    )

core_checks = {
    "checksum_manifest_is_complete": set(checksum_entries) == payloads,
    "checksums_match": not any(item.startswith("checksum:") for item in failures),
    "cards_2431": len(cards) == 2431,
    "features_2431": len(features) == 2431,
    "source_oracle_scorable_1876": len(source) == 1876,
    "uncertainty_rows_4176": len(uncertainty) == 4176,
    "population_flow_has_five_tasks": len(flow) == 5,
    "legacy_v6_source_role_metric_replay": legacy_source_metric_replay,
    "five_invariants_zero_failures": len(invariants) == 5
    and all(row["pass"] == "True" and row["failure_count"] == "0" for row in invariants),
    "relations_6657": len(relations) == 6657,
    "cross_pipeline_uncertainty_20": len(cross_uncertainty) == 20,
}
failures.extend(name for name, passed in core_checks.items() if not passed)

for path in ROOT.rglob("*"):
    if path == ROOT / "run_artifact.py":
        continue
    if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts and path.suffix.lower() in {
        ".md", ".csv", ".json", ".py", ".tex", ".bib", ".txt", ".ttl", ".cff"
    }:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "/mnt/e/github repos/" in text or "E:\\github repos\\" in text or "../../_scaa_evidence_build_project" in text:
            failures.append(f"machine_specific_project_path:{path.relative_to(ROOT)}")

extended = validate_extended(ROOT)
if extended["status"] != "PASS":
    failures.extend(f"extended:{name}" for name in extended["failures"])

result = {
    "status": "PASS" if not failures else "FAIL",
    "release": "v2.1.0",
    "checks": core_checks,
    "extended_validation": extended,
    "failures": sorted(set(failures)),
    "scope": (
        "The package validates derived reporting analysis, evidence-card construction checks, source-role retention, "
        "contract invariants, bounded OpenPLC/Schneider adapters, and portable provenance records. Raw binary/source "
        "extraction and human-utility evaluation are outside the one-command replay."
    ),
    "licenses": {"code": "BSD-3-Clause", "derived_data": "CC-BY-4.0"},
    "evidence_label": "DERIVED_EVIDENCE",
}
print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(0 if not failures else 1)
