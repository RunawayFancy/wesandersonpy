# T21 result: diagram and faded-iteration baseline visual review

## Task and status

- Task: T21, render and qualitatively compare the diagram/time-domain and faded-iteration examples with their corresponding authorized references.
- Context: `context/conversation-v007.md`.
- Status: baseline render and original-detail comparison complete; no plotting code or fixture was changed.

The generated images contain only the bundled synthetic fixtures. Reference images were inspected only for layout, hierarchy, plot grammar, and color-role comparison. No values were digitized, extracted, or treated as measurements.

## Render evidence

The Conda PowerShell hook was loaded and `wespy` was activated. Both scripts completed with exit code 0:

```powershell
python examples/diagram_sequence_time_domain.py `
  --data-dir examples/data/diagram_sequence `
  --output examples/figures/generated/baseline/diagram_sequence_time_domain.png

python examples/multiple_iterations_faded.py `
  --input examples/data/multiple_iterations/iteration_populations.csv `
  --output examples/figures/generated/baseline/multiple_iterations_faded.png
```

Generated artifacts:

- `examples/figures/generated/baseline/diagram_sequence_time_domain.png`, 1296 x 1836 pixels, 152,223 bytes.
- `examples/figures/generated/baseline/multiple_iterations_faded.png`, 1512 x 594 pixels, 60,558 bytes.

Each generated PNG and its correspondingly named file under `plotting_example/` was inspected with original-detail image viewing.

## Diagram, time response, and population sweeps

### Preserved key features

- The four-part vertical narrative is recognizable: a borderless two-channel sequence, a compact response plot, and two aligned population panels.
- Panel letters are consistently placed outside the left edge and give the intended publication-style hierarchy.
- The response panel preserves the core grammar of circular points over a broad pale guide curve, two vertical timing guides, a boxed frame, and an internal legend.
- The population panels preserve marker-only categorical series, a shared transition guide, a legend above the upper population panel, a low-value inset with callout connectors, and preparation/level annotations on the right.
- The `Zissou1` red, cyan, and mustard family gives the figure a coherent film-palette identity, and the visible synthetic-data caption is clear.

### Layout and readability shortcomings

1. The schematic labels collide. `State prep.`, `Spectroscopy pulse`, and `Stimulation pulse` occupy nearly the same horizontal/vertical zone; portions visually merge. The reference separates these labels by using pulse-adjacent placement rather than centering every label above its rectangle. This is the clearest figure-level defect.
2. The generated composition is substantially more open vertically than the reference. The lower preparation panel uses a zero-to-one range although all visible synthetic points occupy only the lower part, leaving a large empty middle. Its energy-level annotation consequently floats far above the data and feels detached.
3. The upper population inset is too large relative to its host panel. Its numeric tick labels are crowded, and the long cyan callout connectors cross much of the panel and become stronger visual elements than the low-population data they are meant to explain. The reference uses a smaller inset, a compact highlighted source region, and short neutral connectors.
4. The top-level legend displays `P1`, `P2`, `P7`, `P8`, and `P9plus` as italic strings rather than polished state notation. The visual reference uses compact ket/state labels, which are easier to scan and align with the preparation annotations.
5. The generated response panel is taller and its broad guide is heavy enough to read as a band; the reference's guide is visually closer to a line. The current layer order remains legible, but the guide competes more with the points than necessary.

### Color and hierarchy shortcomings

1. Five categorical population roles are compressed into a palette whose closest pairs are hard to distinguish at small marker size. `P2` and `P7` are two nearby blue/cyan tones, while `P8` and `P9plus` are nearby gold/yellow tones. The marker shape is identical for every series, so color is the only differentiator in the data area.
2. Schematic event text uses the golden `Zissou1` color even when associated with blue or red channels. Against white it has weaker contrast than the channel strokes, and it obscures the semantic connection between event and channel.
3. The yellow transition/timing guides attract more attention than their structural role warrants, particularly in the population panels.

### Recommended package-palette-based revision

