# T22 fidelity and scatter baseline visual review r01

## Task, context, and status

- Task: T22, fidelity and scatter baseline visual review.
- Context: `context/conversation-v007.md`.
- Inspection date: 2026-08-23.
- Status: **Complete with improvement findings.** Both unchanged scripts rendered successfully from bundled synthetic fixtures, and both generated/reference pairs were inspected at original detail. The baseline images should not be promoted as approved exhibits yet.

## Scope and integrity

I inspected `examples/README.md`, the two assigned scripts, and their two synthetic fixture READMEs. I rendered only the assigned scripts into `examples/figures/generated/baseline/` and visually compared each generated PNG with its corresponding authorized reference PNG under `plotting_example/`.

The references were used only for qualitative layout, hierarchy, encoding, and color-role comparison. I did not digitize, transcribe, estimate, or extract plotted measurements. The generated figures use only independently invented CSV fixtures under `examples/data/`. No script, fixture, package module, reference image, or prior report was edited.

## Render evidence

The Conda PowerShell hook activated `wespy`; `Get-Command python` resolved to `E:\conda\envs\wespy\python.exe`, and the interpreter reported Python 3.12.12.

Commands:

```console
python examples/fidelity_multi_parameter.py --data-dir examples/data/fidelity_multi_parameter --output examples/figures/generated/baseline/fidelity_multi_parameter.png
python examples/scatter_with_simulation.py --data-dir examples/data/scatter_simulation --output examples/figures/generated/baseline/scatter_with_simulation.png
```

Both commands exited `0` and printed their expected save confirmations. PowerShell image inspection recorded:

| Image | Dimensions | File size |
|---|---:|---:|
| Generated fidelity baseline | 1026 x 936 | 99,460 bytes |
| Fidelity reference | 467 x 348 | 43,685 bytes |
| Generated scatter baseline | 1170 x 1476 | 102,955 bytes |
| Scatter reference | 593 x 675 | 135,959 bytes |

These dimensions are file properties only and are not measurements extracted from plotted content.

## Fidelity multi-parameter review

### Preserved visual grammar

- The generated figure retains the reference's single near-square boxed axes, logarithmic horizontal scale, five parameter series, lower-left frameless legend, solid guide curves, discrete markers, and right-side dotted asymptote segments.
- Marker shapes preserve redundant categorical encoding: circles, squares, downward triangles, upward triangles, and a hollow circle. The hollow `j=8` series remains distinguishable without relying only on hue.
- Each series consistently reuses one color for its marker, line, and asymptote, so the visual mapping is internally coherent.
- The broad hierarchy is readable: the red upper curve is dominant, the other curves separate through their descent, and the synthetic-data footer is clear without being mistaken for an axes label.

### Shortcomings and diagnosis

- **Discrete-versus-continuous semantics are mismatched.** The five `j` cases are presented as five explicit legend categories with distinct marker shapes, but colors are obtained by sampling `get_colormap("Darjeeling1", kind="continuous")`. Because the five samples land across a qualitative multi-hue palette, the code communicates neither a perceptually ordered continuous scale nor an explicitly discrete palette choice. No colorbar or continuous legend supports a continuous interpretation.
- The gold/down-triangle and orange/up-triangle series are visually close, especially where their descending curves cross the same region. Their opposite marker orientations help, but the lines and dotted asymptotes still depend heavily on similar warm hues.
- The cyan hollow-circle series is clearly visible against white, yet it is less harmonious with the red/teal/warm cluster than the muted mauve role in the reference. The result feels like five independently vivid accents instead of one restrained categorical family.
- Markers, legend spacing, axes labels, and overall canvas are larger and heavier relative to the plotting region than in the compact reference. The spacious result is readable, but the legend attracts more attention than necessary and the figure loses some of the reference's publication-style density.
- The current saturated red receives substantially more visual weight than the other series. This is defensible if `j=1` is intended as the focal condition, but the script does not otherwise establish that hierarchy.

### Recommended package-palette-based changes

1. Use `wes.get_palette(...)` for the five fixed series unless the design explicitly changes to a true ordered color scale with a colorbar. This makes the discrete semantics visible in the code and documentation.
2. A concrete cohesive candidate is `Cavalcanti1`, reordered by semantic role rather than source position: red for `j=1`, dark green for `j=2`, sage for `j=3`, mustard for `j=4`, and blue-gray for the hollow `j=8`. In package-index terms, that candidate is `{1: palette[4], 2: palette[1], 3: palette[2], 4: palette[0], 8: palette[3]}`. Human rendering should decide whether the red/green distinction has enough contrast; the existing marker-shape redundancy must remain.
3. If `Darjeeling1` is retained, obtain it with `get_palette("Darjeeling1")`, explicitly reorder the source colors to maximize adjacent-series separation, and document that the hues are categorical rather than interpolated magnitude.
4. Reduce marker and legend scale modestly while keeping marker shapes and the hollow-circle treatment. This would restore compact hierarchy without changing data or scientific meaning.

