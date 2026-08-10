# Clean-room package validation

**Evidence label:** `DERIVED_EVIDENCE`

- validated_at: `2026-08-10 Asia/Shanghai`
- release: `v2.0.0`
- command: `python run_artifact.py`
- exit_code: `0`
- expected_status: `PASS`
- validation_boundary: all packaged checksums, row-count surfaces, five stored invariants, schema-metric replay, relation/uncertainty counts, and path sanitization

```json
{
  "status": "PASS",
  "checks": {
    "cards": true,
    "features": true,
    "oracle_scorable": true,
    "uncertainty_rows": true,
    "population_flow": true,
    "schema_rows": true,
    "schema_metric_replay": true,
    "invariants": true,
    "relations": true,
    "cross_uncertainty": true
  },
  "failures": [],
  "scope": "Derived reporting analysis is self-contained; full raw extraction requires separately acquired PLC-BEAD inputs.",
  "release": "v2.0.0",
  "licenses": {
    "code": "BSD-3-Clause",
    "derived_data": "CC-BY-4.0"
  },
  "evidence_label": "DERIVED_EVIDENCE"
}
```

The release commit and tag are additionally verified from a fresh remote clone before publication; the exact commit SHA and result are recorded in the GitHub Release notes.
