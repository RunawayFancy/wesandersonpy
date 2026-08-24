# V01: Independent synthetic-data verification

## Verification identity and verdict

- Task: T12, independent verification against `context/conversation-v002.md`.
- Inspection date: 2026-08-23.
- Status: **FAIL for the complete five-case set; four cases pass and one requires data revision before plotting-script implementation.**
- Human-review readiness: the diagram/sequence, multiple-iterations, fidelity, and scatter/simulation fixtures are ready for qualitative human review. The readout-calibration/Rabi fixture is not yet ready for approval because two visible data layers cannot be reproduced from its current CSVs as documented.

## Scope and methods

I independently inspected the five authorized PNGs at original resolution, then reviewed every README and CSV in the five authorized `examples/data/` directories. I compared panel geometry, axes, marks, color roles, legends/direct labels, annotations, and qualitative trends against the T09 through T11 reports. I used read-only PowerShell operations (`Get-Content`, `Import-Csv`, grouping, uniqueness checks, and numeric range summaries) to examine schemas, row counts, category coverage, blanks, duplicate rows, and provenance fields. I did not run Python, render any plotting script, digitize reference values, or assess scientific validity.

Evidence inspected:

- `plotting_example/Diagram_sequence_timedomain_dataplot_with_multi_params.png`
- `plotting_example/Fidelity_plots_with_multi_params.png`
- `plotting_example/Multiple_iteration_data_with_faded_effect.png`
- `plotting_example/Multiple_subplots_readout_calibration_rabi_data.png`
- `plotting_example/Scattered_dataplot_with_highlight_simulation_result.png`
- All README and CSV files under `examples/data/diagram_sequence/`, `examples/data/multiple_iterations/`, `examples/data/fidelity_multi_parameter/`, `examples/data/scatter_simulation/`, and `examples/data/readout_calibration_rabi/`
- T09 r01, T10 r02, and T11 r01 result reports

## Visual comparison and case results

### Diagram, sequence, and population sweeps: PASS

The T09 characterization accurately identifies the four vertically arranged regions: a two-channel sequence schematic, an early-peaking and slowly decaying response panel, and two aligned multi-state population panels with a shared transition guide. It also correctly records the marker-only state series, the upper population inset and callout, direct preparation labels, and energy-ladder annotations. The data provide all data-bearing layers: four named sequence events, paired point/guide response columns, and five state series for each of two preparations. Inset bounds, guide positions, baselines, callout geometry, and ladder drawings can appropriately remain presentation configuration.

### Multiple faded iterations: PASS

The reference is correctly characterized as one wide population panel with three categorical marker series, repeated lower-opacity iterations, and a tan vertical dashed guide. The CSV contains four fade ranks for each of `P0`, `P1`, and `P7` at a shared 11-point control grid, which is sufficient to exercise categorical colors, repeated translucent clouds, and an opaque newest trace. Exact point density and alpha tuning are optional visual refinements.

### Fidelity multi-parameter plot: PASS

The T10 report correctly records the single near-square panel, logarithmic horizontal axis, five marker/line combinations, marker identities, lower-left legend, and separate right-side dotted asymptotes. The curve and asymptote tables include all five parameter categories, a common positive 14-point logarithmic coordinate grid, separate marker and line ordinates, and one ordered asymptote segment per category. The invented curves reproduce the necessary qualitative ordering and the irregular low-`j = 8` shoulder without claiming source values.

### Scatter with highlighted simulation: PASS

The three-panel height hierarchy, branch and outlier layers, source marker/color distinctions, red highlighted line, compact probability panels, and legend placements are accurately characterized. The CSVs separate four nominal branches by source, an experimental-style outlier layer by group, and panel-b/panel-c probability sources including the panel-b highlighted simulation. The data cover the visible regimes and notch/depression behaviors. Their point density is lower than the reference, but every distinct visible data layer is represented and the schema is usable; densification is optional rather than required for structural acceptance.

### Readout-calibration and Rabi composite: FAIL

The T11 report accurately captures the asymmetric four-region layout, nested tone-response axes, three IQ panels, four pulse-duration rows, direct labels, energy ladders, and SU(2) annotation. The sequence, Rabi-population, and spin-expectation tables contain the relevant categorical and trace roles. However, the tone and IQ fixtures do not fully cover two visible layers:

1. Each of the nine tone-response states has only five detuning values in a state-specific local interval of width `0.8 MHz`; the intervals shift from `-1.55..-0.75` for state 8 to `0.08..0.88` for state 0. In the reference, every colored response curve traverses essentially the full shared detuning axis. The README proposes interpolation, but interpolation of these disjoint local domains cannot produce the visible full-width baselines without undocumented extrapolation or a separately invented model.
2. `iq_scatter.csv` has six state-labeled cluster seeds for each panel/state combination and no point-role field or separate rows for the sparse background/outlier layer that is visibly present, especially in the right IQ panel. Deterministic jitter can increase cluster density, but it does not identify or reproduce that distinct background layer.

## CSV schema and count observations

