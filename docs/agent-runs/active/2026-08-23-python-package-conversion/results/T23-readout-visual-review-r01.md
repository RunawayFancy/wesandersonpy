# T23 result: readout and Rabi baseline visual review

## Task and status

- Task: T23, render and qualitatively compare the unchanged readout-calibration/Rabi example with its authorized visual reference.
- Context: `context/conversation-v007.md`.
- Status: **baseline render passed; visual diagnosis complete; no code or fixture fix applied.**
- Review boundary: the reference was used only for qualitative layout, hierarchy, encoding, density, and color-role comparison. No reference values were digitized, extracted, or treated as experimental input.

## Sources inspected

- `examples/readout_calibration_rabi_subplots.py`
- `examples/data/readout_calibration_rabi/README.md`
- The five bundled synthetic CSVs consumed by the script
- Generated baseline: `examples/figures/generated/baseline/readout_calibration_rabi_subplots.png`
- Authorized reference: `plotting_example/Multiple_subplots_readout_calibration_rabi_data.png`

Both images were inspected at original detail. The generated image is 1980 x 1656 pixels at approximately 180 DPI; the reference is 1024 x 499 pixels. These dimensions are reported only to identify the reviewed artifacts, not to infer source measurements.

## Render evidence

The Conda PowerShell hook was loaded and `wespy` was activated. `CONDA_PREFIX` resolved to `E:\conda\envs\wespy`.

Exact command:

```powershell
python examples/readout_calibration_rabi_subplots.py --data-dir examples/data/readout_calibration_rabi --output examples/figures/generated/baseline/readout_calibration_rabi_subplots.png
```

Exit code: 0.

Console result:

```text
Saved synthetic demonstration figure to examples\figures\generated\baseline\readout_calibration_rabi_subplots.png
```

The visible synthetic-data footer is present. The image was left in the ignored baseline directory and was not promoted to a committed gallery path.

## Overall comparison

The baseline preserves the reference's four-part grammar: `(a)` a control/readout schematic, `(b)` paired tone-response axes, `(c)` three IQ panels, and `(d)` three population rows plus a spin-expectation row. It also preserves the essential mark families: pulse primitives, multiple warm tone curves, directly labeled IQ clusters, strong and faint population traces, dotted reference lines, energy ladders, and a conceptual spin inset.

The largest divergence is hierarchy. The reference is a compact landscape composition: schematic/tone/IQ material occupies the left portion while the four duration rows form a parallel block on the right. The baseline turns those relationships into three full-width vertical bands and gives the duration block most of a much taller canvas. This makes the figure readable as separate sections, but it no longer communicates the reference's side-by-side calibration-versus-dynamics relationship and requires much more visual travel.

The current palette is cohesive at a broad level: near-black ink, coral red, teal, light cyan, and mustard form a recognizable Wes Anderson-inspired family, while the warm tone curves sit in a related red/brown/orange range. The remaining issue is semantic precision. The role named `sage` is actually a light blue from `Zissou1`, so it is close to teal rather than the distinct green role visible in the reference. Some state colors also change by panel without an explicit indication that colors are panel-local roles rather than global state identities.

## Panel-by-panel findings

### `(a)` control/readout schematic

Preserved features:

- Separate control and readout motifs, an arrowed route, repeated pulse elements, a warm meander, a coral horizontal element, and a teal cross-like endpoint are all recognizable.
- The near-black/coral/mustard/teal assignment follows the reference's broad semantic ordering and is attractive on white.
- Color is not the only encoding: geometry and labels distinguish each primitive.

Shortcomings:

- The baseline uses a wide, sparse schematic with substantial unused white space; the reference is a compact vertical chain that reads as one continuous sequence.
- The `RO` label, nearby small label text, and repeated pulse glyphs crowd one another at the upper right of the schematic.
- The control train is visually detached from the lower primitives, while the reference connects the elements more clearly through a single routing path.
- The mustard meander descends diagonally across a large region; the reference's meander is a tighter vertical structural element.

Recommended revision:

- Recompose the primitives into a compact vertical schematic with one clear connector path and a dedicated label zone. Retain the current package-derived ink, coral, mustard, and teal roles, but reduce blank area and prevent `RO` text from touching the pulse glyphs.

### `(b)` paired tone-response axes

Preserved features:

- Nine warm state curves appear in both magnitude and phase axes.
- The two axes share a horizontal domain, have distinct magnitude/phase labels, include tone guides, and preserve direct state annotation.
- `GrandBudapest1` supplies a coherent warm family close to the reference's brown-to-orange treatment.

Shortcomings:

