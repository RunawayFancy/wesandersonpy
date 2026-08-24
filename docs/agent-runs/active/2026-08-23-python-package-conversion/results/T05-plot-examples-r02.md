# T05 result revision r02: V03 example corrections

## Task and context

- Task: correct V03-F01, V03-F02, and V03-F03 within the T05-owned example files.
- Context: `context/conversation-v004.md`, the approved plan, and `verification/V03-static-implementation.md`.
- Status: scoped corrections complete; human Python execution and independent reverification remain pending.

This report supersedes `T05-plot-examples-r01.md` for the corrected implementation state. The earlier report remains unchanged as part of the audit trail.

## Work performed

### V03-F01: configured line width

Manually reflowed every Python line longer than 88 characters across all five example scripts. The changes only restructure expressions, argument lists, comprehensions, and calls; they do not intentionally alter plotting behavior.

### V03-F02: semantic package-derived colors

- In `examples/scatter_with_simulation.py`, retained `FantasticFox1[3]` for the orange simulation layer, changed the experiment layer to contrasting blue `FantasticFox1[2]`, and changed the highlighted trace to red `FantasticFox1[4]`.
- In `examples/readout_calibration_rabi_subplots.py`, changed `ink` and its derived `neutral` role to the near-black last color from `wes.get_palette("Moonrise1")[-1]` instead of the pale first color.
- No hexadecimal color literal was added. All semantic colors remain obtained through the public `wesandersonpy` API.

### V03-F03: generated-output staging

- Changed every script's `DEFAULT_OUTPUT` to `examples/figures/generated/<script-name>.png` relative to the script directory.
- Updated all five first-pass commands in `examples/README.md` to use the ignored generated-output directory.
- Documented that only a human-reviewed, nonconfidential PNG rendered from the synthetic fixtures and checked for sensitive metadata may be copied or moved to `examples/figures/` for version control and README use.
- Preserved every CLI override and input/output collision guard.

## Files changed

- `examples/diagram_sequence_time_domain.py`
- `examples/multiple_iterations_faded.py`
- `examples/fidelity_multi_parameter.py`
- `examples/scatter_with_simulation.py`
- `examples/readout_calibration_rabi_subplots.py`
- `examples/README.md`
- `docs/agent-runs/active/2026-08-23-python-package-conversion/results/T05-plot-examples-r02.md`

No files under `examples/data/` and no prior task or verification reports were modified.

## Static evidence and checks

- A PowerShell line-length scan over exactly five `examples/*.py` files found zero lines longer than 88 characters.
- A source scan confirmed the scatter role indices are simulation `3`, experiment `2`, and highlighted simulation `4` from `FantasticFox1`.
- A source scan confirmed readout `ink` is `wes.get_palette("Moonrise1")[-1]` and `neutral` delegates to that package-derived value.
- A hexadecimal-literal search found no hard-coded palette colors in the example scripts.
- Source and documentation scans confirmed all five default output paths and first-pass commands contain `examples/figures/generated/`.
- `examples/README.md` contains the human review and promotion gate for approved PNGs.
- No Python interpreter, example renderer, Ruff, pytest, mypy, or build command was run.

## Limitations and recommended next action

Runtime, formatting-tool, and visual evidence remain human-only under `AGENT.md`. The host should request independent static reverification of V03-F01 through V03-F03, then have the human run Ruff and render all five staged PNGs. Only human-approved nonconfidential images should be promoted from `examples/figures/generated/` to `examples/figures/`.
