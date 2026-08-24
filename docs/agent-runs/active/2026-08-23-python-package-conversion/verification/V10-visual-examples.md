# V10: Independent visual verification of revised plotting examples

## Verification identity and verdict

- Task: T27, independent verification of the five revised plotting examples.
- Context: `context/conversation-v007.md`.
- Verification date: 2026-08-23.
- Verdict: **Pass; all five revised examples are exhibit-ready for human maintainer review.** No blocking overlap, clipping, color-role, rendering, lint, formatting, or test defect was confirmed. The generated review PNGs remain staging artifacts and were not promoted or published.

This verdict means that each example is a coherent qualitative demonstration of intentional `wesandersonpy` color selection. It does not establish quantitative aesthetic superiority, scientific accuracy, or fitness for publication at every output size.

## Scope and boundaries

I independently inspected the current five scripts, rendered them from only their bundled synthetic CSV fixtures, and compared every fresh PNG with its correspondingly named authorized reference under `plotting_example/` at original detail. Reference images were used only for qualitative layout, hierarchy, plotting grammar, and color-role comparison. I did not digitize, transcribe, estimate, or extract values from any reference and did not inspect or use experimental data.

I remained read-only with respect to implementation files, fixtures, references, prior reports, task files, context files, and the plan. No fix was applied. The only persistent authored file is this verification report; the five final-review PNGs are authorized ignored outputs.

## Environment

The Conda PowerShell hook activated `wespy` successfully:

- `CONDA_PREFIX`: `E:\conda\envs\wespy`
- Python: 3.12.12 from `E:\conda\envs\wespy\python.exe`
- `wesandersonpy`: 0.1.0 installed editable from the repository
- Matplotlib: 3.11.1
- NumPy: 2.5.2
- Pytest: 9.1.1
- Ruff: 0.16.4

`pip list` contains the editable package and the development/example dependencies requested through `requirement.txt`.

## Rendering evidence

The following commands ran from the repository root after activating `wespy`; all five exited 0 and printed their expected synthetic-figure save confirmations:

```powershell
python examples/diagram_sequence_time_domain.py --data-dir examples/data/diagram_sequence --output examples/figures/generated/final-review/diagram_sequence_time_domain.png
python examples/multiple_iterations_faded.py --input examples/data/multiple_iterations/iteration_populations.csv --output examples/figures/generated/final-review/multiple_iterations_faded.png
python examples/fidelity_multi_parameter.py --data-dir examples/data/fidelity_multi_parameter --output examples/figures/generated/final-review/fidelity_multi_parameter.png
python examples/scatter_with_simulation.py --data-dir examples/data/scatter_simulation --output examples/figures/generated/final-review/scatter_with_simulation.png
python examples/readout_calibration_rabi_subplots.py --data-dir examples/data/readout_calibration_rabi --output examples/figures/generated/final-review/readout_calibration_rabi_subplots.png
```

Fresh output and reference dimensions, reported only to identify the inspected artifacts, were:

| Pair | Final-review PNG | Reference PNG |
|---|---:|---:|
| Diagram sequence and time domain | 1296 x 1728 | 588 x 839 |
| Multiple faded iterations | 1512 x 594 | 527 x 249 |
| Multi-parameter fidelity | 972 x 792 | 467 x 348 |
| Scatter with simulation | 1116 x 1332 | 593 x 675 |
| Readout calibration and Rabi subplots | 2448 x 1152 | 1024 x 499 |

Every final-review PNG and its corresponding reference PNG was opened at original detail for the observations below.

## Independent visual observations

### Diagram sequence and time domain

- The four-part vertical narrative, sequence channels, response panel, aligned population panels, transition guides, inset, legends, and right-side preparation sketches preserve the reference's key grammar and hierarchy without copying reference values.
- `State prep.`, `Spectroscopy pulse`, `Stimulation pulse`, and `Measurement` are clearly separated. Panel tags, axes labels, population legend, inset, preparation annotations, and the synthetic footer are visible without blocking overlap or clipping.
- The discrete state roles are intentional and package-derived: red, near-black, light blue, blue-gray, and mustard are reinforced by distinct filled/open marker geometries and mathematical labels. The muted beige guides recede behind the data.
- The composition is more spacious than the compact reference, but the extra space does not break the hierarchy.

### Multiple faded iterations

- The wide boxed panel, marker-only repeated traces, chronological fading, upper-right horizontal legend, transition guide, and external panel tag preserve the reference grammar.
- Dark navy `P0`, brick red `P1`, and light blue `P7` are harmonious on white and remain distinguishable at every opacity. The newest layer is dominant and the oldest layer remains visible; the muted guide is subordinate.
- Mathematical legend labels, axes text, panel tag, and synthetic footer are fully visible and do not collide.

### Multi-parameter fidelity

- The near-square boxed axes, logarithmic domain, five guide/marker series, categorical legend, and right-side dotted asymptotes preserve the reference hierarchy.
- A discrete `Cavalcanti1` palette correctly represents five categorical cases. Marker shape, fill state, line, and legend labels redundantly identify every case, including the hollow `j=8` series.
- The restrained red-brown, dark green, muted sage, mustard, and blue-green family is balanced on white. The muted `j=3` and `j=8` roles are closer in visual weight than the other pairs, but their different shapes and fill states prevent ambiguity at the reviewed resolution.
- No axis, legend, footer, or asymptote is clipped or blocked.

### Scatter with simulation

