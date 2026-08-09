# Cross-pipeline evidence-card adapter report

**Evidence label:** `DERIVED_EVIDENCE`

## Inputs

The adapter uses a separate local evidence package: hash-profiled native OpenPLC ELF
binaries and radare2/r2pipe relation records. It does not reuse the PLC-BEAD `nm`
feature table.

## Results

- Cards emitted: 10
- Relation rows joined: 6657
- Relation types represented: 8
- Uncertainty rows joined: 20
- Manifest/relation/uncertainty SHA256 joins: all matched
- Cards with function identifiers: 10
- Cards with function-call/basic-block graph relations: 10
- Cards with both static-analysis and label-scope uncertainty: 10

The adapter populated direct observability and graph channels, retained partial
claim-support fields, and preserved explicit uncertainty. This shows that the record
contract can be instantiated over a second binary-analysis pipeline.

## Boundary

The ten binaries are locally compiled OpenPLC-derived x86-64 ELFs, not an independent
vendor ecosystem. The result establishes schema/record portability only. It does not
establish semantic completeness, function correctness, behavioral patch confirmation,
vulnerability detection, analyst utility, or broad external generalization.