- Preserve the `Zissou1` visual theme but construct roles intentionally: red `Zissou1[-1]` for `P1`, near-black `Moonrise1[-1]` for `P2`, light blue `Zissou1[1]` for `P7`, blue-gray `Royal1[0]` for `P8`, and mustard `Zissou1[2]` for `P9plus`. These remain package-derived and match the documented semantic roles more closely.
- Add redundant marker shapes or filled/open variants for the closest state categories so interpretation does not depend on color alone.
- Use `Moonrise1[-1]` for high-contrast schematic annotation text and a muted neutral such as `Moonrise2[2]` for timing/transition guides.
- Place schematic labels individually: keep state preparation above its narrow pulse, move spectroscopy text to the right of its pulse, and place stimulation text to the right of or inside its broad block.
- Reduce the height of the response panel and especially the lower population panel. Give the lower panel a tighter illustrative y-range with a small margin, while retaining the synthetic values unchanged.
- Shrink and simplify the inset, reduce its tick count, highlight a compact source rectangle, and use short neutral connectors.
- Replace machine identifiers with an explicit display-label map such as `$|1\rangle$`, `$|2\rangle$`, and `$|9+\rangle$` without changing CSV values.

## Multiple iterations with fading

### Preserved key features

- The short, wide single-panel geometry closely matches the reference's overall silhouette.
- All four iterations remain visible as vertical translucent stacks at shared control coordinates; opacity increases monotonically so the newest trace is visually dominant.
- Circular markers are used without connecting lines, preserving the reference's repeated-scatter grammar.
- The three-item horizontal legend, boxed frame, population axis, transition guide, and external panel letter are all present.
- The synthetic-data footer is visible without overlapping the axes.

### Color, fading, and readability shortcomings

1. The current semantic mapping does not match the fixture contract or the reference hierarchy. `P0` and `P1` are both cyan-family colors and are difficult to distinguish, while `P7` is gold. The intended roles are dark navy/ink for `P0`, brick red for `P1`, and light blue for `P7`.
2. The saturated red dashed transition guide is the strongest chromatic element in the panel even though it is contextual rather than a primary series. The reference uses a restrained tan/neutral guide.
3. Fading itself works, but the faintest cyan layers approach invisibility on white and the two cyan series visually mix. Slightly compressing the alpha range would preserve chronology while keeping the oldest layer readable.
4. Markers are relatively large and widely spaced, which makes the repeated layers read as isolated vertical stacks rather than soft repeated traces. The fixture should remain unchanged, but smaller markers would make the visual cloud lighter and less blocky.
5. Legend labels render as italic `P0`, `P1`, and `P7` rather than subscripted `$P_0$`, `$P_1$`, and `$P_7$`. The external panel letter is also much larger and farther from the frame than in the reference.

### Recommended package-palette-based revision

- Use a role-focused combination derived from the package: dark navy `BottleRocket2[2]` for `P0`, brick red `Royal1[1]` for `P1`, and light blue `Zissou1[1]` for `P7`. This provides the requested dark/warm/light hierarchy while retaining a restrained Wes Anderson palette character.
- Use muted beige `Moonrise2[2]` for the regime guide, with a slightly thinner dashed stroke.
- Use a narrower alpha progression, for example approximately 0.25 through 0.90, keep the newest iteration above older layers with explicit z-order, and slightly reduce marker size.
- Add an explicit display-label map with proper subscripts and reduce/reposition the panel letter closer to the upper-left frame.
- Retain the wide aspect and current legend location; those choices already match the reference well.

## Findings ordered by priority

### Moderate T21-F01: diagram schematic labels overlap

Three event labels collide in the upper schematic, weakening the sequence ordering and making the most explanatory region difficult to read. Individual pulse-aware label placement is required.

### Moderate T21-F02: categorical colors do not provide sufficient separation

The diagram has two close blue categories and two close yellow categories with identical marker shapes. The faded plot is more severe: its two primary series are both cyan while the expected red category is absent. Package-derived role mappings and redundant markers should be revised before exhibit approval.

### Moderate T21-F03: diagram inset and vertical allocation obscure hierarchy

The oversized inset, long colored connectors, and large empty region in the lower population panel make annotations dominate the synthetic data. Tighter panel allocation and compact neutral callout geometry would better preserve the reference hierarchy.

### Low T21-F04: typography and contextual guides need refinement

Machine-like legend labels, oversized panel tags, and saturated guide colors make both figures feel less publication-ready. Explicit mathematical display labels and muted package-derived guide colors would improve polish without changing data.

## Limitations and next action

- This is a qualitative visual comparison, not a scientific validation or quantitative similarity score.
- No color-vision-deficiency simulation, print proof, or alternate-background test was performed.
- Reference values were not read or inferred; recommendations concern only presentation.
- No baseline image should be promoted to `examples/figures/` in its current form.

The host should reconcile these findings with the other baseline reviews, assign scoped script-only fixes, then request a second render and independent visual review before asking the human maintainer to approve any exhibit.
