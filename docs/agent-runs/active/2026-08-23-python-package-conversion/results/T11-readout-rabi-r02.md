# T11 result revision r02: readout-calibration and Rabi example

## Status and scope

This revision addresses V01-F01, V01-F02, and V01-F03 from `verification/V01-synthetic-data.md`. It changes only the assigned `examples/data/readout_calibration_rabi/` artifacts and adds this result record. The earlier T11 r01 report and the V01 verification record remain unchanged.

All values remain independently invented, synthetic, non-experimental, not digitized, and unsuitable for scientific or physical inference. No Python was run.

## Revised visual findings

The reference is a wide, publication-style composite with four lettered regions and a restrained palette of near-black, coral, teal, sage, and warm orange/brown.

### Region (a): pulse-sequence schematic

- Frameless drawing in the upper-left area.
- A short black control-pulse train, a separated readout burst, and a small frequency arrow sit across the top.
- A routed path changes from black to coral to an orange descending meander and ends at a teal cross-like coupling symbol.
- This is drawing geometry, not measurement data; `sequence_primitives.csv` remains unchanged and records synthetic normalized primitives.

### Region (b): tone response

- Two touching axes share a full detuning x-axis: magnitude-like `|S11|` above and phase-like `angle(S11)` below.
- Nine warm-hued response curves cross essentially the full axis. Each has a high baseline and a state-dependent resonance dip; the phase curve has a corresponding broad excursion.
- Direct labels identify states `|8>` through `|0>`. Three tone-region labels and dotted vertical guides appear in the lower axis.
- Revised `tone_response.csv` now makes the visual requirement explicit in data: all nine states share the same 11 detuning values from -1.50 through 1.00 MHz. Each series therefore renders from the left panel limit to the right panel limit without extrapolation.

### Region (c): IQ scatter strip

- Three adjacent axes share outer I/Q labels and omit numeric tick labels.
- Colored semi-transparent clouds represent overlapping state groups; direct state labels replace a conventional legend.
- A visibly separate sparse field of tiny outlier/background points exists around the clouds, particularly in the right panel.
- Revised `iq_scatter.csv` adds `point_role`. Existing colored samples are `cluster`; new neutral samples are `background` and use `state=background`. The right panel receives ten background rows, while left and middle receive four each, preserving the qualitative density difference.

### Region (d): pulse-duration populations and spin display

- Three stacked population rows use smooth colored lines plus filled circular markers, dotted unity guides, direct state annotations, and small energy-ladder drawings at right.
- Black exchanges dominance with coral, teal, then sage in successively different drive cases. Minor same-family traces remain near the baseline.
- A fourth shared-x row shows three expectation-like colored traces and an SU(2) conceptual inset.
- The expectation axis visibly uses illustrative endpoints near `-7/2` and `7/2`. Revised `spin_expectations.csv` is self-contained on that display scale: the value column is now `expectation_j_units`, values lie within -3.5 to 3.5, and no plot-time scale transform is required.

## Exact data-contract changes

### `tone_response.csv`

- Replaced 45 locally sampled rows with 99 rows: 9 states x 11 common detuning positions.
- Common detuning grid: `-1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00` MHz.
- Retained columns `state`, `detuning_mhz`, `magnitude_abs_s11`, and `phase_rad`.
- Invented full-baseline values around each offset magnitude dip and associated phase excursion.

### `iq_scatter.csv`

- Added the `point_role` column.
- Tagged all 60 pre-existing state-associated rows as `cluster`.
- Added 18 distinct sparse background rows: 4 left, 4 middle, and 10 right.
- Background rows use `state=background`, `color_role=neutral`, and `point_role=background` so plotting code can style/filter the layer independently.

### `spin_expectations.csv`

- Renamed `expectation` to `expectation_j_units`.
- Replaced normalized-looking values with self-contained synthetic display values on the illustrative ±3.5 range.
- The intended axis is explicitly `[-3.5, 3.5]`, with endpoint labels `-7/2` and `7/2`; no plot-time multiplication is permitted or required.

### `README.md`

- Documents the full common tone grid and interpolation only within that domain.
- Defines `point_role` and separate styling/usage of the background layer.
- Defines the expectation display units, y-limits, fractional endpoint labels, and absence of a plot-time transform.
- Retains the prominent synthetic/non-experimental disclaimer and clarifies detached plotting usage.

## Recommended later plotting behavior

- Group tone data by state, sort on `detuning_mhz`, and render all groups on identical x-limits. Any smoothing should remain inside the stored domain.
- Split IQ data by `point_role`: colored low-alpha cluster marks versus smaller neutral low-alpha background marks. Optional fixed-seed densification applies only to clusters.
- Plot `expectation_j_units` directly, set y-limits to ±3.5, and format the endpoint ticks as `-7/2` and `7/2`.
- Keep panel letters, direct labels, tone guides, energy ladders, and the SU(2) sphere as presentation configuration rather than scientific data.

## Revised artifact inventory

- Updated `examples/data/readout_calibration_rabi/README.md`
- Unchanged `sequence_primitives.csv`
- Updated `tone_response.csv`
- Updated `iq_scatter.csv`
- Unchanged `rabi_populations.csv`
- Updated `spin_expectations.csv`
- Added `docs/agent-runs/active/2026-08-23-python-package-conversion/results/T11-readout-rabi-r02.md`

The three V01 findings assigned to T11 are resolved at the fixture and documentation level, pending independent re-verification and later human visual approval.