- Eleven stored samples per state render as angular polylines. The reference curves are visually smooth and much denser, so the baseline reads more like a schematic polygon than a calibrated-response grammar.
- Adjacent `GrandBudapest1` samples repeatedly pass through similar coral/brown hues. State order is difficult to perceive from color alone.
- State labels are attached at individual minima, producing a staggered row that competes with the curves. The reference uses a compact ordered state key between the axes.
- The baseline tone labels read left-to-right as Tone I, II, III, while the reference's displayed ordering runs in the opposite numbered direction. Even without copying positions or values, the semantic ordering should be consciously chosen and documented.
- The magnitude axis is disproportionately wide relative to the schematic, and its panel letter dominates the top-row alignment.

Recommended revision:

- Use a documented interpolation of the synthetic common-domain samples to draw smooth guide curves while retaining the original points or otherwise making the synthetic source explicit.
- Move state labels into one ordered, colored key between the axes instead of placing each label at a curve minimum.
- For ordinal color communication, consider `wes.get_colormap("Zissou1", kind="continuous")` sampled consistently from cool to warm, with direct labels retained as redundant encoding. If `GrandBudapest1` is kept for closer warm-family resemblance, add an ordered key and stronger lightness separation rather than relying on hue alone.
- Decide whether tone numbering should match the reference's descending visual order or use ascending order, then make that decision explicit rather than incidental.

### `(c)` IQ triptych

Preserved features:

- Three bordered IQ panels, direct basis-state labels, distinct colored clusters, and a separate sparse neutral background layer are present.
- Marker color plus direct text labels provides useful redundant categorization.
- Cluster placement and the stronger background presence in the right panel reproduce the requested qualitative layer structure without claiming source values.

Shortcomings:

- Each cluster contains only a handful of large points, whereas the reference uses dense clouds. The result looks like a small categorical scatter example rather than a readout-cloud grammar.
- The three axes are separated by wide gutters and each repeats an x-axis label. The reference tiles the panels tightly and uses a shared label, creating a more coherent triptych.
- The generated axis-role labels are reversed relative to the visible reference orientation: the baseline places `I` horizontally and `Q` vertically, while the reference displays the opposite assignment. This should be resolved as a deliberate schema/presentation choice.
- Light-cyan text and points have weak contrast on white, particularly where labels overlap their own clusters.
- State colors are panel-local: state 3 changes from teal to coral, and state 6 changes from mustard to light cyan. That reproduces aspects of the reference, but the figure offers no legend or note explaining that hue represents the current panel's highlighted role rather than a global state identity.

Recommended revision:

- Use the fixture README's allowed deterministic, fixed-seed jitter to create denser synthetic clouds while keeping background points separate and visibly labeling the output synthetic.
- Tile the axes with shared borders or minimal gutters and use one shared horizontal label plus one shared vertical label.
- Confirm and document the intended I/Q axis orientation.
- Either make state colors globally consistent or explicitly treat them as panel-local roles. For a stronger global system, reserve coral for the `|2>` target, teal for `|4>`, and a distinct green for `|7>` across IQ, population, and ladder annotations.

### `(d)` population rows

Preserved features:

- Three stacked population rows show a near-black baseline state, one strongly colored target manifold, faint secondary traces, dotted upper guides, and right-side energy-ladder sketches.
- Line weight, opacity, and marker size reinforce dominant versus minor traces, so interpretation does not rely on color alone.
- The target-case sequence of coral, teal, and a lighter cool color broadly follows the reference's case progression.

Shortcomings:

- The rows span almost the entire figure width and dominate the page, unlike the compact right-hand block in the reference.
- The nine-point traces form visibly triangular segments. The reference's dense markers and smooth oscillatory lines create a much stronger temporal rhythm.
- Minor traces are so pale that several nearly disappear, especially in the second and third rows.
- Every row repeats the short `$P$` y label; the reference uses one stronger group label, which gives the block better hierarchy.
- The energy ladders overlap the data region and are compressed to the same four-level geometry for all three cases. In the reference they occupy a dedicated right margin and visibly scale in complexity with the case.
- The `(d)` panel label is effectively lost at the far-left/top boundary of the full-width duration block, while the reference identifies the block clearly.

Recommended revision:

- Restore a compact right-column duration block, give its energy ladders a reserved annotation column outside the trace area, and place one visible `(d)` label plus one group y label.
- Draw smooth synthetic guides through the stored points while retaining markers, or add a documented deterministic sample-density step. Increase minor-trace alpha enough to remain legible while keeping dominant traces heavier.
- Make ladder complexity and target labels reflect the displayed case hierarchy without deriving any values from the reference.

### Spin-expectation row and conceptual inset

Preserved features:

- Three colored components, endpoint-style fractional tick labels, a legend, and a circular arrow inset preserve the reference's spin-vector grammar.
- Components are redundantly identified by the legend and distinct trajectories.

