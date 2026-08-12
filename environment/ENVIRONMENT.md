# Observed validation environment

**Evidence label:** `DERIVED_EVIDENCE`

Observed on 2026-08-11:

- OS: WSL2 Linux `6.6.87.2-microsoft-standard-WSL2`, x86-64
- Python: `3.10.12`
- Git: `2.34.1`
- Tectonic: `0.16.9`
- radare2: `6.1.9`, commit `654d5474ce`, launched with the recorded local library path
- RO-Crate validator used for the landed v10 evidence: `0.11.3_b959343+2-dirty`; the current executable also reports an upstream tag/version mismatch, so the package preserves portable summaries and source-output SHA-256 values

`run_artifact.py` and both package metadata/extended validators require only the Python standard library. Tectonic, radare2, and `rocrate-validator` are not required for the package-level replay. Their recorded outputs are validated rather than silently regenerated under a different tool state.
