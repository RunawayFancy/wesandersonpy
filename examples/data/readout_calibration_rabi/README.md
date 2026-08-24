# Synthetic data for the readout-calibration/Rabi example

> **Synthetic-data notice:** Every value in this directory is artificial and non-experimental. The files were designed only to exercise plot layers seen in a visual reference. They do not reproduce, digitize, fit, validate, or make claims about the source measurements, and they are not intended to be physically meaningful.

The tables support a future Matplotlib example with four labeled regions: a pulse-sequence schematic, two stacked cavity-tone response axes, three adjacent IQ-scatter axes, and a four-row pulse-duration figure. All state names are generic basis-state labels retained because they are part of the visible plotting grammar.

## Files and schemas

### `sequence_primitives.csv`

One row per schematic element. Coordinates are normalized drawing coordinates invented for this example.

- `primitive_id`: unique element name.
- `group`: logical schematic group.
- `kind`: drawing primitive (`pulse_train`, `line`, `arrow`, `meander`, or `cross`).
- `x0`, `y0`, `x1`, `y1`: normalized extent or endpoints.
- `amplitude`: normalized pulse/meander amplitude; blank when irrelevant.
- `repeat_count`: repetition count; blank when irrelevant.
- `color_role`: semantic color key for a later palette mapping.
- `label`: optional visible label.

### `tone_response.csv`

Artificial samples for the two vertically stacked line axes.

- `state`: generic basis-state index.
- `detuning_mhz`: invented cavity-tone detuning on a common grid from -1.50 to 1.00 MHz.
- `magnitude_abs_s11`: arbitrary magnitude-like response.
- `phase_rad`: arbitrary phase-like response in radians.

Every state has 11 samples on exactly the same full detuning grid, so all nine curves can traverse the complete shared x-axis without extrapolation. Each curve contains a differently offset invented resonance dip and phase excursion. A later example may interpolate within this common domain only for visual smoothness; it must continue to label the result synthetic.

### `iq_scatter.csv`

Artificial IQ points for the three side-by-side scatter axes.

- `iq_panel`: left, middle, or right scatter panel.
- `state`: generic basis-state index.
- `point_id`: point identifier within a cluster.
- `i_mv`, `q_mv`: invented in-phase and quadrature coordinates in millivolts.
- `color_role`: semantic color key.
- `point_role`: `cluster` for state-associated points or `background` for the distinct sparse outlier layer. Background rows use `state=background` and `color_role=neutral`.

Plot `cluster` rows as the colored state clouds and plot `background` rows separately with smaller, low-alpha neutral marks. The right panel intentionally has more background points than the others to reproduce the visible sparse-field role. The intentionally small clouds can be plotted directly. If a denser visual is desired, a later example may add deterministic jitter to cluster rows using a documented fixed seed; background rows should remain a distinct layer.

### `rabi_populations.csv`

Artificial population-like traces for the upper three rows of the pulse-duration figure.

- `drive_case`: generic drive case (`case_a`, `case_b`, or `case_c`).
- `state`: basis-state index.
- `duration_ns`: invented pulse duration.
- `population`: artificial value between zero and one.
- `color_role`: semantic color key; state zero is black and the highlighted manifold uses a case color.
- `trace_role`: `dominant` or `minor` for styling.

The values are illustrative oscillations with small secondary traces. They are not normalized as a physical model and should not be interpreted as probabilities from an experiment.

### `spin_expectations.csv`

Artificial traces for the bottom pulse-duration row.

- `component`: generic `Jx`, `Jy`, or `Jz` series.
- `duration_ns`: invented pulse duration.
- `expectation_j_units`: artificial display-scale value in generic angular-momentum units.
- `color_role`: semantic color key.

Values are already stored on the illustrative display scale; do not multiply them at plot time. Use a y-axis range of `[-3.5, 3.5]` and endpoint tick labels `-7/2` and `7/2`. The column is generic visual-demo data, not a normalized expectation or a physical estimate.

## Reproducibility guidance

Keep the files immutable in the plotting example, use explicit palette-name-to-`color_role` mappings, and place a visible "synthetic demonstration data" note in the script docstring or figure caption.