Shortcomings:

- The light-cyan and teal components are close in hue, and the light-cyan trajectory has weak contrast.
- The inset overlaps the data field. It lacks the reference's clear `SU(2)`/axis/angle annotation hierarchy and reads as a decorative circle rather than an explanatory coordinate sketch.
- The bottom row is visually separated from the population rows by the overall tall layout rather than integrated as the fourth row of one compact block.

Recommended revision:

- Place the conceptual inset in the same reserved annotation column as the energy ladders and add concise semantic labels for its axes/angle.
- Keep coral and teal for two components, but replace the current light-blue `sage` role with a package-derived muted green such as `wes.get_palette("Moonrise2")[0]` or `wes.get_palette("Cavalcanti1")[3]`. This restores a red/teal/green triad closer to the reference and gives better separation from teal.

## Semantic color-role audit

Current cross-panel roles are partly systematic:

- `ink`/`neutral` consistently use the near-black final color of `Moonrise1` for schematic ink, IQ background, baseline population traces, guides, and the spin circle.
- `coral`, `teal`, `sage`, and `orange` consistently resolve through one shared dictionary, so the same role name always renders with the same package color.
- Population cases use coral for the `|2>` case, teal for `|4>`, and the light-blue `sage` role for `|7>`.
- Spin components reuse coral, teal, and `sage`, creating a deliberate connection with the population block.

However, categorical meaning is not fully consistent:

- The `sage` name suggests green but resolves to a light cyan close to teal. This weakens both semantic naming and visual separation.
- In the IQ triptych, repeated basis states can change role between panels. In particular, state 3 and state 6 do not retain one color. This follows the reference's panel-local highlighting, but the baseline does not tell viewers that color is contextual.
- The right IQ target `|7>` uses mustard/orange, while the population `|7>` target and its ladder use light cyan. This is the clearest cross-panel inconsistency if colors are intended to identify target states.
- Tone-response colors form a separate warm ordinal system and do not connect state identities to the IQ/population system. That separation can work, but it should look intentionally ordinal through an ordered key.

Recommended package-based role system:

1. Keep `Moonrise1[-1]` for neutral ink and baselines.
2. Keep `Zissou1[-1]` for the coral/red `|2>` target and `Zissou1[0]` for the teal `|4>` target.
3. Use a genuinely muted green from `Moonrise2[0]` or `Cavalcanti1[3]` for the `|7>` target and the third spin component.
4. Retain a warm mustard/orange only for ancillary readout or sequence emphasis, not for a target state that is green elsewhere.
5. Treat tone states as an explicitly ordinal colormap with an ordered direct-label key, rather than implying that their hues are the same categorical state map used elsewhere.

This system still uses `wesandersonpy` for every semantic color, keeps the characteristic warm/cool palette personality, and improves category separation without claiming perceptual uniformity.

## Recommended layout hierarchy

The highest-value structural revision is a landscape outer grid with two principal columns:

- Left column: compact schematic and paired tone axes on the upper row, tightly tiled IQ triptych below.
- Right column: three population rows plus the spin row, with a slim reserved annotation column for ladders and the conceptual inset.

This restores the reference's visual comparison between calibration/readout structure and time-domain dynamics while keeping all synthetic values and package color APIs unchanged. A shared typographic scale, fewer repeated axis labels, and consistent panel-letter anchors would then make the figure feel like one composition rather than several stacked demonstrations.

## Priority findings

1. **High visual priority:** restore the landscape two-column hierarchy; the current portrait stack is the main loss of reference grammar.
2. **High visual priority:** increase smoothness/density using documented transformations of only the synthetic fixtures, especially for tone curves, IQ clouds, and population traces.
3. **Moderate visual priority:** replace light-blue `sage` with a true package-derived green and make `|2>`, `|4>`, and `|7>` target roles consistent across IQ, population, ladder, and spin contexts.
4. **Moderate visual priority:** reserve space for energy ladders and the spin inset, and improve direct-label/legend placement.
5. **Moderate visual priority:** clarify whether tone colors are ordinal and IQ colors are panel-local; preserve direct labels as redundant encoding.
6. **Low visual priority:** consolidate repeated axis labels and refine line/marker opacity after the structural revision is rendered.

## Limitations and next action

This is a qualitative baseline review, not experimental validation or a quantitative aesthetics claim. No accessibility simulator, color-vision-deficiency transform, pixel metric, data extraction, or scientific comparison was performed.

The host should reconcile this diagnosis with the other four baseline reviews, then assign a separate implementation task if the recommended structure and role system are accepted. The revised script should be rendered into a new generated subdirectory and independently reviewed against this baseline before any image is promoted to the README gallery.
