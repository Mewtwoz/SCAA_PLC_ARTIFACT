# Record-contract invariant report

**Evidence label:** `DERIVED_EVIDENCE`

These checks establish machine-verifiable record properties only. They do not measure analyst utility or semantic correctness.

| Invariant | Checked units | Failures | Pass | Definition |
|---|---:|---:|---|---|
| I1_IDENTITY_HASH | 2431 | 0 | True | Every primary card SHA-256 replays against its binary bytes. |
| I2_UNCERTAINTY_CLOSURE | 4176 | 0 | True | Every weak EC1-EC5 slot has a typed uncertainty record. |
| I3_UNSUPPORTED_NOT_NEGATIVE | 555 | 0 | True | Unsupported CODESYS tool outputs remain partial rather than unexplained missing/negative. |
| I4_SOURCE_TRACE | 1876 | 0 | True | Every mapped source hash replays against the source bytes. |
| I5_CROSS_PIPELINE_HASH_JOIN | 6677 | 0 | True | Every second-pipeline relation/uncertainty SHA-256 joins its manifest row. |