- The tall upper branch panel, two compact probability panels, shared horizontal domain, external panel tags, top source legend, local highlighted-trace key, and lower legend preserve the reference's main plot grammar.
- Warm burnt-orange circles represent simulation, dark teal diamonds represent experiment, and the solid red line is reserved for the highlighted synthetic trace. Shape, line, legend, and direct text redundantly support all color roles.
- Panel `(a)`'s lower axis title is visible between panels, and all tags, legends, annotations, ticks, axes titles, and the synthetic footer have clear separation.
- The synthetic fixture is substantially sparser than the reference. This reduces trajectory density but does not obscure the intended comparison and is preferable to inferring or fabricating reference-like points.

### Readout calibration and Rabi subplots

- The revised landscape layout restores the reference's high-level hierarchy: compact control/readout, tone, and IQ material on the left; population and spin dynamics in the dominant right block; and a reserved annotation column for ladders and the SU(2) sketch.
- All four panel tags are visible. The schematic labels and primitives are separated, tone axes and their ordered state key are readable, the IQ triptych behaves as one group, dynamics labels remain outside the data, and ladders and spin annotations do not cover primary traces.
- Coral/red `|2>`, teal `|4>`, and muted-green `|7>` targets are stable across relevant IQ, population, ladder, and spin roles. Near-black establishes the baseline hierarchy. Direct labels, marker samples, line weight, opacity, legends, and geometry keep meaning from depending on color alone.
- The tone key and several IQ direct labels are compact and close to their marks, but remain legible at original detail and do not constitute a blocking overlap. IQ clouds remain sparse because the fixture contains only the approved synthetic points.
- The synthetic/non-experimental footer is fully visible beneath the landscape composition.

## Quality and test evidence

Scoped commands:

```powershell
python -m ruff check examples/diagram_sequence_time_domain.py examples/multiple_iterations_faded.py examples/fidelity_multi_parameter.py examples/scatter_with_simulation.py examples/readout_calibration_rabi_subplots.py
python -m ruff format --check examples/diagram_sequence_time_domain.py examples/multiple_iterations_faded.py examples/fidelity_multi_parameter.py examples/scatter_with_simulation.py examples/readout_calibration_rabi_subplots.py
python -m pytest
```

Results:

- Ruff lint: pass, `All checks passed!`.
- Ruff format check: pass, all five files already formatted.
- Pytest: pass, 79 tests passed in 0.53 seconds.
- Pytest emitted three `MatplotlibDeprecationWarning` instances for passing `N` to `ListedColormap` in `src/wesandersonpy/palettes.py:101`. This is an existing package-maintenance warning and did not cause a render or test failure.
- Static scan across all five scripts: no hard-coded 3-, 6-, or 8-digit hexadecimal color literal found.

## Acceptance matrix

| Acceptance criterion | Result | Independent evidence |
|---|---|---|
| Every script exits successfully and visibly identifies synthetic/non-experimental data | Pass | Five final-review renders exited 0; each footer was visible at original detail. |
| No blocking overlap or clipping | Pass | Every final-review PNG inspected at original detail; labels, legends, tags, insets, and footers remain readable. |
| Reference plotting grammar and hierarchy are preserved without copying values | Pass | Pair-by-pair qualitative observations above; only bundled fixtures were supplied to the scripts. |
| Package-derived colors are intentional, harmonious on white, and redundantly encoded | Pass | Palette roles are supported by markers, fill, lines, opacity, labels, legends, or geometry in every example. |
| Fidelity uses a discrete categorical palette | Pass | Five explicit categorical roles plus five marker treatments. |
| Faded iterations separate navy, red, and light blue | Pass | All three roles and four opacity levels are visible. |
| Scatter separates warm simulation, dark experiment, and red highlight | Pass | Circle, diamond, and solid-line redundancy is consistent across panels. |
| Readout uses landscape hierarchy and stable red/teal/green targets | Pass | Two-column composition and cross-panel target roles confirmed visually. |
| Ruff, formatting, tests, and no-hard-coded-hex checks pass | Pass | Scoped checks and 79-test run recorded above. |

## Findings ordered by severity

### Confirmed blocking defects

None.

### Low V10-L01: fixture density differs visibly from several references

The scatter trajectories and readout IQ clouds contain fewer marks than their references, and the diagram/faded examples also sample their domains more sparsely. This is a known synthetic-fixture limitation, not a rendering defect. No reference-derived points should be added to close the density gap.

### Low V10-L02: a few categorical or direct-label regions merit reduced-size human review

The fidelity `j=3` and `j=8` roles are both muted, while the readout tone key and a few IQ labels are compact. Redundant marker/fill/direct-label encodings make them unambiguous at original detail, but a human should recheck them at the exact README or publication display size.

### Informational V10-I01: Matplotlib deprecation warnings remain

The repository tests pass, but three tests warn that `ListedColormap(N=...)` will be removed in Matplotlib 3.13. This warning is outside the visual-example implementation scope and should be handled as separate package maintenance.

## Untested areas and subjective limitations

- No color-vision-deficiency simulation, grayscale conversion, print proof, projector check, or alternate-background evaluation was performed.
- No reduced-resolution README rendering or alternate Matplotlib backend was tested; original-detail Windows rendering was the visual basis.
- The palettes are artistic categorical palettes, not guaranteed perceptually uniform scales. Redundant forms mitigate but do not remove the need for human accessibility review.
- Aesthetic harmony is necessarily subjective. This review confirms coherent, intentional roles and improved semantic discipline over arbitrary color assignment; it does not claim a measurable or universal aesthetic advantage.
- Static and visual review of synthetic demonstrations is not experimental or scientific validation.

## Final recommendation

The five final-review images are ready to be shown to the human maintainer as candidate exhibits. Human approval should precede copying any ignored final-review PNG into a committed README/gallery location. The two low limitations and the unrelated Matplotlib deprecation warning do not block that review.
