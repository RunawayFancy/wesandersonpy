# T26 result: readout and Rabi visual revision

## Task and status

- Task: T26, revise the readout-calibration/Rabi example from the T23 baseline diagnosis.
- Context: `context/conversation-v007.md` and `results/T23-readout-visual-review-r01.md`.
- Status: **implementation, owned-file quality checks, candidate render, and original-detail visual review complete.**
- Ownership observed: only `examples/readout_calibration_rabi_subplots.py` and this result report were edited. The generated candidate is an authorized ignored output.

No synthetic fixture, package module, reference image, other example, plan, task, or prior report was modified. The reference was used only for qualitative layout, hierarchy, density, and role comparison; no values were extracted or digitized.

## Implemented changes

### Landscape hierarchy

- Replaced the tall three-band composition with a 13.6 x 6.4 inch landscape figure.
- Built a two-column outer grid. The left column contains the compact calibration/readout material: schematic and paired tone axes above a tiled IQ triptych. The wider right column contains the three population rows and spin row.
- Added a narrow annotation column beside the dynamics data. Energy ladders and the SU(2) sketch now occupy their own axes and cannot cover primary traces.
- Consolidated population labeling to one group y label and retained one visible `(d)` anchor. Shared duration axes expose tick labels only on the bottom row.

### Stable package-derived semantic roles

- Retained near-black `Moonrise1[-1]` for ink, baselines, neutral background points, guides, and annotation outlines.
- Retained `Zissou1[-1]` coral for the `|2>` target and `Zissou1[0]` teal for the `|4>` target.
- Replaced the light-cyan `sage` value with the true muted green `Moonrise2[0]` for the `|7>` target and `Jz` component.
- Applied target-state overrides to IQ labels/clouds as well as population traces and ladders, so `|2>`, `|4>`, and `|7>` keep the same coral, teal, and muted-green identities in the relevant regions.
- Assigned IQ state `|6>` the existing package-derived orange role so it remains distinguishable from green `|7>` in the right IQ panel. This IQ-specific separation does not alter the green minor-manifold treatment in the `|7>` population case.
- Introduced no hard-coded hexadecimal colors; a final source scan found zero hex literals.

### Display-only smoothing and mark hierarchy

- Added a cosine-blended display interpolation that passes through every existing synthetic sample. It creates smooth paths without modifying fixture rows or presenting interpolated locations as new observations.
- Used the smooth paths for tone, population, and spin curves.
- Retained the original population and spin sample positions as visible markers over the smooth guides, preserving a clear distinction between stored samples and display interpolation.
- Increased minor-population trace opacity modestly while preserving thinner lines and smaller markers than dominant traces.
- Replaced per-minimum tone labels with one ordered colored state key inside the magnitude axis. Tone labels now read III, II, I from left to right to match the qualitative reference ordering.

### Annotation and schematic cleanup

- Reoriented the warm meander as a compact vertical primitive through the existing normalized endpoints rather than a large diagonal element.
- Gave `Control`, `RO`, and omega labels dedicated offsets, eliminating the baseline overlap around the readout burst.
- Generated presentation-only ladder level counts appropriate to the displayed target label and placed each ladder in the reserved annotation column.
- Moved the spin circle into its own annotation axis and added concise `SU(2)`, `Jx`, `Jy`, and `Jz` labels.
- Reduced repeated IQ x labels to one shared visual label on the middle panel while retaining the fixture-consistent convention of I on the horizontal axis and Q on the vertical axis.

## Exact commands and outcomes

All Python commands ran from the repository root after loading Conda's PowerShell hook and activating `wespy` at `E:\conda\envs\wespy`.

Formatting and linting:

```powershell
python -m ruff format examples/readout_calibration_rabi_subplots.py
python -m ruff check examples/readout_calibration_rabi_subplots.py
```

Initial outcome: Ruff reformatted the owned file and lint passed. After the final IQ state-color correction, Ruff reported the file unchanged and lint again passed.

Final verification:

```powershell
python -m ruff format --check examples/readout_calibration_rabi_subplots.py
python -m ruff check examples/readout_calibration_rabi_subplots.py
```

Outcome: `1 file already formatted`; `All checks passed!`; both exit codes 0.

Candidate render:

