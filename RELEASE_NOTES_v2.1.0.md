# SCAA-PLC artifact v2.1.0 release notes

**Evidence label:** `DERIVED_EVIDENCE`

## Added since v2.0.0

- Five-field bivariate support/closure cards for 2,431 PLC-BEAD records and 10 OpenPLC relation-backed records.
- Stored ten-fold source-role predictions plus package-local replay from bivariate card signatures.
- Separate EC1 construction/identity check over 7,293 representation rows.
- Six record-fault injection outputs.
- Complete 56-row OpenPLC eligibility registry with 10 included and 46 excluded rows.
- Two closed Schneider/ARM VxWorks evidence cards and hash-addressed function-signature summaries; no proprietary payload is included.
- Workflow Run RO-Crate 0.5 and PROV-O export, portable official-validator summaries, and current-environment revalidation record.
- Author-defined report-requirement matrix with verified 2/9, 6/9, and 9/9 counts.
- Five-file CODESYS tool-path probe and compatibility reports.
- Scientifically locked JSS CAS sources, current vector figures, updated bibliography, and preserved v2.0 manuscript snapshot.
- Extended validator, release-metadata rebuilder, complete checksum set, and clean-room validation log.

## Corrected

The RO-Crate recommended-level count is 134/135 checks, not 133/135. One recommended check emitted two findings with the same identifier. The 55/55 required-profile result is unchanged.

## Publication identity

- GitHub release: `https://github.com/Mewtwoz/SCAA_PLC_ARTIFACT/releases/tag/v2.1.0`
- Release commit: `7f87738ecbf19c09d5d63bee99e6de86ac32bce1`
- Zenodo version DOI: `10.5281/zenodo.21896622`
- Zenodo concept DOI: `10.5281/zenodo.21869717`

## Post-publication clean-clone erratum (2026-08-12)

A clean checkout and the public Zenodo ZIP expose an integrity-metadata defect: 18 text CSV files are stored with LF endings by Git, while the v2.1.0 checksum manifest was generated from a CRLF working tree. Consequently, v2.1.0 reports failure only for those byte-level checksum entries and `checksums_match`; all other 10 core checks and all 39 extended scientific/package checks pass.

The normalized checksum manifests are corrected on `main` at commit `55b57f2d9f92d928daacb15e66c192c23f1e7775`, where a Linux clean clone passes 11/11 core and 39/39 extended checks. The v2.1.0 tag and Zenodo record remain immutable and were not moved or overwritten. A subsequent corrective release is required for a DOI archive whose bundled checksum manifest passes unchanged.