| Case | Files and rows | Structural observations | Result |
|---|---:|---|---|
| Diagram/sequence | `sequence_events.csv` 4; `time_domain_response.csv` 31; `population_sweeps.csv` 110 | Two preparations x five states x eleven control points; paired response columns; no blank cells or duplicate full rows | Pass |
| Multiple iterations | `iteration_populations.csv` 132 | Four iterations x three series x eleven shared control points; one consistent fade rank per iteration; no blanks or duplicate full rows | Pass |
| Fidelity | `fidelity_curves.csv` 70; `fidelity_asymptotes.csv` 5 | Five parameters x fourteen positive x-values plus one asymptote per parameter; bounded fidelity values and explicit row provenance | Pass |
| Scatter/simulation | `panel_a_branches.csv` 78; `panel_a_outliers.csv` 23; `panels_bc_probabilities.csv` 94 | Four branch identities with both sources, three outlier groups, all panel-b/panel-c sources, bounded probabilities, and explicit row provenance | Pass |
| Readout/Rabi | `sequence_primitives.csv` 9; `tone_response.csv` 45; `iq_scatter.csv` 60; `rabi_populations.csv` 144; `spin_expectations.csv` 27 | Expected sequence roles, nine tone states, ten panel/state IQ groups, three Rabi cases with dominant/minor traces, and three expectation components; tone-domain and IQ-background coverage defects remain | Fail |

All CSVs parsed as rectangular tables. No duplicate complete rows were found. The 18 blank cells in `sequence_primitives.csv` occur only in optional `amplitude`, `repeat_count`, or `label` fields where the primitive kind does not require them. Numeric columns used in the summaries parsed successfully. Population and probability columns are bounded in the expected plotting range; the response marker maximum of `1.012` is consistent with the README's approximate normalization rather than a claim of exact probability normalization.

## Disclaimer and provenance checks

Every data directory has a prominent README notice stating that its values are synthetic, non-experimental, independently invented, not digitized, and unsuitable for scientific inference. No README or CSV claims that values are measured, experimentally valid, fitted, calibrated, or physically meaningful. The fidelity and scatter/simulation CSVs additionally carry `data_origin=synthetic_non_experimental` on every row. The other three directories rely on directory-level README provenance; adding the same row-level field would improve detached-file safety but is not required to resolve the present acceptance defects.

The `source=experiment` rows in the scatter fixture do not make an experimental-validity claim because each such row also carries the explicit synthetic origin field and the directory notice explains that source labels only reproduce plot grammar.

## Findings ordered by severity

### Moderate defect V01-F01: tone-response x coverage is insufficient

The local, non-overlapping five-point domains cannot support the full-width per-state curves visible in the reference using the documented interpolation approach. Revise `tone_response.csv` so every state is sampled on a common detuning grid spanning the intended panel limits, with enough points to show an offset resonance dip and phase excursion. This is a data-sufficiency defect and blocks acceptance of the readout/Rabi case.

### Moderate defect V01-F02: IQ sparse-background layer is absent

The data represent cluster centers/shapes only. Add clearly synthetic background/outlier rows, preferably distinguished by a `point_role` such as `cluster` versus `background`, or provide a separate background CSV. This is distinct from optional densification because the reference and T11 report identify the background as a separate visible layer.

### Low-severity documentation issue V01-F03: spin-expectation scaling is ambiguous

The reference bottom row visibly uses endpoint labels of approximately `-7/2` and `7/2`, while `spin_expectations.csv` spans approximately `-1..1` and the README calls that the displayed normalized range. A later script could intentionally scale the normalized values, but the required factor and axis semantics are undocumented. Clarify whether the CSV is normalized and specify the display transform, or store display-scale values. This does not remove a trace layer and is not independently blocking.

## Optional improvements, not defects

- Add `data_origin=synthetic_non_experimental` to the diagram, iterations, and readout/Rabi CSVs for consistent provenance when files are detached from their READMEs.
- Increase scatter/IQ sampling density or document a fixed-seed densification recipe for closer visual resemblance; density alone is not needed to exercise a represented layer.
- Keep guide locations, panel letters, inset/callout geometry, energy ladders, direct labels, and the SU(2) diagram in plotting configuration rather than duplicating them as scientific data.
- Use machine-readable Unicode or plain-text label metadata consistently when implementation begins; console rendering of some existing punctuation was not treated as evidence of file corruption.

## Untested areas and limitations

- No Python, package API, plotting script, interpolation, random-jitter routine, or image rendering was executed, as prohibited by T12 and `AGENT.md`.
- This review does not establish numerical, statistical, experimental, or physical validity and makes no comparison of exact source values.
- Pixel-level styling, font metrics, palette assignment, final annotation placement, accessibility, and rendered-image regression remain untested.
- CSV encoding was not independently byte-validated; visual shell output of some punctuation may reflect console decoding.

## Required next action

Revise the readout/Rabi tone table to provide full shared-axis curve coverage, add an explicit IQ background/outlier layer, and clarify spin-expectation scaling. Preserve the current synthetic-data disclaimers. After those changes, request a new independent verification report rather than modifying this V01 record.
