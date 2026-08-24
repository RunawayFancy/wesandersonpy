# T05 result: manufacturing plotting examples

## Task and context

- Task: T05, implement one readable Matplotlib script for each of the five approved manufacturing-style plotting cases.
- Context used: `context/conversation-v004.md` and the approved `plan.md`.
- Status: implementation complete; Python execution and visual approval remain assigned to the human maintainer.

## Sources inspected

- `AGENT.md`, the approved plan, and `tasks/T05-manufacturing-examples.md`.
- `results/T09-sequence-iterations-r01.md`, `results/T10-fidelity-scatter-r02.md`, and `results/T11-readout-rabi-r02.md`.
- All five `examples/data/*/README.md` files and all 14 verified synthetic CSV fixtures.
- The implemented public package surface in `src/wesandersonpy/__init__.py` and `src/wesandersonpy/palettes.py` to confirm the approved `get_palette` and `get_colormap` signatures.

## Work performed

Created exactly five standalone CLI scripts:

- `examples/diagram_sequence_time_domain.py` renders a sequence schematic, a time-response panel, two population panels, an inset, aligned transition guides, and level annotations.
- `examples/multiple_iterations_faded.py` renders repeated marker-only traces with monotonically increasing opacity and a categorical legend.
- `examples/fidelity_multi_parameter.py` renders five marker/line series on a logarithmic axis with separate dotted asymptote layers.
- `examples/scatter_with_simulation.py` renders a tall branch-scatter panel and two shared-axis probability strips, including the distinct highlighted illustrative trace.
- `examples/readout_calibration_rabi_subplots.py` renders the schematic, paired tone axes, IQ triptych with a separate background layer, three population rows, and the expectation-value row with an SU(2)-style conceptual inset.

Also created `examples/README.md` with exact human-run commands, a figure index, input/output behavior, synthetic-data cautions, and the requested feedback contract.

All visible semantic colors come from `wesandersonpy.get_palette` or `wesandersonpy.get_colormap`; no palette hexadecimal values are copied into the scripts. Multi-file cases accept `--data-dir`; the single-file faded-iteration case accepts `--input`; all scripts accept `--output`. Defaults point to the reviewed fixtures relative to each script. Each script validates required columns, refuses to overwrite an input CSV, creates only the selected output directory, saves at 180 DPI, closes the figure in a `finally` block, and includes both a docstring disclaimer and visible synthetic-data footer.

## Files changed

- `examples/diagram_sequence_time_domain.py`
- `examples/multiple_iterations_faded.py`
- `examples/fidelity_multi_parameter.py`
- `examples/scatter_with_simulation.py`
- `examples/readout_calibration_rabi_subplots.py`
- `examples/README.md`
- `docs/agent-runs/active/2026-08-23-python-package-conversion/results/T05-plot-examples-r01.md`

No files under `examples/data/` were edited.

## Static evidence and checks

- PowerShell inventory confirmed exactly five `examples/*.py` files with the names required by the approved plan.
- Text inspection confirmed that every script exposes its required input option and `--output`, calls `figure.savefig`, and closes with `plt.close` in a `finally` block.
- A hexadecimal-color search found no hard-coded palette hex values in the example scripts.
- The implemented package data confirms that `Zissou1`, `Darjeeling1`, `FantasticFox1`, `Moonrise1`, and `GrandBudapest1` exist and have enough source colors for every direct index used.
- All 14 expected CSV input paths exist.
- A PowerShell line-length audit found no Python lines longer than 100 characters.
- All edited files were reread after patching. No Python file, test runner, formatter, linter, type checker, renderer, or build command was executed, in accordance with `AGENT.md` and context v004.

## Limitations and unresolved verification

- Syntax, imports, typing, Matplotlib compatibility, and rendered layout require human execution because agents are prohibited from running Python in this project.
- The output figures have not been visually inspected. Typography, annotation overlap, and spacing may need a later revision after the human returns the five PNGs.
- Alternate input paths are supported by the CLI contract, but the examples are designed and documented around the reviewed synthetic schemas. The README explicitly instructs users not to pass confidential or experimental data.

## Recommended next action

The host should send the five commands in `examples/README.md` to the human maintainer. The human should return the Python and installed-package versions, console output, and all five generated PNGs for independent visual review before any exhibit is committed or embedded in the root README.
