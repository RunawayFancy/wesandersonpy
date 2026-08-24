# T05: Manufacturing plot examples

## Context

Use `context/conversation-v001.md`, the approved plan, T03 outputs, and human-provided nonconfidential plot-case specifications.

## Scope

Create one readable script per approved manufacturing plotting case, initially `examples/fidelity_multi_parameter.py` and `examples/readout_calibration_rabi_subplots.py`, using the installed `wesandersonpy` package for every color or colormap.

## Authorized inputs

Human descriptions of plot type, column names, units, color mapping, palette, styling, output filename, and a shareable visual reference. These specifications must exclude measurements and experimental values.

## Prohibited inputs and actions

Do not open, copy, transform, summarize, or write experimental data. Do not open or inspect the two reference PNGs. Do not fabricate results. Do not execute the scripts or generate purported result images.

## Expected outputs

Individual scripts under `examples/`, an `examples/README.md`, input schema validation, command-line input/output arguments, and exact human-run instructions.

## Acceptance criteria

Every approved case has one discoverable script, data loading is outside the core package, scripts do not hard-code palette values, outputs are deterministic given the same input, and source data is never overwritten.

## Dependencies

Human case specifications and T03.
