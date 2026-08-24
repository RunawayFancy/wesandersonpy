# Synthetic scatter and simulation-highlight data

> **SYNTHETIC, NON-EXPERIMENTAL DATA.** Every value in this directory was invented solely to exercise a three-panel plotting example. Nothing was digitized from the reference image. The values are not measured, simulated from a physical model, fitted, validated, or physically meaningful.

The fixture mirrors the reference's plot grammar: a tall upper branch diagram and two shorter probability panels sharing a horizontal coordinate. It does not reproduce the source values.

## Files

- `panel_a_branches.csv`: tidy nominal trajectories for four invented branches. Each branch has `simulation` and `experiment` rows. `n_g` is the invented horizontal coordinate, `n_r_crit` the invented response, and `point_id` preserves display order without implying a continuous physical model.
- `panel_a_outliers.csv`: a separate scatter-only layer of invented experimental points. `outlier_group` allows different sparse clouds to be styled or filtered independently.
- `panels_bc_probabilities.csv`: tidy probability traces for panels `b` and `c`. `source` distinguishes simulation, experiment, and the red highlighted simulation in panel b. `replicate_id` provides two artificial experimental point clouds while simulations use replicate zero.

## Plotting notes

Use a three-row `GridSpec` with approximate height ratios `2.6:1:1`, modest vertical spacing, and shared x limits from 0 to 0.25. Panel a uses small orange circles for simulation and smaller dark diamond markers for experiment; draw the points without connecting lines. Panels b and c use the same source-color mapping. Draw `highlight_simulation` in panel b as a solid red line above the scatter and give it an in-panel annotation. Probability values are intentionally bounded from zero to one.

Every data row contains `data_origin=synthetic_non_experimental` as an additional provenance guard.
