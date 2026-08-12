# CODESYS ICSREF Compatibility Report

Evidence label: DERIVED_EVIDENCE

## Status

`ICSREF_COMPATIBILITY_EVALUATED_REPORT_ONLY`

This report evaluates whether ICSREF can be used directly on the local PLC-BEAD CODESYS `.app` samples. It does not claim any CODESYS recovery.

## ICSREF acquisition

| Field | Value |
|---|---|
| Repository | `https://github.com/momalab/ICSREF.git` |
| Local path | `09_paper1_experiment_evidence/codesys_deep_dive/.external/ICSREF` |
| Clone mode | `--depth 1` |
| Stated scope | CODESYS binaries compiled with the CODESYS v2 compiler |
| Stated runtime | Python 2.7 |
| Stated radare2 requirement | radare2 v3.1.3 |

## Local environment compatibility

| Requirement | Local state | Compatibility |
|---|---|---|
| Python 2.7 | `python2.7` not found | blocked |
| Python 2 | `python2` not found | blocked |
| radare2 v3.1.3 | current r2 is different and needs local library path | not matched |
| Python packages | `angr`, `cmd2`, `dill`, `ujson`, `pygraphviz`, `pymodbus` missing from active Python 3 | blocked |
| local PLC-BEAD samples | `.app` extension, CODESYS v3-style dataset samples | not the `.PRG` input expected by ICSREF CLI |

## Static compatibility findings

| Finding | Evidence |
|---|---|
| ICSREF README states CODESYS v2 scope | `README.rst`: "binaries compiled with the CODESYS v2 compiler" |
| ICSREF install requires Python 2.7 | `INSTALL.md` |
| ICSREF interactive analyzer requires `.PRG` extension | `icsref.py` checks `filename[-4:].upper() != '.PRG'` |
| ICSREF `Program` parser assumes fixed PRG header offsets | `PRG_analysis.py` reads offsets at `0x20`, `0x2C`, and `0x44` |
| ICSREF function-boundary heuristic uses ARM prologue/epilogue byte patterns | `PRG_analysis.py` contains prologue/epilogue matching logic |

## Local sample probes

Five local samples were inspected for compatibility metadata:

| Sample | Suffix | Size bytes | First 16 bytes |
|---|---|---:|---|
| `codesys__ARRAY_ABS.app` | `.app` | 183880 | `8101cc00708480007270690071a08000` |
| `codesys__ARRAY_ADD.app` | `.app` | 184176 | `8101cc00708480007270690071a08000` |
| `codesys__ARRAY_INIT.app` | `.app` | 183888 | `8101cc00708480007270690071a08000` |
| `codesys__ARRAY_MUL.app` | `.app` | 184200 | `8101cc00708480007270690071a08000` |
| `codesys__ARRAY_SORT.app` | `.app` | 184832 | `8101cc00708480007270690071a08000` |

The samples are `.app` files, not `.PRG` files. The ICSREF CLI would reject them by extension before analysis. Bypassing the extension check would still require a Python 2.7 environment and validation that the v2 PRG header/function-boundary assumptions apply, which is not established.

## Conclusion

ICSREF is relevant prior art but is not directly compatible with the local PLC-BEAD CODESYS `.app` samples under the current environment.

Recommended status:

`ICSREF_NOT_DIRECTLY_COMPATIBLE_WITH_LOCAL_CODESYS_APP_SAMPLES`

## Boundary

Allowed:

- ICSREF is a published/open CODESYS v2 reverse-engineering framework.
- Local PLC-BEAD CODESYS `.app` samples do not match the ICSREF `.PRG`/Python 2.7 execution path.

Forbidden:

- Do not claim ICSREF failed to recover after a full configured run; no full Python 2.7 ICSREF environment was established.
- Do not claim CODESYS recovery is impossible.
- Do not use ICSREF code-region assumptions on local `.app` samples without a separate authorized compatibility bridge.
