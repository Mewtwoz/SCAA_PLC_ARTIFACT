# v10 standards and external-corpus experimental extension

**Evidence label:** `DERIVED_EVIDENCE`

**Date:** 2026-08-11

## Purpose

This extension addresses two bounded validity risks in the JSS manuscript: the absence of a standards-validated provenance package and the former absence of a vendor/architecture adapter outside OpenPLC-derived x86-64 inputs. It does not evaluate vulnerability detection, semantic recovery, function-boundary accuracy, or human utility.

## Independent Schneider/ARM adapter

The adapter reads two legally acquired Schneider Electric Modicon M340 BMXP341000 archives: SV340 and SV370. The archive and embedded VxWorks-payload SHA-256 values replay against the confirmed intake inventory. Architecture-aware radare2 function lists are separately hash-addressed and contain 7,733 and 7,920 heuristic function boundaries. Multiplicity-aware matching of `(complexity, size)` signatures produces 7,434 matched instances, or 0.961335 relative to the SV340 function-list count.

Two bivariate evidence cards are constructed. EC1 and EC3 are `supported/not_required` because function candidates and static summary records exist. EC2, EC4, and EC5 are `unobserved/explained` because core-logic identity, declared state role, and a retained relation graph are unavailable. Both card-level closure values are `complete`. No CVE, vulnerable/fixed, behavioral-patch, semantic, or function-correctness label is assigned.

The builder reads the proprietary payload members in memory and does not copy them into the v10 directory or the Workflow Run RO-Crate. Permanent outputs contain only hashes, derived profiles, function-list summaries, evidence cards, and validation results.

## Cross-corpus deterministic workflow

The workflow accepts three derived card tables: 2,431 PLC-BEAD cards, 10 OpenPLC/radare2 cards, and two Schneider/VxWorks cards. It checks the support/closure vocabulary and card-closure invariant before emitting a 21-row corpus-by-field/state summary plus a machine-readable validation result. The workflow exits successfully and records three inputs and two outputs.

## Result boundary

The extension demonstrates that the same bivariate reporting contract can encode a second extraction shape and an independently sourced vendor/architecture pair while preserving unavailable-field closure. Two versions of one product are not evidence of broad vendor portability. The 7,733/7,920 counts are tool-produced heuristic boundaries, not a ground-truth recovery score. The 0.961335 signature ratio is a structural count comparison, not semantic equivalence or confirmation of a security patch.

## Principal outputs

- `SCHNEIDER_EXTERNAL_CORPUS_PROFILE.csv`
- `SCHNEIDER_EXTERNAL_EVIDENCE_CARDS.csv`
- `SCHNEIDER_FUNCTION_SIGNATURE_METRICS.csv`
- `SCHNEIDER_EXTERNAL_ADAPTER_VALIDATION.json`
- `workflow_run_rocrate/`
- `V10_BUILD_RESULT.json`
- `V10_VALIDATION_RESULT.json`
