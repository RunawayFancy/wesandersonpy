# Synthetic fidelity multi-parameter data

> **SYNTHETIC, NON-EXPERIMENTAL DATA.** Every value in this directory was invented for a plotting demonstration. The values were not digitized from the reference figure and are not measured, fitted, validated, or physically meaningful.

The files support a single Matplotlib panel with a logarithmic horizontal axis, five parameter series, markers over smooth lines, and short dotted asymptote guides at the right edge.

## Files

- `fidelity_curves.csv`: one row per parameter and horizontal-axis coordinate. `marker_fidelity` supplies the plotted marker and `line_fidelity` supplies the connected guide curve. `parameter_j` identifies the five legend entries.
- `fidelity_asymptotes.csv`: one dotted horizontal segment per parameter. `x_start` and `x_end` delimit the segment and `asymptote_fidelity` gives its height.

## Schema and plotting notes

`x_scaled` is a dimensionless invented coordinate intended to be labelled `2*pi/(Omega*T)` with mathematical typesetting. Plot it on a log scale. Both fidelity columns and `asymptote_fidelity` are dimensionless and deliberately bounded between zero and one. `data_origin` is repeated in every CSV row as an additional provenance guard.

Suggested visual encodings are circles for `j=1`, squares for `j=2`, downward triangles for `j=3`, upward triangles for `j=4`, and open circles for `j=8`. Use the same palette color for a series' marker, solid line, and dotted asymptote.
