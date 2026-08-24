# T25: Revise fidelity and scatter examples

## Context

Read `context/conversation-v007.md` and `results/T22-fidelity-scatter-visual-review-r01.md`.

## Scope and ownership

Edit only `examples/fidelity_multi_parameter.py` and `examples/scatter_with_simulation.py`. Preserve every synthetic fixture value and plotting grammar. Make fidelity's five categorical series use an explicit discrete package palette with intentional ordering and redundant marker roles rather than sampling a continuous colormap. Improve marker/line/legend restraint. Give scatter a cohesive warm simulation, dark structural experiment, and red highlighted-trace mapping derived from package palettes; fix the lost panel-(a) x-axis label and refine density/hierarchy without inventing points. Retain visible synthetic-data notices. Render candidates under `examples/figures/generated/candidate/` and format/check only the two owned scripts.

## Acceptance criteria

- All semantic colors come from `wesandersonpy`; no hard-coded hexadecimal colors are introduced.
- Fidelity's adjacent series remain visually distinct and the discrete API matches categorical semantics.
- Scatter uses color plus marker/line form, keeps its red highlighted trace, and restores readable panel labeling.
- Both scripts run in `wespy`; both candidate/reference pairs are inspected at original detail.
- Write `results/T25-fidelity-scatter-visual-revision-r01.md` with changes, commands, evidence, and remaining limitations.
