# T22: Fidelity and scatter baseline visual review

## Context

Read `context/conversation-v007.md`, `examples/README.md`, the two assigned scripts, and their synthetic fixture READMEs.

## Scope

Activate `wespy`. Render `fidelity_multi_parameter.py` and `scatter_with_simulation.py` unchanged into `examples/figures/generated/baseline/`. Inspect each generated PNG and its corresponding reference PNG under `plotting_example/` at original detail. Diagnose structural fidelity, categorical differentiation, continuous versus discrete color semantics, highlighted simulation result, contrast, legends, and concrete harmony improvements.

## Authorized outputs

Generated baseline PNGs and `results/T22-fidelity-scatter-visual-review-r01.md`.

## Prohibited actions

Do not edit scripts, fixtures, package code, references, or existing reports. Do not extract numerical data from reference images or use experimental data.

## Acceptance criteria

- Both scripts complete in `wespy` using only bundled synthetic inputs.
- Both image pairs receive specific qualitative comparison.
- Findings distinguish preserved key features from color/layout shortcomings and recommend package-palette-based changes without applying them.
