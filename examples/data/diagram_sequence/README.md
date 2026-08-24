# Synthetic diagram-and-sequence example data

> **SYNTHETIC, NON-EXPERIMENTAL DATA.** Every value in this directory was invented for software demonstration and visual-regression examples. The values were not digitized from the reference image, are not measurements, and must not be used for scientific inference.

This directory supports a later four-panel Matplotlib example: a two-channel pulse-sequence schematic, a time-domain response, and two stacked population sweeps prepared in different illustrative states.

## Files and schemas

### `sequence_events.csv`

One row per schematic event.

- `channel`: schematic baseline (`transmon` or `resonator`).
- `event`: stable machine-readable event name.
- `start_arb`, `end_arb`: invented horizontal positions in arbitrary sequence units.
- `amplitude_arb`: invented pulse height in arbitrary units.
- `render_role`: suggested Matplotlib shape treatment.
- `label`: display text for the event.

The event timings are schematic only and are intentionally independent of the time-domain panel.

### `time_domain_response.csv`

One row per invented time sample.

- `time_us`: illustrative time coordinate in microseconds.
- `data_normalized`: artificial point value, normalized to an illustrative peak of approximately one.
- `fit_normalized`: artificial smooth comparison curve; it is not a fitted result.

The values produce a rounded rise, a peak near the early guide, and a long decay. A later example can show `data_normalized` as red circular markers and `fit_normalized` as a wide pale-red line. Suggested vertical guides are at `0.0` and `2.0` microseconds.

### `population_sweeps.csv`

Tidy population-like demo values, one row per preparation, state, and control setting.

- `preparation`: illustrative preparation label (`state_1` or `state_7`).
- `state`: output series (`P1`, `P2`, `P7`, `P8`, or `P9plus`).
- `nbar_r_max`: invented dimensionless control parameter.
- `population`: artificial bounded ordinate used only for plotting.

Suggested state-color roles are dark red (`P1`), dark blue (`P2`), light blue (`P7`), muted blue-gray (`P8`), and mustard (`P9plus`). Use circular markers without connecting lines. An illustrative transition guide may be placed at `nbar_r_max = 900`. The `state_1` panel can include an inset limited to roughly `0`–`0.055` to reveal the four low-valued series.

## Integrity note

Names resembling state populations are retained only to make the intended plotting layers legible. The dataset is not calibrated, physically validated, fitted, or representative of a device.
