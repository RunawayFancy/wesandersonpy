# Synthetic faded-iteration example data

> **SYNTHETIC, NON-EXPERIMENTAL DATA.** Every value in this directory was invented to demonstrate repeated scatter traces and opacity fading. Nothing was digitized from the reference image, and no value is measured, fitted, calibrated, or physically meaningful.

The intended example is a single wide axes containing repeated population-like traces for three series. Older iterations are drawn with lower opacity, while the newest iteration is saturated and visually dominant.

## File and schema

`iteration_populations.csv` is tidy data with one row per iteration, series, and artificial control setting:

- `iteration_id`: invented acquisition/rendering iteration (`iter_01` through `iter_04`).
- `fade_rank`: chronological opacity rank; `1` is faintest and `4` is most opaque.
- `series`: legend grouping (`P0`, `P1`, or `P7`).
- `nbar_r_max`: invented dimensionless x coordinate.
- `population`: artificial bounded y coordinate.

A later script can map `fade_rank` monotonically to alpha, plot small circular markers without connecting lines, and add an illustrative dashed tan transition guide at `nbar_r_max = 900`. Suggested series colors are dark navy (`P0`), brick red (`P1`), and light blue (`P7`). Place a horizontal three-item legend in the upper-right portion of the axes.

The four explicit iterations are deliberately offset from one another so repeated markers form translucent vertical clouds at shared x coordinates. They are visualization fixtures only.
