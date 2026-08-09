# Ungated lexical transfer probe

**Evidence label:** `DERIVED_EVIDENCE`

## Design

The production SA-001 rule remains scoped to GEB. This probe removes only the toolchain gate and applies the lexical predicate `core_symbol_text contains dt_FB_` unchanged to GEB, OpenPLC v2, and OpenPLC v3. The reference is a separately extracted Structured Text syntax predicate from the same PLC-BEAD snapshot.

| Toolchain | Production scope | n | Source FB | Probe positive | TP | FP | FN | TN | Recall |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GEB | IN_SCOPE | 616 | 353 | 353 | 353 | 0 | 0 | 263 | 1.000000 |
| OpenPLCv2 | OUT_OF_SCOPE | 618 | 359 | 0 | 0 | 0 | 359 | 259 | 0.000000 |
| OpenPLCv3 | OUT_OF_SCOPE | 639 | 376 | 0 | 0 | 0 | 376 | 263 | 0.000000 |

## Boundary

The OpenPLC rows are out of scope for the production SA-001 rule. Their FN counts belong only to this ungated lexical transfer probe. The result tests reuse of one GEB naming pattern; it does not test semantic recovery, runtime roles, function boundaries, or vulnerability detection.
