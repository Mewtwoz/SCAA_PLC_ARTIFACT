# Clean-room package validation

**Evidence label:** `DERIVED_EVIDENCE`

- validated_at: `2026-08-12 Asia/Shanghai`
- release: `v2.1.0`
- method: package copied to a new `/tmp` directory with `.git`, `__pycache__`, and bytecode excluded
- command: `python3 run_artifact.py`
- exit_code: `0`
- final_status: `PASS`
- core_checks: `11/11`
- extended_checks: `39/39`
- failures: `0`
- temporary_copy_removed: `YES`

The isolated run verified the stable checksum file set and file digests; 2,431 primary records; 1,876 source-oracle rows; bivariate card states; source-role prediction and confusion-count replay; the EC1 construction check; five zero-failure invariants; six injected-fault guards; 56 OpenPLC manifest rows, 10 relation-backed inputs, 46 exclusions, 6,657 relations, and 20 uncertainty rows; two closed Schneider cards; 21 Workflow Run summary rows; three PROV-O link families; the 2/9, 6/9, and 9/9 author-defined requirement counts; and the recorded 55/55 required plus 134/135 required-and-recommended RO-Crate check counts.

This validation replays packaged derived records. It does not rerun excluded raw binary/source extraction or create human-validation results.
