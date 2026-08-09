# Schema derivation and content-validity boundary

**Evidence label:** `DERIVED_EVIDENCE`

## Design requirements

The schema was derived to preserve five requirements: sample and hash identity; observation-to-rule provenance; distinction between unsupported and negative findings; typed uncertainty closure; and run-level reproducibility. These requirements connect binary-analysis uncertainty, computational provenance, and empirical-software-reporting guidance. They are requirements for a reporting contract, not claims of semantic completeness.

## Empirical failure cases

The initial categories were exercised against three landed failure families: CODESYS container/tool mismatch, ambiguous state-role naming, and cross-pipeline relation/label-scope uncertainty. EC1--EC6 are all instantiated in the primary population. Observed U-codes are: U01, U02, U11, U13, U09b. Defined but unobserved codes are: U03, U04, U05, U06, U07, U08, U09, U10, U12, U14, U09a. Unobserved codes are not evidence of saturation.

## Validation status

The package reports slot and code coverage plus cross-pipeline contract instantiation. Independent coder agreement, expert content validation, and a new-category saturation study have not been completed. Accordingly, the paper describes EC1--EC6 and U01--U14 as chosen provenance categories, not a complete or universally validated taxonomy. The accompanying reviewer task protocol is `TEMPLATE_ONLY` until independent responses exist.
