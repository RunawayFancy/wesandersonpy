# V02: Readout-calibration/Rabi reverification

## Verification identity and verdict

- Task: T13, independent reverification against `context/conversation-v002.md`, T11 r02, and V01.
- Inspection date: 2026-08-23.
- Status: **PASS.**
- Overall readiness: **the complete five-case synthetic-data set is ready for human qualitative review before plotting-script implementation.** This conclusion combines the four unchanged case passes recorded in V01 with the readout-calibration/Rabi pass established here.

## Scope and methods

I inspected the readout-calibration/Rabi reference PNG at original resolution and reviewed the revised directory README plus all five CSVs under `examples/data/readout_calibration_rabi/`. I used read-only PowerShell CSV parsing and grouping to verify headers, row counts, full-row and primary-key uniqueness, missing cells, categorical coverage, numeric domains, and the exact contracts relevant to V01-F01 through V01-F03. I did not run Python, render plotting code, digitize reference values, modify V01, or assess scientific validity.

Sources inspected:

- `plotting_example/Multiple_subplots_readout_calibration_rabi_data.png`
- `examples/data/readout_calibration_rabi/README.md`
- `examples/data/readout_calibration_rabi/sequence_primitives.csv`
- `examples/data/readout_calibration_rabi/tone_response.csv`
- `examples/data/readout_calibration_rabi/iq_scatter.csv`
- `examples/data/readout_calibration_rabi/rabi_populations.csv`
- `examples/data/readout_calibration_rabi/spin_expectations.csv`
- `tasks/T11-readout-and-rabi.md`
- `results/T11-readout-rabi-r02.md`
- `verification/V01-synthetic-data.md`

## V01 finding disposition

### V01-F01: tone-response x coverage is insufficient — RESOLVED

`tone_response.csv` now contains 99 rows: nine state series with 11 rows each. Every state has the identical detuning grid `-1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00`, with no duplicate `(state, detuning_mhz)` keys. All nine curves therefore span the common `-1.50..1.00 MHz` display domain without extrapolation. Each state also contains an offset magnitude dip and associated phase excursion, qualitatively supporting the full-width layered response curves visible in reference region `(b)`.

### V01-F02: IQ sparse-background layer is absent — RESOLVED

`iq_scatter.csv` now contains 78 rows and a `point_role` column. The original 60 state-associated rows are marked `cluster`; 18 independently selectable rows are marked `background`, with `state=background` and `color_role=neutral`. Background counts are four in the left panel, four in the middle panel, and ten in the right panel. This supplies the distinct sparse field visible around the colored clouds and preserves the stronger right-panel background presence. No duplicate `(iq_panel, state, point_role, point_id)` keys were found.

### V01-F03: spin-expectation scaling is ambiguous — RESOLVED

`spin_expectations.csv` now uses the explicit column `expectation_j_units`. Its 27 rows comprise `Jx`, `Jy`, and `Jz` on the same nine-duration `0..800 ns` grid. All values lie within `[-3.5, 3.5]`; the actual combined range is `-3.47..3.50`. The README directs plotting these values without multiplication, sets the y-range to `[-3.5, 3.5]`, and specifies endpoint tick labels `-7/2` and `7/2`. The stored scale and display contract are consistent and unambiguous.

## Revised CSV and regression observations

| File | Rows | Verification result |
|---|---:|---|
| `sequence_primitives.csv` | 9 | Unchanged drawing roles remain present. Its 18 blank cells are confined to optional primitive attributes and labels. |
| `tone_response.csv` | 99 | Nine states x eleven identical full-domain coordinates; no blanks, duplicate full rows, or duplicate state/x keys. |
| `iq_scatter.csv` | 78 | Ten cluster panel/state groups plus separately filterable background rows in all three panels; no blanks or duplicate keys. |
| `rabi_populations.csv` | 144 | Unchanged three-case structure remains intact: 27, 45, and 72 rows for cases a, b, and c; dominant/minor roles and bounded `0..1` values remain present. |
| `spin_expectations.csv` | 27 | Three components x nine shared durations; direct display-scale values stay within the documented bounds. |

All five revised-directory CSVs parsed as rectangular tables. No duplicate complete rows were found. The changed tone, IQ, and spin schemas are documented accurately in the README, and the unchanged sequence and population tables still cover their previously accepted visual layers.

## Reference-image and layer comparison

The revised data remain aligned with the qualitative construction of the reference:

- Region `(a)` retains the frameless control/readout sequence and routed multicolor schematic primitives.
- Region `(b)` can now draw all nine magnitude and phase response series across the full common x-axis while retaining state-dependent offsets.
- Region `(c)` can separately draw colored state clouds and a sparse background field, with more background points in the right panel.
- Region `(d)` retains three population rows with dominant and minor traces and now supplies the bottom expectation traces directly on the visibly intended fractional-endpoint scale.

Panel letters, direct labels, tone guides, energy ladders, reference lines, and the SU(2) inset remain presentation configuration, which is appropriate because they are annotations rather than measurement-like data layers. Exact marker density and smoothing remain later styling choices, not missing schema elements.

## Synthetic provenance and claims

The directory README prominently states that every value is artificial, non-experimental, not digitized, not fitted or validated, and not physically meaningful. It also requires later plotting output to retain a visible synthetic-demonstration notice. No revised CSV or documentation artifact claims experimental validity. State, response, population, and expectation terminology is explicitly presented as generic plotting grammar rather than a physical result.

## Findings ordered by severity

No blocking, moderate, or low-severity defects were found in the T13 acceptance scope.

Optional future consistency improvement: add a row-level `data_origin=synthetic_non_experimental` field to these CSVs so detached files carry the same provenance guard already used by the fidelity and scatter fixtures. The prominent directory-level notice is sufficient for this verification and the omission does not block human review.

## Untested areas and limitations

- No Python, interpolation, densification, plotting script, package API, or rendered-image regression was run.
- Pixel-level layout, font metrics, palette selection, marker density, smoothing quality, and annotation placement remain for later plotting implementation and human visual review.
- This static verification establishes fixture structure and qualitative layer coverage only. It provides no numerical, statistical, experimental, or physical validation.

## Final decision

T11 r02 resolves V01-F01, V01-F02, and V01-F03. The readout-calibration/Rabi case now passes its data-sufficiency and documentation criteria. Together with V01's four prior passes, all five synthetic-data cases are ready for the human to review their proposed characteristics before authorizing plotting-script or package implementation.
