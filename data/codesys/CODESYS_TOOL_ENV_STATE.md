# CODESYS Tool Environment State

Evidence label: DERIVED_EVIDENCE

## Status

`CODESYS_TOOLING_REPAIR_PARTIAL`

This file records the CODESYS tooling repair authorized by `ADVISOR_REVIEW_V3A_AUTHORIZATION.md`. It documents tool environment state only. It does not claim CODESYS recovery.

## Before state

| Tool | Before status |
|---|---|
| global `binwalk` | `/home/admin1/.local/bin/binwalk` existed but failed with `ModuleNotFoundError: No module named 'binwalk.core'` |
| `unblob` | command not found |
| `r2` | available only when `LD_LIBRARY_PATH=/home/admin1/.local/lib/x86_64-linux-gnu` is set |
| `retdec-decompiler` | missing |
| `ida64` | missing |

## Repair actions

| Action | Result |
|---|---|
| Created project-local venv | `09_paper1_experiment_evidence/codesys_deep_dive/.codesys_tooling_venv` |
| Installed `unblob` in venv | success; `unblob --version` reports `26.6.4` |
| Tried `pip install git+https://github.com/ReFirmLabs/binwalk.git` in venv | failed; repository has no `setup.py` or `pyproject.toml` |
| Checked Rust/cargo path for current binwalk | blocked; `cargo` and `rustc` not found |
| Checked sudo path for apt install | blocked; `sudo` requires password |
| Downloaded Ubuntu `python3-binwalk` / `binwalk` debs with `apt-get download` | success; local extraction only, no system package install |
| Extracted debs under project-local path | `09_paper1_experiment_evidence/codesys_deep_dive/.apt_tools/extracted` |
| Verified local binwalk Python import | success via `PYTHONPATH=.../.apt_tools/extracted/usr/lib/python3/dist-packages` |

## After state

| Tool | After status |
|---|---|
| global `binwalk` | still broken; not modified |
| local apt-extracted `binwalk` | usable through `PYTHONPATH=.../.apt_tools/extracted/usr/lib/python3/dist-packages python3 .../.apt_tools/extracted/usr/bin/binwalk` |
| local apt-extracted binwalk smoke scan | one sample scan on `codesys__ARRAY_ABS.app` exited `0` and reported no signatures; this is a CLI repair check, not a CD-2 recovery rerun |
| venv `unblob` | installed and version-reported as `26.6.4`; no recovery trial run |

## Boundary

Allowed:

- binwalk has a project-local usable path.
- unblob is installed in a project-local venv.

Forbidden:

- Do not claim CODESYS recovery.
- Do not claim global system tooling has been repaired.
- Do not treat the one binwalk smoke scan as a new CD-2 recovery result.
