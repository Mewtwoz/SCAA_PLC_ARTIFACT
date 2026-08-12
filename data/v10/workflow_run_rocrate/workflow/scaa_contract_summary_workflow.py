#!/usr/bin/env python3
"""Summarise bivariate SCAA evidence-card states across named corpora.

This workflow consumes derived CSV records only. It does not inspect or copy
raw PLC binaries, infer semantic correctness, or assign vulnerability labels.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


FIELDS = (
    "ec1_function_recovery",
    "ec2_core_logic_candidate",
    "ec3_static_facts",
    "ec4_declared_state_role",
    "ec5_relation_graph",
)
ALLOWED_SUPPORT = {"supported", "not_supported", "unobserved"}
ALLOWED_CLOSURE = {"not_required", "explained", "unexplained"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_cards(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {"sample_id", "binary_sha256", "card_closure_status"}
    for field in FIELDS:
        required.add(f"{field}_support_status")
        required.add(f"{field}_closure_status")
    missing = sorted(required - set(rows[0] if rows else []))
    if missing:
        raise ValueError(f"{path}: missing columns {missing}")
    for row in rows:
        if len(row["binary_sha256"]) != 64:
            raise ValueError(f"{path}: invalid SHA256 for {row['sample_id']}")
        if row["card_closure_status"] != "complete":
            raise ValueError(f"{path}: incomplete card {row['sample_id']}")
        for field in FIELDS:
            support = row[f"{field}_support_status"]
            closure = row[f"{field}_closure_status"]
            if support not in ALLOWED_SUPPORT or closure not in ALLOWED_CLOSURE:
                raise ValueError(f"{path}: invalid bivariate state for {row['sample_id']}:{field}")
            if support == "supported" and closure != "not_required":
                raise ValueError(f"{path}: supported field requires not_required closure")
            if support != "supported" and closure != "explained":
                raise ValueError(f"{path}: unsupported/unobserved field requires explained closure")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plcbead", type=Path, required=True)
    parser.add_argument("--openplc", type=Path, required=True)
    parser.add_argument("--schneider", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--validation", type=Path, required=True)
    args = parser.parse_args()

    inputs = {
        "PLC-BEAD": args.plcbead,
        "OpenPLC/radare2": args.openplc,
        "Schneider/VxWorks": args.schneider,
    }
    cards = {name: read_cards(path) for name, path in inputs.items()}
    output_rows: list[dict[str, object]] = []
    for corpus, rows in cards.items():
        for field in FIELDS:
            counts = Counter(
                (row[f"{field}_support_status"], row[f"{field}_closure_status"])
                for row in rows
            )
            for (support, closure), count in sorted(counts.items()):
                output_rows.append(
                    {
                        "corpus": corpus,
                        "sample_count": len(rows),
                        "evidence_field": field,
                        "support_status": support,
                        "closure_status": closure,
                        "count": count,
                        "evidence_label": "DERIVED_EVIDENCE",
                    }
                )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]))
        writer.writeheader()
        writer.writerows(output_rows)

    validation = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_label": "DERIVED_EVIDENCE",
        "status": "PASS",
        "corpus_sample_counts": {name: len(rows) for name, rows in cards.items()},
        "input_sha256": {name: sha256(path) for name, path in inputs.items()},
        "output_rows": len(output_rows),
        "output_sha256": sha256(args.output),
        "boundary": (
            "Bivariate record-contract validation only; no semantic correctness, "
            "human utility, vulnerability detection, or broad portability claim."
        ),
    }
    args.validation.write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
