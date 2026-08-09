# Clean-room package validation

**Evidence label:** `DERIVED_EVIDENCE`

- executed_utc: `2026-08-09T11:23:58.396984+00:00`
- command: `python3 run_artifact.py`
- exit_code: `0`
- temporary_copy_removed: `true`

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
  "human_actions": [
    "select code/data licenses",
    "upload fixed release and record URL/tag",
    "optionally archive release for DOI"
  ],
  "evidence_label": "DERIVED_EVIDENCE"
}
```
