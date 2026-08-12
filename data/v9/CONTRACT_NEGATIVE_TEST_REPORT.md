# Contract negative and fault-injection tests

**Evidence label:** `DERIVED_EVIDENCE`

Each test mutates an in-memory copy of one landed record and asks whether the relevant guard rejects the fault. No evidence input is modified.

| Test | Guard | Observed result | Pass |
|---|---|---|---|
| FI-I1 | I1 identity hash | HASH_MISMATCH | True |
| FI-I2 | I2 uncertainty closure | UNCLOSED_UNOBSERVED_FIELD | True |
| FI-I3 | I3 tool-gap non-negativity | TOOL_GAP_MISCLASSIFIED | True |
| FI-I4 | I4 source trace | SOURCE_HASH_MISMATCH | True |
| FI-I5 | I5 cross-pipeline join | RELATION_MANIFEST_HASH_MISMATCH | True |
| FI-ADAPTER-01 | relation adapter allowlist | UNSUPPORTED_RELATION_TYPE | True |

These tests exercise declared failure branches. They do not validate relation semantics, vulnerability detection, or a new external corpus.
