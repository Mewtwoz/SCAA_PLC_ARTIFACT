# SCAA-PLC JSS Artifact v2.1.0

**Evidence label:** `DERIVED_EVIDENCE`

This release synchronizes the public v2.0 artifact with the scientifically locked JSS content. It packages the bivariate evidence contract, the source-role and EC1 construction-check records, fault-injection outputs, OpenPLC eligibility audit, bounded Schneider/ARM adapter, author-defined report-requirement check, Workflow Run RO-Crate/PROV-O export, and the current CAS manuscript-support files.

The immutable release is available as GitHub tag [`v2.1.0`](https://github.com/Mewtwoz/SCAA_PLC_ARTIFACT/releases/tag/v2.1.0), fixed at commit `7f87738ecbf19c09d5d63bee99e6de86ac32bce1`. Zenodo archives that release under version DOI [`10.5281/zenodo.21896622`](https://doi.org/10.5281/zenodo.21896622) and concept DOI [`10.5281/zenodo.21869717`](https://doi.org/10.5281/zenodo.21869717).

## Quick start

From the package root, run:

```bash
python3 run_artifact.py
```

Only Python 3's standard library is required. The expected final status is `PASS`. The command verifies the portable checksum set, core population and relation surfaces, source-role replay, the EC1 construction check, bivariate nominal states, six fault injections, OpenPLC eligibility, Schneider card closure, report-requirement counts, Workflow Run RO-Crate structure, PROV-O links, and normalized official-validator counts.

For the extended checks alone:

```bash
python3 scripts/extended/validate_extended_evidence.py
```

After an intentional payload change, rebuild integrity metadata with:

```bash
python3 scripts/rebuild_release_metadata.py
```

## Package map

- `data/current/`: v6 full-population inputs and results retained for lineage and source-role metric replay.
- `data/v9/`: five-field bivariate cards, predictions, metrics, state counts, fault-injection results, provenance crosswalk, and report-structure controls.
- `data/v10/`: two-card Schneider/ARM adapter, function-signature summaries, Workflow Run RO-Crate, PROV-O export, and portable summaries of official RO-Crate validator outputs.
- `data/v11/`: the complete 56-to-10 OpenPLC adapter eligibility registry and the 2/9, 6/9, 9/9 author-defined requirement matrix.
- `data/cross_pipeline/`: the 56-row native manifest, 6,657 relation rows, and 20 uncertainty rows used by the bounded OpenPLC instantiation. Raw binaries are excluded.
- `data/codesys/`: the five-file public-tool probe and compatibility/environment reports.
- `data/config/`: PLC-BEAD manifest, deterministic split, and mapping rules.
- `scripts/extended/`: package-local validation of v9--v11 claims and counts.
- `scripts/verify_plcbead_acquisition.py`: optional hash replay against a separately acquired PLC-BEAD checkout.
- `manuscript_support/`: scientifically locked CAS sources, bibliography, and current vector figures. `v2.0_legacy/` preserves the prior public-release manuscript snapshot for provenance only.
- `history/`: non-contributory classifier and ablation chronology; these files are not evidence for the current reporting-method claims.
- `checksums/` and `ARTIFACT_MANIFEST.csv`: stable payload checksums and the complete file inventory.

## Reproduction boundary

The one-command validator replays and checks the derived reporting-analysis surface. It does not rerun raw binary/source extraction. Re-running GNU `nm` requires a separately acquired PLC-BEAD snapshot; re-running radare2 extraction requires the excluded OpenPLC binaries and the recorded extraction environment. The Schneider firmware archives and payloads are not redistributed; the package contains only author-generated, hash-addressed derived records.

The EC1 tool-output target is verified as a lossless construction/identity check because it is derived from the EC1 support state. The source-function-block task is the only nontrivial RQ2 decoder task. Neither check establishes semantic correctness, vulnerability-detection performance, or analyst utility.

## Third-party acquisition boundary

Raw PLC-BEAD files are not redistributed because the examined upstream snapshot contains no explicit license file. Acquire the dataset from its upstream repository under the terms supplied by its maintainers, then run:

```bash
python3 scripts/verify_plcbead_acquisition.py /path/to/PLC-BEAD
```

This verifies all 2,431 binary hashes without copying upstream inputs into the package. See `THIRD_PARTY_NOTICES.md` for OpenPLC and Schneider boundaries.

## Licenses and publication identity

Author-generated code and documentation are released under BSD-3-Clause (`LICENSE`). Author-generated derived data are released under CC BY 4.0 (`LICENSE-DATA`). These grants do not cover separately acquired upstream source code, PLC-BEAD binaries, OpenPLC binaries, or Schneider firmware.

The GitHub release/tag, full commit, Zenodo version DOI, and Zenodo concept DOI above identify v2.1.0. The prior v2.0 DOI remains valid for its earlier immutable version but does not identify this expanded tree.
