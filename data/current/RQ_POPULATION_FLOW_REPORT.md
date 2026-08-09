# RQ-specific population flow

**Evidence label:** `DERIVED_EVIDENCE`

A historical function-label gate is retained only for historical classifier diagnostics. It does not control the current card, tool-output, or source-oracle tasks.

| Analysis | Start | Included | Excluded | Inclusion basis | Exclusion basis |
|---|---:|---:|---:|---|---|
| CARD_ACCOUNTING | 2431 | 2431 | 0 | every manifest binary | none |
| TOOL_OUTPUT_AVAILABILITY | 2431 | 2431 | 0 | target defined for every attempted binary | none |
| SOURCE_FUNCTION_BLOCK_PRESENCE | 2431 | 1876 | 555 | unambiguous mapped Structured Text oracle | CODESYS proprietary project source or missing/ambiguous ST mapping |
| HISTORICAL_FUNCTION_CLASSIFIER | 2431 | 2353 | 78 | scorable historical function label | label missing/sentinel; this gate does not control current RQs |
| SECOND_PIPELINE_CONTRACT_INSTANTIATION | 10 | 10 | 0 | pre-existing samples with manifest, relation, and uncertainty rows | not a population-generalization sample |
