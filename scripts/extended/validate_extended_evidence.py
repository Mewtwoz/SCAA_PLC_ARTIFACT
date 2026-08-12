#!/usr/bin/env python3
"""Validate the v9--v11 evidence surfaces packaged for the JSS revision.

Evidence label: DERIVED_EVIDENCE

This validator uses only the Python standard library and landed derived files.
It does not rerun binary extraction or infer semantic/vulnerability labels.
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def majority(values: list[int]) -> int:
    counts = Counter(values)
    return sorted(counts, key=lambda value: (-counts[value], value))[0]


def bivariate_signature(card: dict[str, str], schema: str) -> tuple[str, ...]:
    field_stems = {
        "EC1": "ec1_function_recovery",
        "EC2": "ec2_core_logic_candidate",
        "EC3": "ec3_static_facts",
        "EC4": "ec4_declared_state_role",
        "EC5": "ec5_relation_graph",
    }
    selected = {
        "S2_OBSERVABILITY_CLOSURE": ["EC1"],
        "S3_EMPIRICAL_CHANNELS": ["EC1", "EC4"],
        "S6_FULL_CONTRACT": ["EC1", "EC2", "EC3", "EC4", "EC5"],
    }[schema]
    values: list[str] = []
    for field in selected:
        stem = field_stems[field]
        values.extend((card[f"{stem}_support_status"], card[f"{stem}_closure_status"]))
    values.append(card["card_closure_status"])
    return tuple(values)


def validate(root: Path) -> dict[str, object]:
    failures: list[str] = []
    checks: dict[str, bool] = {}

    def check(name: str, condition: bool) -> None:
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)

    v9 = root / "data/v9"
    cards = read_csv(v9 / "BIVARIATE_EVIDENCE_CARDS.csv")
    cross_cards = read_csv(v9 / "BIVARIATE_CROSS_PIPELINE_EVIDENCE_CARDS.csv")
    metrics = read_csv(v9 / "BIVARIATE_SCHEMA_METRICS.csv")
    predictions = read_csv(v9 / "BIVARIATE_SCHEMA_PREDICTIONS.csv")
    negative = read_csv(v9 / "CONTRACT_NEGATIVE_TEST_RESULTS.csv")
    card_by_sample = {row["sample_id"]: row for row in cards}

    check("v9_primary_cards_2431", len(cards) == 2431)
    check("v9_cross_pipeline_cards_10", len(cross_cards) == 10)
    check("v9_six_metric_rows", len(metrics) == 6)
    check("v9_prediction_rows_12921", len(predictions) == 12921)
    check("v9_all_primary_cards_closed", all(row["card_closure_status"] == "complete" for row in cards))
    check("v9_all_cross_cards_closed", all(row["card_closure_status"] == "complete" for row in cross_cards))
    check("v9_all_card_hashes_present", all(len(row["binary_sha256"]) == 64 for row in cards + cross_cards))

    support_columns = [name for name in cards[0] if name.startswith("ec") and name.endswith("_support_status")]
    closure_columns = [name for name in cards[0] if name.startswith("ec") and name.endswith("_closure_status")]
    check("v9_five_bivariate_observation_fields", len(support_columns) == 5 and len(closure_columns) == 5)
    check(
        "v9_nominal_state_vocabularies",
        all(row[name] in {"supported", "not_supported", "unobserved"} for row in cards for name in support_columns)
        and all(row[name] in {"not_required", "explained", "unexplained"} for row in cards for name in closure_columns),
    )

    tool_rows = [row for row in predictions if row["task"] == "TOOL_OUTPUT_AVAILABILITY"]
    expected_tool_rows = 2431 * 3
    check("ec1_construction_rows_7293", len(tool_rows) == expected_tool_rows)
    check(
        "ec1_target_is_derived_from_ec1_support",
        all(
            int(row["actual"])
            == int(card_by_sample[row["sample_id"]]["ec1_function_recovery_support_status"] == "supported")
            for row in tool_rows
        ),
    )
    check("ec1_construction_predictions_are_lossless", all(row["actual"] == row["predicted"] for row in tool_rows))

    source_rows = [row for row in predictions if row["task"] == "SOURCE_FUNCTION_BLOCK_PRESENCE"]
    by_schema: dict[str, dict[str, tuple[str, str]]] = defaultdict(dict)
    for row in source_rows:
        by_schema[row["schema"]][row["sample_id"]] = (row["actual"], row["predicted"])
    check("source_role_rows_5628", len(source_rows) == 1876 * 3)
    check(
        "source_role_s3_s6_predictions_identical",
        by_schema.get("S3_EMPIRICAL_CHANNELS") == by_schema.get("S6_FULL_CONTRACT")
        and len(by_schema.get("S3_EMPIRICAL_CHANNELS", {})) == 1876,
    )
    metric_map = {(row["task"], row["schema"]): row for row in metrics}
    s3 = metric_map.get(("SOURCE_FUNCTION_BLOCK_PRESENCE", "S3_EMPIRICAL_CHANNELS"), {})
    s6 = metric_map.get(("SOURCE_FUNCTION_BLOCK_PRESENCE", "S6_FULL_CONTRACT"), {})
    check(
        "source_role_s3_s6_metrics_identical",
        bool(s3) and all(s3.get(key) == s6.get(key) for key in ("tp", "fp", "fn", "tn", "accuracy", "balanced_accuracy", "macro_f1")),
    )

    oracle = read_csv(root / "data/current/ALL_POPULATION_SOURCE_ORACLE.csv")
    source_targets = {
        row["sample_id"]: int(row["source_oracle_function_block"] == "True")
        for row in oracle
        if row["source_oracle_function_block"] in {"True", "False"}
    }
    stored_source = {
        (row["schema"], row["sample_id"]): int(row["predicted"])
        for row in source_rows
    }
    source_fold = {row["sample_id"]: row["fold_id"] for row in source_rows}
    replay_ok = True
    metric_replay_ok = True
    for schema in ("S2_OBSERVABILITY_CLOSURE", "S3_EMPIRICAL_CHANNELS", "S6_FULL_CONTRACT"):
        replayed: dict[str, int] = {}
        folds = sorted({source_fold[sample_id] for sample_id in source_targets})
        for fold in folds:
            train_ids = [sample_id for sample_id in source_targets if source_fold[sample_id] != fold]
            test_ids = [sample_id for sample_id in source_targets if source_fold[sample_id] == fold]
            groups: dict[tuple[str, ...], list[int]] = defaultdict(list)
            for sample_id in train_ids:
                groups[bivariate_signature(card_by_sample[sample_id], schema)].append(source_targets[sample_id])
            lookup = {key: majority(values) for key, values in groups.items()}
            global_value = majority([source_targets[sample_id] for sample_id in train_ids])
            for sample_id in test_ids:
                replayed[sample_id] = lookup.get(bivariate_signature(card_by_sample[sample_id], schema), global_value)
        replay_ok &= all(replayed[sample_id] == stored_source[(schema, sample_id)] for sample_id in source_targets)
        tp = sum(source_targets[sample_id] == 1 and replayed[sample_id] == 1 for sample_id in source_targets)
        fp = sum(source_targets[sample_id] == 0 and replayed[sample_id] == 1 for sample_id in source_targets)
        fn = sum(source_targets[sample_id] == 1 and replayed[sample_id] == 0 for sample_id in source_targets)
        tn = sum(source_targets[sample_id] == 0 and replayed[sample_id] == 0 for sample_id in source_targets)
        reported = metric_map[("SOURCE_FUNCTION_BLOCK_PRESENCE", schema)]
        metric_replay_ok &= (tp, fp, fn, tn) == tuple(int(reported[key]) for key in ("tp", "fp", "fn", "tn"))
    check("source_role_predictions_replayed_from_bivariate_cards", replay_ok)
    check("source_role_confusion_counts_replayed", metric_replay_ok)
    check("six_fault_injections_trigger_guards", len(negative) == 6 and all(row["pass"] == "True" for row in negative))

    current_invariants = read_csv(root / "data/current/CONTRACT_INVARIANT_RESULTS.csv")
    check(
        "five_record_contract_invariants_pass",
        len(current_invariants) == 5
        and all(row["pass"] == "True" and row["failure_count"] == "0" for row in current_invariants),
    )

    v11 = root / "data/v11"
    eligibility = read_csv(v11 / "OPENPLC_ADAPTER_ELIGIBILITY_FLOW.csv")
    included = [row for row in eligibility if row["eligibility_status"] == "INCLUDED_RELATION_BACKED_CARD_INPUT"]
    excluded = [row for row in eligibility if row["eligibility_status"] == "EXCLUDED_NO_LANDED_RELATION_ROWS"]
    relations = read_csv(root / "data/cross_pipeline/RELATION_EXTRACTION_RECORDS_v2_3.csv")
    manifest = read_csv(root / "data/cross_pipeline/NATIVE_BINARY_MANIFEST_v2_6.csv")
    relation_counts = Counter(row["sample_id"] for row in relations)
    check("openplc_manifest_population_56", len(manifest) == 56 and len(eligibility) == 56)
    check("openplc_relation_backed_inputs_10", len(included) == 10)
    check("openplc_explicit_exclusions_46", len(excluded) == 46)
    check("openplc_relation_rows_6657", len(relations) == 6657)
    check(
        "openplc_eligibility_counts_replay",
        all(int(row["relation_row_count"]) == relation_counts[row["sample_id"]] for row in eligibility),
    )
    check("openplc_included_hashes_match", all(row["relation_sha256_status"] == "MATCH" for row in included))

    requirements = read_csv(v11 / "REPORT_DESIGN_REQUIREMENT_COVERAGE.csv")
    totals = Counter(row["representation_id"] for row in requirements)
    satisfied = Counter(
        row["representation_id"] for row in requirements if row["requirement_satisfied"].lower() == "true"
    )
    check("design_requirement_rows_27", len(requirements) == 27 and set(totals.values()) == {9})
    check(
        "design_requirement_counts_2_6_9",
        satisfied == Counter({"AGGREGATE_ONLY": 2, "FLAT_PROVENANCE": 6, "SCAA_BIVARIATE_CONTRACT": 9}),
    )

    v10 = root / "data/v10"
    vendor_cards = read_csv(v10 / "SCHNEIDER_EXTERNAL_EVIDENCE_CARDS.csv")
    vendor_profile = read_csv(v10 / "SCHNEIDER_EXTERNAL_CORPUS_PROFILE.csv")
    vendor_validation = json.loads((v10 / "SCHNEIDER_EXTERNAL_ADAPTER_VALIDATION.json").read_text(encoding="utf-8"))
    check("schneider_two_closed_cards", len(vendor_cards) == 2 and all(row["card_closure_status"] == "complete" for row in vendor_cards))
    check("schneider_relation_graph_unobserved", all(row["ec5_relation_graph_support_status"] == "unobserved" for row in vendor_cards))
    check(
        "schneider_function_counts_7733_7920",
        {int(row["function_count"]) for row in vendor_profile} == {7733, 7920},
    )
    check("schneider_validation_passes", str(vendor_validation.get("status", "")).startswith("PASS"))

    crate = v10 / "workflow_run_rocrate"
    crate_metadata = json.loads((crate / "ro-crate-metadata.json").read_text(encoding="utf-8"))
    graph = {entity["@id"]: entity for entity in crate_metadata["@graph"]}
    action = graph.get("#contract-summary-run", {})
    workflow_validation = json.loads((crate / "outputs/workflow_validation.json").read_text(encoding="utf-8"))
    prov_text = (crate / "prov/run_provenance.ttl").read_text(encoding="utf-8")
    check("workflow_run_crate_three_inputs", len(action.get("object", [])) == 3)
    check("workflow_run_crate_two_outputs", len(action.get("result", [])) == 2)
    check("workflow_summary_has_21_rows", workflow_validation.get("output_rows") == 21)
    check("prov_o_three_link_families", all(token in prov_text for token in ("prov:used", "prov:wasGeneratedBy", "prov:wasAssociatedWith")))

    required = json.loads((v10 / "ROCRATE_VALIDATION_REQUIRED.json").read_text(encoding="utf-8"))
    recommended = json.loads((v10 / "ROCRATE_VALIDATION_RECOMMENDED.json").read_text(encoding="utf-8"))
    check("rocrate_required_55_of_55", required.get("passed_checks") == 55 and required.get("failed_checks") == 0)
    check(
        "rocrate_recommended_134_of_135_with_two_findings",
        recommended.get("passed_checks") == 134
        and recommended.get("total_checks") == 135
        and recommended.get("failed_checks") == 1
        and recommended.get("finding_count") == 2,
    )

    codesys = read_csv(root / "data/codesys/CODESYS_TOOL_TRIAL_RESULTS.csv")
    check("codesys_probe_has_five_hash_addressed_rows", len(codesys) == 5 and all(len(row["sha256"]) == 64 for row in codesys))
    check("codesys_probe_records_no_r2_code", all("havecode false" in row["r2_output_summary"] for row in codesys))

    return {
        "evidence_label": "DERIVED_EVIDENCE",
        "status": "PASS" if not failures else "FAIL",
        "checks": checks,
        "failures": failures,
        "counts": {
            "primary_cards": len(cards),
            "bivariate_cross_pipeline_cards": len(cross_cards),
            "source_role_rows": len(source_rows),
            "ec1_construction_rows": len(tool_rows),
            "openplc_manifest_rows": len(manifest),
            "openplc_relation_rows": len(relations),
            "schneider_cards": len(vendor_cards),
            "workflow_summary_rows": workflow_validation.get("output_rows"),
        },
        "boundary": (
            "Validation covers landed derived reporting records and package structure. It does not rerun raw binary "
            "extraction, establish semantic correctness, support vulnerability detection, or provide human-utility evidence."
        ),
    }


if __name__ == "__main__":
    package_root = Path(__file__).resolve().parents[2]
    result = validate(package_root)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
