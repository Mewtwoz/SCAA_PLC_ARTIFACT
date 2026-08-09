# SCAA-PLC JSS Artifact Release Candidate

**Evidence label:** `DERIVED_EVIDENCE`

This package supports the content-revised SCAA-PLC reporting-method manuscript. It contains all author-generated data required to verify the reported full-population accounting, source-role analysis, representation comparison, contract invariants, trace cases, and bounded second-pipeline instantiation.

## Quick start

From the package root, run:

```bash
python3 run_artifact.py
```

The command uses only the Python standard library, verifies every payload checksum, checks all declared row-count surfaces, confirms the five zero-failure invariants, and scans for machine-specific absolute paths. The expected status is `PASS`.

## Package map

- `data/current/`: v6 full-population cards, source oracle, metrics, predictions, uncertainty rows, population flow, schema coverage, trace cases, and invariant results. The 195-MiB feature CSV is gzip-compressed for GitHub compatibility.
- `data/cross_pipeline/`: derived native manifest, relation, and uncertainty tables used by the bounded radare2 instantiation. Raw binaries are excluded.
- `data/config/`: manifest, split, core/runtime rules, and state-adapter rules.
- `data/v5/`: earlier row-level method-validation outputs retained for result lineage.
- `reviewer_task/`: independent reviewer-task protocol and empty response tasks (`TEMPLATE_ONLY`). No human result is claimed.
- `scripts/`: PLC-BEAD acquisition verifier; `run_artifact.py` replays the fold-wise schema confusion counts from packaged rows.
- `manuscript_support/`: current LaTeX source, supplement, bibliography, and revision report.
- `history/`: non-contributory classifier/ablation chronology removed from the submission supplement.
- `environment/`: observed build environment and dependency notes.
- `checksums/`: SHA-256 payload manifest.

## Third-party acquisition boundary

Raw PLC-BEAD files are not redistributed because the examined upstream snapshot contains no explicit license file. Acquire the dataset from its upstream repository under the terms supplied by its maintainers, then run:

```bash
python3 scripts/verify_plcbead_acquisition.py /path/to/PLC-BEAD
```

This verifies all 2,431 binary hashes without copying raw files into the package.

## Reproducibility levels

The one-command validator reproduces and checks the derived reporting-analysis surface. Re-running `nm` from raw inputs requires a separately acquired PLC-BEAD snapshot and GNU binutils. Re-running the radare2 extraction requires the excluded OpenPLC binaries and the original extraction environment; the package verifies the landed derived relation/uncertainty joins but does not claim an extraction rerun without those inputs.

## Release status

`READY_FOR_HUMAN_LICENSE_AND_UPLOAD_DECISION`. Before upload, the authors must choose code and data licenses, replace the license templates, create a fixed release tag, and record the reviewer URL. A persistent archive/DOI is recommended for the submission version.