## Scatter and highlighted-simulation review

### Preserved visual grammar

- The three vertically stacked boxed panels, shared horizontal domain, tall upper branch panel, two compact probability strips, outside-left panel letters, top source legend, and lower-panel legend structure all match the reference's essential organization.
- Simulation and experiment are redundantly distinguished by color and marker shape: orange circles versus cyan diamonds. The same mapping remains consistent across all three panels.
- The red highlighted trace in panel `(b)` is visually unmistakable, stays above the point layers, and has an in-panel red line key. Reserving red for the highlight creates a sound emphasis hierarchy.
- The script uses `get_palette("FantasticFox1")` for discrete semantic roles, which is appropriate: source identity and highlighted status are categories, not values on a continuous scale. No unnecessary colorbar is introduced.
- Panel `(c)` keeps its source legend away from the dense upper trace region, and the synthetic-data footer clearly limits interpretation.

### Shortcomings and diagnosis

- The cyan experiment layer is much lighter than the reference's dark blue-gray layer. It remains distinct from orange, but its sparse outliers and branch deviations have low visual authority on white, so the nominal orange simulation often dominates even where experimental scatter is the intended story.
- The generated fixture is visually much sparser than the reference, especially along the upper-panel branches and in the two probability strips. The key branch shapes remain recognizable, but individual paired points dominate over trajectory structure. This is a fixture-density limitation, not evidence that values should be inferred from the reference.
- Panel `(a)` calls for an `$n_g$` label in the approved grammar, and the script sets one, but the rendered label is visually lost or occluded at the tight boundary above panel `(b)`. The upper x tick labels remain visible, making the missing label especially noticeable.
- The top legend symbols and text are large relative to the point marks, and the generous top whitespace weakens the connection between legend and axes. Panel letters are also much heavier than the reference's restrained serif labels.
- The phrase `Highlighted illustrative trace` is appropriately non-scientific but occupies a long horizontal span. It competes with the panel's data and is less compact than the reference's local annotation.

### Recommended package-palette-based changes

1. Test a single-palette `BottleRocket2` role mapping: golden simulation from `palette[0]`, dark navy experiment from `palette[2]`, and red highlight from `palette[1]`. This retains the reference's warm/dark/red hierarchy, substantially improves experiment contrast on white, and keeps every role package-derived and categorically explicit.
2. Preserve circle-versus-diamond redundancy and the highlight's solid-line encoding regardless of palette choice. This is the strongest accessibility feature in the current figure.
3. Increase vertical spacing around the `(a)`/`(b)` boundary or position the upper `$n_g$` label explicitly so it is visible. Tighten the legend scale/top margin at the same time rather than enlarging the overall canvas.
4. Shorten the local label to a phrase such as `Highlighted synthetic trace` while retaining the red line sample and the non-experimental meaning.
5. Do not synthesize extra points from the reference. If greater visual density is desired, treat that as a separately reviewed synthetic-fixture revision with explicit provenance; otherwise use smaller markers and stronger dark experiment contrast to make the existing structure read more continuously.

## Findings summary

### Moderate T22-F01: fidelity color construction does not match its categorical legend semantics

Five discrete cases are sampled through a continuous multi-hue colormap without a continuous legend, while two warm series remain close in line/asymptote appearance. Change to an explicit discrete package palette and preserve redundant markers.

### Moderate T22-F02: the scatter experiment layer lacks contrast and the upper x label is visually absent

Light cyan diamonds do not carry the structural weight of the reference's dark experimental layer, particularly for sparse outliers, and panel `(a)`'s intended `$n_g$` label is not legible at the tight panel boundary. A dark package-derived categorical role and a small spacing/label-position correction are warranted.

### Low T22-F03: both baselines are oversized and visually heavier than their references

Large markers, legends, typography, and whitespace make both outputs readable but less compact. A restrained scale pass would improve hierarchy without changing fixtures or plot semantics.

## Files produced

- `examples/figures/generated/baseline/fidelity_multi_parameter.png`
- `examples/figures/generated/baseline/scatter_with_simulation.png`
- This result record.

## Recommended next action

The host should reconcile T22 with the other baseline reviews before authorizing implementation. If changes are assigned, keep them scoped to package-derived color-role selection, legend/marker scale, and the confirmed panel-label spacing issue; do not infer new values from the references. Render revisions into a separate generated review directory and obtain human approval before promoting any PNG.
