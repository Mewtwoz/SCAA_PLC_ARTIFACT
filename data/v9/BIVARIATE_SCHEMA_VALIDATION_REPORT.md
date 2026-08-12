# Bivariate evidence-state validation

**Evidence label:** `DERIVED_EVIDENCE`

The revised contract separates nominal observation support from explanation closure. `supported` means that the configured field rule has qualifying observable support; `not_supported` means that an applicable field rule was attempted without qualifying support; and `unobserved` means that the configured tool/format did not expose the required observation. Closure is recorded independently as `not_required`, `explained`, or `unexplained`. These states are reporting decisions, not truth probabilities or correctness scores. The source oracle is not used during card-state assignment.

EC6 is no longer a support-strength slot. It is the card-level closure field over EC1--EC5. The label S6 denotes the full contract (five observation fields plus closure), not six ordinal measurements.

## Realized primary-population states

| Field | Support status | Closure status | Rows |
|---|---|---|---:|
| EC1 | supported | not_required | 1876 |
| EC1 | unobserved | explained | 555 |
| EC2 | supported | not_required | 1876 |
| EC2 | unobserved | explained | 555 |
| EC3 | supported | not_required | 1876 |
| EC3 | unobserved | explained | 555 |
| EC4 | not_supported | explained | 1401 |
| EC4 | supported | not_required | 475 |
| EC4 | unobserved | explained | 555 |
| EC5 | supported | not_required | 1876 |
| EC5 | unobserved | explained | 555 |
| CARD | NOT_APPLICABLE | complete | 2431 |

## Ten-fold information-retention replay

| Task | Representation | n | Balanced accuracy | Macro F1 | Signatures |
|---|---|---:|---:|---:|---:|
| TOOL_OUTPUT_AVAILABILITY | S2_OBSERVABILITY_CLOSURE | 2431 | 1.000000 | 1.000000 | 2 |
| TOOL_OUTPUT_AVAILABILITY | S3_EMPIRICAL_CHANNELS | 2431 | 1.000000 | 1.000000 | 3 |
| TOOL_OUTPUT_AVAILABILITY | S6_FULL_CONTRACT | 2431 | 1.000000 | 1.000000 | 3 |
| SOURCE_FUNCTION_BLOCK_PRESENCE | S2_OBSERVABILITY_CLOSURE | 1876 | 0.500000 | 0.367072 | 1 |
| SOURCE_FUNCTION_BLOCK_PRESENCE | S3_EMPIRICAL_CHANNELS | 1876 | 0.692033 | 0.637565 | 2 |
| SOURCE_FUNCTION_BLOCK_PRESENCE | S6_FULL_CONTRACT | 1876 | 0.692033 | 0.637565 | 2 |

The replay is a dataset-specific information-retention test. It does not establish schema economy, analyst utility, semantic accuracy, or predictive deployment performance.
