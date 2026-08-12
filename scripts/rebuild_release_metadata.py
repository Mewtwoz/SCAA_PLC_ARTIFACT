#!/usr/bin/env python3
"""Rebuild portable checksums and the artifact inventory.

Evidence label: DERIVED_EVIDENCE
"""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKSUMS = ROOT / "checksums/SHA256SUMS"
MANIFEST = ROOT / "ARTIFACT_MANIFEST.csv"
DYNAMIC = {
    "ARTIFACT_MANIFEST.csv",
    "checksums/SHA256SUMS",
    "CLEAN_ROOM_VALIDATION_LOG.md",
    "RELEASE_CANDIDATE_VALIDATION.json",
}


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts and path.suffix != ".pyc"
    )


def role(relative: str) -> str:
    if relative.startswith("data/"):
        return "derived_data"
    if relative.startswith("scripts/") or relative == "run_artifact.py":
        return "validation_code"
    if relative.startswith("manuscript_support/"):
        return "manuscript_support"
    if relative.startswith("history/"):
        return "non_contributory_history"
    if relative.startswith("environment/"):
        return "environment_record"
    if relative.startswith("checksums/") or relative == "ARTIFACT_MANIFEST.csv":
        return "integrity_metadata"
    return "release_documentation"


def main() -> None:
    current = files()
    stable = [path for path in current if str(path.relative_to(ROOT)) not in DYNAMIC]
    CHECKSUMS.parent.mkdir(parents=True, exist_ok=True)
    CHECKSUMS.write_text(
        "".join(f"{sha256(path)}  {path.relative_to(ROOT)}\n" for path in stable),
        encoding="utf-8",
    )

    inventory = [path for path in files() if path != MANIFEST]
    with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["file_path", "bytes", "sha256", "role", "evidence_label"],
            lineterminator="\n",
        )
        writer.writeheader()
        for path in inventory:
            relative = str(path.relative_to(ROOT))
            writer.writerow(
                {
                    "file_path": relative,
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                    "role": role(relative),
                    "evidence_label": "DERIVED_EVIDENCE",
                }
            )
    print(f"stable_checksum_entries={len(stable)}")
    print(f"artifact_manifest_entries={len(inventory)}")


if __name__ == "__main__":
    main()
