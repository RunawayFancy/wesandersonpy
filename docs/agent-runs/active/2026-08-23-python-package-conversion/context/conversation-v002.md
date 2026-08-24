# Conversation context v002

## Objective

Continue using the approved planning record while performing a newly authorized bounded subtask: inspect five local plot-reference PNGs, record their visual and layout characteristics, and create clearly labeled artificial datasets suitable for later example scripts.

## Authorization added 2026-08-23

The human explicitly authorized the agents to read the updated reference plot images and asked for subagents to generate artificial data for later use. This authorizes image inspection, layout characterization, and writes confined to distinct synthetic-data subdirectories and task result reports. It does not authorize the wider package implementation, Git initialization, source relocation, dependency installation, Python execution, or publishing.

## Reference images

- `plotting_example/Diagram_sequence_timedomain_dataplot_with_multi_params.png`
- `plotting_example/Fidelity_plots_with_multi_params.png`
- `plotting_example/Multiple_iteration_data_with_faded_effect.png`
- `plotting_example/Multiple_subplots_readout_calibration_rabi_data.png`
- `plotting_example/Scattered_dataplot_with_highlight_simulation_result.png`

## Data-integrity rules

- Inspect images for layout, mark types, panel structure, labels, color roles, and qualitative trends only.
- Do not digitize, transcribe, or claim exact values from the reference images.
- Do not present synthetic data as experimental, measured, fitted, validated, or physically meaningful.
- Add a clear synthetic-data notice in every assigned data directory.
- Use invented parameter names only when a reference label cannot be safely or clearly identified, and document that choice.
- Do not run Python files.

## Task assignments

- T09: sequence/time-domain diagram and faded-iteration plot.
- T10: fidelity plot and scatter plot with highlighted simulation.
- T11: readout-calibration/Rabi subplot figure.

## Expected handoff

Each assigned agent writes only its assigned result report and synthetic-data directories. The host reviews the artifacts, reconciles naming and schema consistency without rewriting agent reports, and asks the human to approve the characteristics before plotting scripts are implemented.
