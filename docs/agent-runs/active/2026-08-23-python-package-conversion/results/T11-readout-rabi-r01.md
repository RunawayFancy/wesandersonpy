# T11 result: readout-calibration and Rabi example

## Scope and data status

Inspected only `plotting_example/Multiple_subplots_readout_calibration_rabi_data.png`. The observations below concern composition and visual grammar, not exact data. All companion CSV values are independently invented, synthetic, non-experimental, and not physically validated. No source values were digitized or transcribed.

## Overall composition

- Wide landscape figure, approximately 2:1 in aspect ratio, with four lettered regions.
- Region `(a)` occupies the narrow upper-left area; `(b)` occupies the upper middle; `(c)` spans the lower-left/middle; `(d)` is a tall right-hand block extending nearly the full height.
- The visual style is publication-like: serif text, thin black spines, inward-looking compact ticks, white background, and restrained muted colors.
- Dominant semantic colors are black/near-black plus coral red, deep teal, sage green, and warm orange/brown variants. Markers and lines share their series colors.
- No conventional boxed legend appears. Series identity is conveyed through direct state labels, curve color, and small energy-level schematics at the far right of region `(d)`.

## Region (a): control/readout sequence schematic

- A frameless schematic rather than a conventional Cartesian axis.
- The top line contains a short black control pulse train at left, the word `Control`, a separated compact readout burst labeled `RO`, and a short horizontal frequency arrow ending in an omega label.
- A path drops from the upper waveform area and changes color by stage: black first, coral/red across a short horizontal segment, orange through a vertically descending rounded meander, and teal at the terminal coupling symbol.
- The orange route forms repeated squared/rounded U-turns. It terminates above a teal cross-like resonator/coupler glyph near the bottom.
- There are no numeric ticks. Geometry, repetition, label placement, and color transitions carry the meaning.
- `sequence_primitives.csv` stores invented normalized geometry sufficient to redraw each visible role without implying circuit or pulse validity.

## Region (b): stacked cavity-tone response

- Two vertically stacked axes share the detuning x-axis and touch at a strong horizontal divider.
- The upper axis shows magnitude-like response, labeled with an absolute-value form of `S11`; its y-range visually sits around the mid-single digits. Multiple smooth curves have similar high baselines and offset resonance dips.
- The lower axis shows phase-like response, labeled as the angle of `S11` in radians. Visible reference ticks are negative fractional multiples of pi. Curves have broad phase excursions aligned approximately with the magnitude features.
- The shared x-axis is labeled cavity-tone detuning in MHz and spans negative to positive values. Only the lower axis displays x tick labels.
- Nine warm-hued curves progress from dark brown/black through rust to orange. Direct labels for states `|8>` through `|0>` sit in a row near the bottom of the magnitude axis and use the corresponding curve colors.
- Text labels `Tone 3`, `Tone 2`, and `Tone 1` divide the phase panel into three x-regions. Two vertical dotted guides descend through much of the lower axis at approximate tone boundaries/locations.
- Lines have no visible point markers. The synthetic table supplies five invented points per state; a future example can use a smooth interpolator while explicitly retaining the synthetic label.

## Region (c): readout IQ clouds

- Three adjacent rectangular scatter axes form a single strip. Internal boundaries are visible as vertical black spines.
- A shared x-label `Q (mV)` is centered below the strip; a shared vertical label `I (mV)` is placed at the left. Numeric tick labels are suppressed.
- The left and middle panels each contain four dense, partially overlapping colored clouds. The right panel contains two dominant clouds plus sparse background/outlier points.
- Direct ket-style state labels sit near their clusters instead of using a legend. The visible grouping is approximately states 0–3 in the left panel, 3–6 in the middle panel, and 6–7 in the right panel.
- Clouds are semi-transparent, made from very small points, and use orange, sage, coral, and teal. Their shapes are elliptical/irregular rather than perfect circles; overlap and sparse outliers add depth.
- The synthetic file uses six deliberately coarse points per cluster so all categories and placements are explicit. A future script may apply deterministic fixed-seed jitter to create denser clouds, but must not characterize the result as measurement noise.

## Region (d): pulse-duration populations and expectation values

- Four vertically stacked axes share pulse duration on the x-axis. The first three are equal-height population panels; the fourth is a slightly shorter expectation-value panel.
- Horizontal spines separate rows. Only the bottom axis has the `Pulse duration (ns)` x-label and visible numeric x tick labels; the left edge carries a shared `Populations` label across the upper rows.
- Each of the upper three rows contains smooth lines with small filled circular markers at regular duration samples. A dotted black horizontal reference line lies at population 1. A zero baseline/spine is visually important.
- Top population row: black and coral families exchange dominance in repeated oscillations. Direct annotations emphasize the black initial state and a coral target state; additional low-amplitude coral traces remain near zero.
- Middle population row: black and teal families exchange dominance, with several small teal intermediate traces. Direct labels emphasize states `|0>` and `|4>`.
- Lower population row: black and sage families vary more slowly, with a broad sage maximum near the middle and several overlapping intermediate-state traces. Direct labels emphasize states `|0>` and `|7>`.
- The far right of each population row contains a compact vertical energy ladder: short gray horizontal levels, a bold black lower level, and colored curved/vertical transition marks. These are annotations/inset graphics, not a fourth data series or legend.
- The bottom row shows three colored marker-plus-line expectation traces on a symmetric vertical scale. The y-label is a ket/bracket-style expectation symbol. Coral and teal traces oscillate with different phases; the sage trace makes one broad negative excursion and returns upward.
- A small `SU(2)` sphere/circle inset overlaps the lower-right of the bottom row. It includes axes/arrows, an equator-like ellipse, a curved trajectory, and angular labels. This is a conceptual annotation, not data derived from the CSVs.

## Recommended future Matplotlib construction

- Use a top-level `GridSpec` with a narrow left schematic column, a middle response/scatter block, and a wide right block. Use nested `GridSpecFromSubplotSpec` objects for the two response rows, three IQ columns, and four pulse-duration rows.
- Share x-axes within the response pair and within the four pulse-duration rows. Suppress redundant x tick labels with `tick_params(labelbottom=False)`.
- Draw direct labels with `Axes.text`; reserve `inset_axes` or manually positioned child axes for the three energy ladders and SU(2) annotation.
- Use low-alpha, very small scatter markers for IQ clouds; use thin lines plus small circular markers for time traces; use dotted horizontal reference lines at one.
- Preserve whitespace around panel letters and avoid a global legend. Map semantic color roles through the package palette API so the example demonstrates categorical palette access.

## Artifacts created

- `examples/data/readout_calibration_rabi/README.md`
- `examples/data/readout_calibration_rabi/sequence_primitives.csv`
- `examples/data/readout_calibration_rabi/tone_response.csv`
- `examples/data/readout_calibration_rabi/iq_scatter.csv`
- `examples/data/readout_calibration_rabi/rabi_populations.csv`
- `examples/data/readout_calibration_rabi/spin_expectations.csv`

No Python was run and no files outside the authorized output paths were edited.
