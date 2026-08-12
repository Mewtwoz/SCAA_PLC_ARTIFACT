# Workflow Run RO-Crate and PROV-O validation report

**Evidence label:** `DERIVED_EVIDENCE`

**Date:** 2026-08-11

## Exported run

The crate records a deterministic Python workflow that validates and summarizes three derived bivariate evidence-card inputs. It declares the workflow as the crate `mainEntity`, represents execution with a `CreateAction`, records the three input files as `object`, and records the summary CSV and validation JSON as `result`. The crate contains no raw Schneider firmware payload.

A companion PROV-O Turtle graph represents the input and output entities, the summary activity, and the responsible agent. The validator confirms the presence of `prov:used`, `prov:wasGeneratedBy`, and `prov:wasAssociatedWith` links.

## Official profile validation

Validation used `rocrate-validator 0.11.3_b959343+2-dirty` against Workflow Run RO-Crate 0.5 and inherited profiles.

Required-profile command:

```bash
rocrate-validator validate --profile-identifier workflow-run-crate \
  --requirement-severity required --relative-root-path . \
  --output-format json --output-file ROCRATE_VALIDATION_REQUIRED.json \
  workflow_run_rocrate
```

The recommended-level run uses the same command with `--requirement-severity recommended` and writes `ROCRATE_VALIDATION_RECOMMENDED.json`.

| Validation level | Passed | Total | Exit | Interpretation |
|---|---:|---:|---:|---|
| REQUIRED | 55 | 55 | 0 | All mandatory checks pass. |
| REQUIRED + RECOMMENDED | 134 | 135 | 1 | One recommended check failed with two findings. |

Both findings belong to recommended check `process-run-crate-0.5_5.1`: the local workflow-file identifier should be an absolute URI. The relative identifier is retained because it also addresses the executable workflow file physically packaged in the crate. The findings are reported as non-blocking `SHOULD` advisories and are not represented as full warning-free conformance.

## Internal validation

Internal checks confirm the Workflow Run context and profile declaration, one `CreateAction`, three inputs, two outputs, a non-empty 21-row summary, two closed Schneider cards, explicit absence of a Schneider relation graph, absence of raw proprietary payloads, and the required PROV-O link families.

Final status: `PASS_REQUIRED_PROFILE_WITH_LOCAL_ID_ADVISORY_AND_HUMAN_RESULTS_MISSING`.

## Interpretation boundary

Profile conformance establishes the structure of the exported run package. It does not establish correctness of binary observations, completeness of the evidence taxonomy, analyst utility, semantic recovery, vulnerability detection, or external generalization.
