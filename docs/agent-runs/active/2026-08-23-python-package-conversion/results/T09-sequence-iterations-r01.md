# T09 result: sequence/time-domain and faded iterations

## Scope and integrity

Only the two assigned PNGs were visually inspected. The descriptions below record qualitative construction and layout; no plotted values were digitized or transcribed. All CSV values produced by T09 are independently invented, synthetic, non-experimental demonstration data without physical validity.

## Reference 1: diagram, time-domain response, and multi-parameter populations

Reference: `plotting_example/Diagram_sequence_timedomain_dataplot_with_multi_params.png`

### Overall geometry

- Tall portrait composition divided into four labeled panels `(a)`–`(d)`.
- `(a)` is a borderless schematic spanning the figure width.
- `(b)` is a short, wide Cartesian axes below the schematic.
- `(c)` and `(d)` are taller stacked Cartesian axes with equal widths and a shared horizontal control variable. Their frames nearly touch; the upper panel suppresses x tick labels and the lower panel supplies the shared x label.
- Panel letters sit outside the left edge. The plotted axes begin farther right, leaving room for vertical labels and panel tags.

### Panel (a): sequence schematic

- Two horizontal channel baselines, labeled at left in contrasting colors: a dark blue-gray upper `Transmon` channel and a red lower `Resonator` channel.
- Upper channel layers: a narrow outlined pulse labeled `State prep.` and a later narrow gray-filled pulse labeled `Spectroscopy pulse`.
- Lower channel layers: a broad muted-red rectangular fill labeled `Stimulation pulse`, followed after a long idle span by a shorter low red block labeled `Measurement`.
- Channel baselines and pulse outlines carry the channel color. Text is placed adjacent to the relevant pulse rather than in a legend.
- There are no visible ticks or numerical axes; horizontal placement communicates ordering and relative duration only.

### Panel (b): time-domain data and comparison curve

- Boxed axes with horizontal `Time t (microseconds)` and vertical `Photons`-like response label; the y notation indicates normalization to a maximum response.
- Red circular `Data` markers lie over a wide, pale rose `Fit` curve. The marker series rises smoothly from near zero, peaks early, and decays asymptotically toward zero over a much longer interval.
- Two pale vertical guides mark the origin and approximate peak-time region.
- The legend sits inside the upper-right area, vertically listing a marker key above a line key.
- Sparse tick labeling and no grid beyond the two guides keep attention on the response shape.

### Panel (c): first prepared-state population sweep

- Five marker-only population series share one control axis and use dark red, dark blue, light blue, blue-gray, and mustard state colors.
- A single-row state legend sits above the axes rather than inside the data area.
- The dominant dark-red series begins high, falls to a mid-level shelf, shows a step near the vertical dotted transition guide, and then slowly increases.
- Four other series remain close to zero and are expanded in a lower-left inset. The inset is boxed, has a very small y range, and is connected to a highlighted region of the main axes by black callout geometry.
- A red `Prepare |1>` annotation appears in the upper-right together with a small energy-level sketch. The sketch uses horizontal levels, curved arrow(s), and colored state labels.
- Y ticks span a population-like range from zero to one. The shared x tick labels are suppressed.

### Panel (d): second prepared-state population sweep

- The five state colors and marker-only encoding are reused for direct comparison with panel `(c)`.
- A light-blue series begins as the largest visible population and declines; a mustard series rises from near zero and becomes the largest at high control values. The red series rises near the dotted transition and then gently declines. Darker blue series remain low.
- The same vertical dotted guide aligns with panel `(c)`.
- A light-blue `Prepare |7>` annotation and miniature level diagram occupy the upper-right region; no duplicate full legend is present because panel `(c)` establishes the mapping.
- The bottom axes carries the shared control-parameter label.

### Likely data fields and generated fixtures

- Sequence event fields: channel, event name, schematic start/end, amplitude, render role, label.
- Time-response fields: time, point value, smooth comparison value.
- Population fields: preparation, state, control parameter, population.
- Generated files: `examples/data/diagram_sequence/sequence_events.csv`, `time_domain_response.csv`, and `population_sweeps.csv`, documented in the directory README.

## Reference 2: multiple iterations with fading

Reference: `plotting_example/Multiple_iteration_data_with_faded_effect.png`

### Geometry and axes

- One short, wide boxed axes labeled `(a)` outside its upper-left corner.
- Vertical axis is `Populations`; horizontal axis is the same barred control parameter used by the population panels above.
- The visible y range is approximately population bounds, with a small margin below zero. The x domain extends from near zero to a few thousand in the reference, but generated values are independent inventions.

### Plot layers and visual roles

- Three circular-marker series are identified by an in-axes horizontal legend near the upper right: dark navy `P0`, brick red `P1`, and light blue `P7`.
- Multiple iterations of each series are drawn at shared x coordinates. Lower-opacity repetitions create vertical/translucent clouds, while a more saturated iteration remains easy to track.
- No connecting lines are apparent; repetition, alpha, and color encode the iteration structure.
- A tan vertical dashed guide near the middle-left divides two qualitative regimes.
- Before the guide, the red series starts high and settles, the navy series rises and plateaus, and the light-blue series stays near zero. Around the guide, all three shift. Afterward, red is roughly mid-level with a mild rise, navy gradually declines, and light blue remains low with a slight rise.
- There is no colorbar; state identity is categorical and iteration age is conveyed implicitly by opacity rather than a second legend.

### Likely data fields and generated fixture

- Fields: iteration identifier, fade/chronology rank, state series, shared control parameter, population.
- Generated file: `examples/data/multiple_iterations/iteration_populations.csv`, documented in the directory README.
- Four explicit synthetic iterations cover all visible layers: three categorical state colors, repeated translucent marker clouds, a newest opaque trace, and a regime guide documented at an illustrative control value of 900.

## Handoff notes

- Later plotting code should treat guide positions, inset limits, alpha values, colors, annotation placement, and level sketches as presentation configuration rather than scientific metadata.
- The miniature level diagrams and callout connectors are annotation artists, not data series.
- The reference notation should be checked by the human before exact labels are finalized; this report intentionally avoids claiming that visually inferred symbols encode a validated physical quantity.
