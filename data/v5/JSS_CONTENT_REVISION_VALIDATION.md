# JSS content-revision validation

**Evidence label:** `DERIVED_EVIDENCE`

**Verdict:** `JSS_CONTENT_REVISION_VALIDATED`

Checks passed: 36/36.

| check | status | detail |
|---|---|---|
| required_file | PASS | 08_split_paper1_plc_binary_analysis/tex/main.tex |
| required_file | PASS | 08_split_paper1_plc_binary_analysis/tex/supplementary.tex |
| required_file | PASS | 08_split_paper1_plc_binary_analysis/tex/main.pdf |
| required_file | PASS | 08_split_paper1_plc_binary_analysis/tex/supplementary.pdf |
| required_file | PASS | 09_paper1_experiment_evidence/v5_jss_method_validation/V5_JSS_METHOD_VALIDATION_RESULT.json |
| required_file | PASS | 09_paper1_experiment_evidence/v5_jss_method_validation/UNGATED_TRANSFER_PROBE_METRICS.csv |
| required_file | PASS | 09_paper1_experiment_evidence/v5_jss_method_validation/SCHEMA_SIMPLIFICATION_METRICS.csv |
| required_file | PASS | 09_paper1_experiment_evidence/v5_jss_method_validation/CROSS_PIPELINE_EVIDENCE_CARDS.csv |
| v5_verdict | PASS | JSS_METHOD_VALIDATION_READY_WITH_SCOPE_LIMITATIONS |
| output_sha256 | PASS | UNGATED_TRANSFER_PROBE_ROWS.csv: fb75b9b1a9d6e3a7d63eeb959a54d986c2beb729cd96b3126c531071f86d260f |
| output_sha256 | PASS | UNGATED_TRANSFER_PROBE_METRICS.csv: 2bfc2424bec907af81fc70308f8e7e1296a223fe6560e2f6f678a7b12890b734 |
| output_sha256 | PASS | UNGATED_TRANSFER_PROBE_REPORT.md: 57c19900928e022d85ddd7d6ec97fb9ce2c94afc257dd69b6b35dc0ef408983f |
| output_sha256 | PASS | SCHEMA_SIMPLIFICATION_METRICS.csv: d84c48a04bb9d1f23f06a25225cdbf1ce0fda755b48a94517a58ed22096b6301 |
| output_sha256 | PASS | SCHEMA_SIMPLIFICATION_PREDICTIONS.csv: cd734b11c268020ec8da278dbfb521c02fcd4b37d01c83185463faef7274ed81 |
| output_sha256 | PASS | SCHEMA_STATE_COLLISION_AUDIT.csv: 2542ceb00c538e62e125eb0fc9f76fe9f969bbc7079e88bad5e941bf556a02d4 |
| output_sha256 | PASS | SCHEMA_SIMPLIFICATION_REPORT.md: 1c0ccafc379edd45953c4308d74b1628c4882b4b5b9362f42a9698829b73a43d |
| output_sha256 | PASS | CROSS_PIPELINE_EVIDENCE_CARDS.csv: 60811b7e8110623eb5a3a768c434b2aacd6529cf1c781fee56f0f5aaaf437618 |
| output_sha256 | PASS | CROSS_PIPELINE_ADAPTER_REPORT.md: d5d1e0ee9a96eec81541abd2c70429d6d73b244471e50ab1613133765a68c8a7 |
| geb_exact_counts | PASS | TP=353, TN=263 |
| ungated_transfer_boundary | PASS | OpenPLC production scope is OUT_OF_SCOPE; ungated-probe FN total is 735 |
| schema_s3_s6_equivalence | PASS | S3 and S6 source-task balanced accuracy and macro F1 match |
| cross_pipeline_cards | PASS | cards=10 |
| cross_pipeline_relations | PASS | relations=6657 |
| required_manuscript_boundary | PASS | OpenPLC rows are out of scope for the production SA-001 rule |
| required_manuscript_boundary | PASS | Schema economy |
| required_manuscript_boundary | PASS | Cross-pipeline record portability |
| required_manuscript_boundary | PASS | public archival URL, DOI, release tag, and artifact license remain unassigned |
| forbidden_revision_phrase | PASS | uses the released ablation |
| forbidden_revision_phrase | PASS | source-syntax-valid |
| forbidden_revision_phrase | PASS | complete cross-compiler portability failure |
| forbidden_revision_phrase | PASS | The 0.15 line |
| forbidden_revision_phrase | PASS | rendered as zero |
| forbidden_revision_phrase | PASS | _claude_academic_advisor |
| forbidden_revision_phrase | PASS | recovery fraction |
| latex_log | PASS | main.log: clean for checked failures |
| latex_log | PASS | supplementary.log: clean for checked failures |

## Boundary

This validation checks internal consistency and landed artifacts. It does not close the pending public-archive/DOI decision, establish analyst utility, or establish cross-vendor generalization.
