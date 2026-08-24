# T10 result: fidelity and scatter/simulation references

This r02 report supersedes r01 for Markdown style only. Its substantive content is unchanged; sentences are no longer hard-wrapped before completion, as required by `AGENT.md`.

## Scope and provenance

Inspected only these assigned files:

- `plotting_example/Fidelity_plots_with_multi_params.png`
- `plotting_example/Scattered_dataplot_with_highlight_simulation_result.png`

This report records visual construction and qualitative behavior only. No values were digitized or transcribed. All CSV values created for this task are independently invented, synthetic, non-experimental, and not physically meaningful.

## Fidelity multi-parameter figure

### Geometry and axes

- One nearly square plotting panel with generous left and bottom margins.
- Horizontal axis is logarithmic, spanning roughly three decades. Major ticks are formatted as powers of ten, and minor log ticks appear without labels.
- Horizontal label is mathematical: `2*pi/(Omega*T)`; vertical label is `Fidelity`.
- Vertical scale runs from approximately zero to one, with sparse major labels at the endpoints. The frame is visible on all four sides and there is no grid or title.

### Layers and encodings

- Five parameter series are shown and identified in a compact, frameless legend inside the lower-left corner: `j = 1`, `2`, `3`, `4`, and `8`.
- Each series combines discrete markers with a thin solid connecting/guide line.
- Marker identities are circle, square, downward triangle, upward triangle, and open circle respectively. The first four appear filled; the last uses a hollow center.
- Colors are visually distinct: muted coral/red, dark teal, sage green, ochre/orange, and mauve/purple.
- At the large-x side, a color-matched short dotted horizontal segment indicates a series-specific limiting level. These guides are separate plot layers and are not legend entries.
- There are no uncertainty bars or filled uncertainty bands.

### Qualitative trends

- All curves begin high at small x and eventually decrease.
- `j = 1` falls most gradually and approaches the highest nonzero level.
- Higher parameter values transition earlier/more steeply and finish closer to zero; the `j = 8` series has a visibly irregular shoulder/dip before its sharp descent.
- The dotted levels are ordered consistently with the large-x ends of the solid curves.

### Likely fields for recreation

- parameter identifier (`parameter_j`)
- logarithmic coordinate (`x_scaled`)
- marker value (`marker_fidelity`)
- smooth/guide-line value (`line_fidelity`)
- asymptote extent and height (`x_start`, `x_end`, `asymptote_fidelity`)
- marker/color metadata supplied by the plotting script

## Scatter plot with highlighted simulation

### Figure geometry and axes

- Three panels are stacked vertically and aligned to the same left/right bounds. The upper panel `(a)` is about 2.5 to 3 times the height of either lower panel; `(b)` and `(c)` are compact strips.
- Panel letters sit outside the axes at upper left in serif type.
- All panels use a horizontal variable labelled `n_g` and span approximately 0 to 0.25. Panels `(a)` and `(c)` show x labels and tick labels; panel `(b)` suppresses them at its shared boundary.
- Panel `(a)` uses a vertical quantity labelled `n_(r,crit)` with several numerical ticks. Panels `(b)` and `(c)` use `P_0`, bounded from zero to one with endpoint tick labels.
- Axes use a boxed frame, inward ticks, no grid, and compact vertical gaps.

### Panel (a): branch diagram

- Two scatter layers are distinguished by both color and marker: simulation is orange with small circular marks, while experiment is dark blue-gray with still smaller diamond-like marks.
- The legend sits centered above the upper axes in a single horizontal row.
- Several trajectories coexist: a short high-valued rising branch at the far left, a broadly descending branch, a long rising arch that turns downward on the right, and a shorter middle branch. The experiment layer tracks these structures imperfectly.
- Sparse dark experimental points away from nominal branches create conspicuous central and right-side outlier clouds. No lines, error bars, or fills connect the branch points.

### Panel (b): probability with highlighted trace

- Orange simulation markers describe a probability that starts high, falls to a middle plateau, jumps to near one in the right half, and contains a narrow right-side notch.
- Dark experimental diamonds form a noisier cloud around the same broad regimes, especially around transitions.
- A solid red highlighted simulation line overlays the scatter. It includes narrow local dips/peaks in the middle region and the same late notch.
- A short red line sample and text annotation identifying the highlighted simulation are placed inside the panel near its lower center. This acts as a local legend rather than joining panel `(a)`'s source legend.

### Panel (c): second probability strip

- Orange simulation circles remain near one over most of the range, enter a broad mid-right depression, then recover.
- Dark experiment diamonds show a noisier version with extra localized scatter near the left and around the depression.
- A two-entry in-panel legend lies along the lower portion: simulation at left, experiment at right. No red highlighted line is present.

### Likely fields for recreation

- panel identifier (`a`, `b`, or `c`)
- source/layer (`simulation`, `experiment`, `highlight_simulation`)
- trajectory/branch identifier and point order for panel `(a)`
- shared horizontal coordinate (`n_g`)
- upper response (`n_r_crit`) or lower-panel probability (`p0`)
- experimental replicate identifier
- separate outlier-group identifier for sparse scatter-only points
- marker, color, z-order, and legend-label metadata supplied by the script

## Created artifacts

- `examples/data/fidelity_multi_parameter/README.md`
- `examples/data/fidelity_multi_parameter/fidelity_curves.csv`
- `examples/data/fidelity_multi_parameter/fidelity_asymptotes.csv`
- `examples/data/scatter_simulation/README.md`
- `examples/data/scatter_simulation/panel_a_branches.csv`
- `examples/data/scatter_simulation/panel_a_outliers.csv`
- `examples/data/scatter_simulation/panels_bc_probabilities.csv`

No Python files were run, and no package implementation files or planning records were changed.
