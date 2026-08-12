# OpenPLC Adapter Eligibility Report

Evidence label: `DERIVED_EVIDENCE`

## Operational rule

The v2.6 manifest contains **56** discovered native OpenPLC-derived binaries. A row is eligible for the landed evidence-card adapter only when its `sample_id` occurs in `RELATION_EXTRACTION_RECORDS_v2_3.csv` and every joined relation row carries the same SHA-256 as the manifest row. This deterministic rule reconstructs the landed adapter input boundary; it is not a prospective sampling plan, a quality ranking, or a semantic filter.

The rule includes **10** relation-backed binaries and excludes **46** binaries because no landed relation rows exist for them. No relation-backed row fails the SHA-256 join. The included binaries account for all **6,657** landed relation rows.

## Compiler stratum

| Compiler | Discovered | Included | Excluded |
|---|---:|---:|---:|
| clang | 10 | 0 | 10 |
| gcc | 46 | 10 | 36 |

## Optimization stratum

| Optimization | Discovered | Included | Excluded |
|---|---:|---:|---:|
| O0 | 22 | 9 | 13 |
| O1 | 4 | 0 | 4 |
| O2 | 22 | 0 | 22 |
| O3 | 4 | 0 | 4 |
| project_O2 | 4 | 1 | 3 |

## Stripping stratum

| Symbol status | Discovered | Included | Excluded |
|---|---:|---:|---:|
| stripped | 28 | 8 | 20 |
| unstripped | 28 | 2 | 26 |

## Interpretation boundary

The 46 excluded manifest rows are real built binaries, but the landed relation table contains no adapter input for them. They therefore remain visible as `EXCLUDED_NO_LANDED_RELATION_ROWS`; they are not silently removed from the starting population. Inclusion establishes only that a hash-consistent relation record can be joined to a manifest sample. It does not establish relation correctness, semantic completeness, vulnerability detection, or adapter portability.

Machine-readable details are in `OPENPLC_ADAPTER_ELIGIBILITY_FLOW.csv` and `OPENPLC_ADAPTER_ELIGIBILITY_SUMMARY.csv`. Validation status: `PASS`.