```powershell
python examples/readout_calibration_rabi_subplots.py --data-dir examples/data/readout_calibration_rabi --output examples/figures/generated/candidate/readout_calibration_rabi_subplots.png
```

Outcome: exit code 0 with:

```text
Saved synthetic demonstration figure to examples\figures\generated\candidate\readout_calibration_rabi_subplots.png
```

The final candidate is 2448 x 1152 pixels at approximately 180 DPI. It remains under the ignored generated directory and was not promoted into the committed gallery.

## Original-detail visual review

The final candidate and `plotting_example/Multiple_subplots_readout_calibration_rabi_data.png` were inspected at original detail.

### Confirmed improvements over the baseline

- The landscape composition now communicates the same high-level relationship as the reference: calibration/readout context on the left and duration dynamics as the dominant right-hand block.
- All four panel letters are visible and aligned with their group starts. The synthetic disclaimer remains visible below the figure.
- The schematic reads as a compact connected sequence. `Control`, `RO`, and omega no longer collide.
- Tone curves are visibly smoother, and the single ordered state key is easier to scan than labels scattered at individual minima.
- IQ axes read as one triptych instead of three unrelated panels. Target-state labels have stable colors, and orange `|6>` is visibly distinct from muted-green `|7>` in the right panel.
- Population curves are smooth while original synthetic samples remain visible as markers. Dominant and minor traces remain distinguishable through line width, marker size, opacity, direct labels, and color.
- Coral `|2>`, teal `|4>`, and muted-green `|7>` form a clearer target progression than the baseline's teal/light-cyan pair.
- Ladders, ladder labels, and the SU(2) sketch no longer obscure data. The ladder complexity now visually distinguishes the three target cases.
- The spin row has a clear red/teal/green component triad, readable legend, and labeled conceptual annotation.

### Preserved key grammar

- Schematic primitives, paired tone axes, three IQ panels, three population panels, spin-expectation row, direct state labels, dotted population guides, energy ladders, and conceptual spin inset are all retained.
- Every displayed value still originates from the authorized synthetic fixture rows. Interpolation is presentation-only and is explicitly described in the source helper docstring.
- Color is reinforced by geometry, direct labels, markers, line weight, opacity, and legends; no critical distinction relies on hue alone.

## Remaining limitations

- IQ clusters still contain only the six stored points per state. They remain visually sparse compared with the reference, because T26 authorized interpolation for paths but did not require adding deterministic jitter-derived cloud points. A later revision could use the fixture README's documented fixed-seed densification policy if the human wants closer cloud grammar.
- The tone curves remain a warm `GrandBudapest1` ordinal family whose adjacent hues can be similar. The ordered state key mitigates this, but the palette is not perceptually uniform and should not be treated as a quantitative scale.
- A few compact IQ state labels sit close to their six-point clusters, and the nine-item tone key is intentionally dense within the small magnitude axis. Both remain legible at the reviewed original resolution, but they are minor crowding points to revisit if the figure is reduced substantially for publication.
- Display interpolation deliberately smooths transitions through sparse synthetic samples; it is not a fit and must remain labeled as presentation-only.
- The candidate retains I on the horizontal IQ axis and Q on the vertical axis because that matches the fixture column semantics and the conventional naming used by the script. This differs from the visible reference label orientation but is an intentional schema-consistent choice.
- Exact font rendering and final readability can vary across Matplotlib backends. The candidate was visually reviewed in the current Windows `wespy` environment only.

## Files changed and outputs

Owned implementation file:

- `examples/readout_calibration_rabi_subplots.py`

Owned result:

- `docs/agent-runs/active/2026-08-23-python-package-conversion/results/T26-readout-visual-revision-r01.md`

Authorized ignored output:

- `examples/figures/generated/candidate/readout_calibration_rabi_subplots.png`

## Final decision

T26 acceptance criteria are satisfied. The script uses package-derived semantic colors only, renders a landscape calibration-versus-dynamics hierarchy, preserves all synthetic fixture values and four region groups, keeps target-state roles consistent across relevant panels, reserves clear annotation space, passes owned-file Ruff formatting/lint checks, and renders successfully in `wespy`. The candidate is ready for host reconciliation and later human approval, but it must not be promoted to the README gallery without that approval.
