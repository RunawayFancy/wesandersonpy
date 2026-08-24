# T21: Diagram and iteration baseline visual review

## Context

Read `context/conversation-v007.md`, `examples/README.md`, the two assigned scripts, and their synthetic fixture READMEs.

## Scope

Activate `wespy`. Render `diagram_sequence_time_domain.py` and `multiple_iterations_faded.py` unchanged into `examples/figures/generated/baseline/`. Inspect each generated PNG and its correspondingly named reference PNG under `plotting_example/` at original detail. Diagnose layout fidelity, plot grammar, color harmony, contrast, hierarchy, fading behavior, legend/readability, and concrete improvement opportunities.

## Authorized outputs

Generated baseline PNGs and `results/T21-diagram-iterations-visual-review-r01.md`.

## Prohibited actions

Do not edit scripts, fixtures, package code, references, or existing reports. Do not extract numerical data from reference images or use experimental data.

## Acceptance criteria

- Both scripts complete in `wespy` using only bundled synthetic inputs.
- Both image pairs receive specific qualitative comparison.
- Findings distinguish preserved key features from color/layout shortcomings and recommend package-palette-based changes without applying them.
