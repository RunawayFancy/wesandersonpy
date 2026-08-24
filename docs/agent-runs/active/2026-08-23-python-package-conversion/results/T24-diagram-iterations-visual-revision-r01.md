# T24 result: diagram and faded-iteration visual revision

## Task and status

- Task: T24, implement the reconciled T21 visual recommendations in the two assigned example scripts.
- Context: `context/conversation-v007.md` and `results/T21-diagram-iterations-visual-review-r01.md`.
- Status: implementation, scoped formatting/linting, candidate rendering, and original-detail visual review complete.

Only the two assigned scripts were edited. Synthetic fixture values, package code, other examples, references, and prior reports were not changed.

## Implementation changes

### `examples/diagram_sequence_time_domain.py`

- Replaced the single five-color categorical assignment with explicit package-derived roles: `Zissou1` red for `P1`, `Moonrise1` near-black for `P2`, `Zissou1` light blue for `P7`, `Royal1` blue-gray for `P8`, and `Zissou1` mustard for `P9plus`.
- Added redundant circle, square, up-triangle, open-diamond, and down-triangle markers so state identity no longer depends only on color.
- Replaced machine-like legend text with explicit ket-style mathematical display labels.
- Changed timing and transition guides to a muted `Moonrise2` beige.
- Made sequence event labeling pulse-aware: state preparation remains centered above its pulse, spectroscopy moves beside its pulse, and resonator labels sit beside their associated blocks. Upper-channel text uses near-black ink while resonator text follows the red channel.
- Reduced the response-guide width and opacity so synthetic points remain the primary layer.
- Reduced the inset footprint, focused it on the early low-value region, limited its tick count, and changed the highlight/connectors to the muted guide color.
- Tightened vertical allocation and the lower population y-range while retaining every fixture value.
- Increased the panel (b)/(c) separation after the first candidate revealed that the response x-axis label collided with the population legend.

### `examples/multiple_iterations_faded.py`

- Assigned package-derived semantic roles: `BottleRocket2` dark navy for `P0`, `Royal1` brick red for `P1`, and `Zissou1` light blue for `P7`.
- Changed the regime guide to muted `Moonrise2` beige and reduced its visual weight.
- Compressed the alpha progression so the oldest iteration remains readable, retained the newest as dominant, and added explicit z-order by fade rank.
- Slightly reduced marker size to make vertical iteration stacks lighter.
- Added proper subscripted mathematical legend labels and reduced/repositioned the panel letter.

No hard-coded hexadecimal colors or non-package categorical color sets were introduced.

## Commands and execution evidence

The Conda PowerShell hook was loaded and `wespy` was activated.

Scoped formatting and linting:

```powershell
python -m ruff format `
  examples/diagram_sequence_time_domain.py `
  examples/multiple_iterations_faded.py

python -m ruff check `
  examples/diagram_sequence_time_domain.py `
  examples/multiple_iterations_faded.py
```

Final result:

```text
2 files left unchanged
All checks passed!
```

Candidate rendering:

```powershell
python examples/diagram_sequence_time_domain.py `
  --data-dir examples/data/diagram_sequence `
  --output examples/figures/generated/candidate/diagram_sequence_time_domain.png

python examples/multiple_iterations_faded.py `
  --input examples/data/multiple_iterations/iteration_populations.csv `
  --output examples/figures/generated/candidate/multiple_iterations_faded.png
```

Both scripts completed with exit code 0. Generated candidates:

- `examples/figures/generated/candidate/diagram_sequence_time_domain.png`, 1296 x 1728 pixels, 142,332 bytes.
- `examples/figures/generated/candidate/multiple_iterations_faded.png`, 1512 x 594 pixels, 61,687 bytes.

A final static scan found zero lines longer than 88 characters and zero hard-coded hexadecimal color literals across the two owned scripts.

## Original-detail visual inspection

Each candidate and its correspondingly named reference under `plotting_example/` was viewed at original detail. Comparison remained qualitative; no reference values were extracted or inferred.

### Revised diagram candidate

- All four sequence labels are now separated and readable. Their placement communicates pulse association more clearly and no label collision remains.
- The response guide now reads as a comparison line rather than a dominant band; red points remain clear above it and muted timing guides recede appropriately.
- The state legend has clear mathematical labels, and all five series can be distinguished through marker geometry as well as color. The near-black, red, light-blue, blue-gray, and mustard roles better match the reference's categorical hierarchy.
- The smaller inset is readable, uses three x ticks and three y ticks, and focuses on the low-valued early region. Its beige outline/connectors are subordinate to the data.
- The lower panel's tighter range removes most unused vertical space and brings its preparation annotation into a more coherent relationship with the plotted series.
- The first rendered candidate exposed a blocking collision between panel (b)'s x label and panel (c)'s legend. Increasing grid spacing resolved it; the final candidate has clean separation.

### Revised faded-iteration candidate

- Dark navy `P0`, brick-red `P1`, and light-blue `P7` are immediately distinguishable and match the documented/reference role hierarchy.
- Four chronological layers remain visible for every series. The newest points are dominant, while the oldest remain legible instead of disappearing into the white background.
- The muted beige guide no longer competes with the primary series.
- Proper subscripts and the smaller panel tag improve publication-style polish.
- The wide boxed layout, marker-only traces, horizontal upper-right legend, and fading grammar remain consistent with the reference.

## Acceptance matrix

| Criterion | Result | Evidence |
|---|---|---|
| No hard-coded hexadecimal or non-package categorical set | Pass | Static scan found zero hex literals; roles use `get_palette`. |
| Diagram labels do not overlap | Pass | Final original-detail candidate inspection. |
| State categories have redundant identification | Pass | Five distinct marker treatments plus explicit colors/labels. |
| Faded plot has dark navy, brick red, light blue, and muted guide | Pass | Package-derived role mapping and candidate inspection. |
| Both scripts run in `wespy` | Pass | Both candidate commands exited successfully. |
| Owned files format and lint cleanly | Pass | Ruff format and lint pass on both paths. |
| Both candidate/reference pairs inspected at original detail | Pass | Two final candidates and two authorized references inspected. |
| Synthetic-data notices retained | Pass | Visible italic footer remains on both candidates. |

## Remaining limitations

- The diagram remains intentionally more spacious and uses modern sans-serif typography rather than duplicating the reference's compact serif styling.
- The synthetic fixtures have fewer horizontal samples than the visual references; no data were added or altered to imitate reference density.
- Level diagrams remain simplified conceptual annotations and must not be interpreted physically.
- No color-vision-deficiency simulation, print proof, or alternate-background review was performed.
- Candidate PNGs remain ignored staging artifacts and have not been promoted to `examples/figures/`.

## Recommended next action

Request independent candidate verification across layout, legibility, synthetic labeling, and source/fixture integrity. If that review passes, present the candidate PNGs to the human maintainer for explicit nonconfidential exhibit approval before promotion.
