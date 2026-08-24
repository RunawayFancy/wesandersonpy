# T23: Readout and Rabi baseline visual review

## Context

Read `context/conversation-v007.md`, `examples/README.md`, the assigned script, and its synthetic fixture README.

## Scope

Activate `wespy`. Render `readout_calibration_rabi_subplots.py` unchanged into `examples/figures/generated/baseline/`. Inspect the generated PNG and corresponding reference PNG under `plotting_example/` at original detail. Diagnose panel layout, repeated semantic color roles across schematic, tone, IQ, population, and spin panels, contrast, hierarchy, density, legend/readability, and concrete harmony improvements. Also audit whether the proposed palette roles communicate categories and progressions consistently.

## Authorized outputs

The generated baseline PNG and `results/T23-readout-visual-review-r01.md`.

## Prohibited actions

Do not edit scripts, fixtures, package code, references, or existing reports. Do not extract numerical data from reference images or use experimental data.

## Acceptance criteria

- The script completes in `wespy` using only bundled synthetic inputs.
- The image pair receives a specific qualitative comparison across all panel groups.
- Findings distinguish preserved key features from color/layout shortcomings and recommend package-palette-based changes without applying them.
