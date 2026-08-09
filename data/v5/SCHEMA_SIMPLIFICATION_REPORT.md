# Evidence-card schema simplification analysis

**Evidence label:** `DERIVED_EVIDENCE`

## Question

Do the six typed slots retain more task-relevant information than a two-field availability summary or a three-channel representation?

The evaluated representations are: (i) EC1 observability plus EC6 uncertainty, (ii) EC1 observability plus EC4 declared-role support plus EC6 uncertainty, and (iii) all six typed slots. A transparent signature-majority decoder is fitted on nine inferred-name folds and applied to the remaining fold. Each sample is tested once.

| Task | Schema | n | Accuracy | Balanced accuracy | Macro F1 | Signatures | Ambiguous-row fraction |
|---|---|---:|---:|---:|---:|---:|---:|
| TOOL_OUTPUT_AVAILABILITY | S2_OBSERVABILITY_UNCERTAINTY | 2353 | 1.000000 | 1.000000 | 1.000000 | 2 | 0.000000 |
| TOOL_OUTPUT_AVAILABILITY | S3_EMPIRICAL_CHANNELS | 2353 | 1.000000 | 1.000000 | 1.000000 | 3 | 0.000000 |
| TOOL_OUTPUT_AVAILABILITY | S6_TYPED_SLOTS | 2353 | 1.000000 | 1.000000 | 1.000000 | 3 | 0.000000 |
| SOURCE_FUNCTION_BLOCK_PRESENCE | S2_OBSERVABILITY_UNCERTAINTY | 1873 | 0.580886 | 0.500000 | 0.367443 | 1 | 1.000000 |
| SOURCE_FUNCTION_BLOCK_PRESENCE | S3_EMPIRICAL_CHANNELS | 1873 | 0.647090 | 0.691974 | 0.637151 | 2 | 1.000000 |
| SOURCE_FUNCTION_BLOCK_PRESENCE | S6_TYPED_SLOTS | 1873 | 0.647090 | 0.691974 | 0.637151 | 2 | 1.000000 |

The shared EC1/EC2/EC3/EC5 channel has 0 row-level mismatches on the evaluated card table. The three-channel and six-slot representations therefore have identical decoding results here. This supports presenting the three empirical channels as the primary analytical representation while retaining the six typed slots only for provenance.

## Boundary

The tool-output task is a pipeline-consistency check. The source-function-block task uses a separately extracted source-syntax predicate, but it remains within one PLC-BEAD snapshot. These are information-retention tests, not human-subject utility, semantic accuracy, vulnerability detection, or external ecosystem tests.
