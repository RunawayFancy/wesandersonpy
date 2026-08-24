# T25 fidelity and scatter visual revision r01

## Task, context, and status

- Task: T25, revise the fidelity and scatter plotting examples after the T22 baseline review.
- Context: `context/conversation-v007.md` and `results/T22-fidelity-scatter-visual-review-r01.md`.
- Inspection date: 2026-08-23.
- Status: **Complete.** Both owned scripts were revised, formatted, linted, rendered from unchanged synthetic fixtures, and compared with their corresponding references at original detail. Candidate images remain ignored review artifacts and have not been promoted.

## Sources and boundaries

I inspected the T25 contract, conversation checkpoint v007, the T22 baseline report, and the two owned scripts. Reference PNGs were used only for qualitative layout, hierarchy, and color-role comparison. No values were digitized or inferred from them.

Only these implementation files were edited:

- `examples/fidelity_multi_parameter.py`
- `examples/scatter_with_simulation.py`

All synthetic fixture values, package modules, reference images, other scripts, and prior reports remain unchanged.

## Fidelity changes

- Replaced continuous colormap sampling with `wes.get_palette("Cavalcanti1")`, making the API match the five categorical legend roles.
- Assigned one intentional discrete mapping: package indices `4`, `1`, `2`, `0`, and `3` for `j=1`, `j=2`, `j=3`, `j=4`, and `j=8` respectively. This gives the series red-brown, dark green, sage, mustard, and blue-green roles without hard-coded color literals.
- Preserved all redundant encodings: circle, square, down-triangle, up-triangle, and hollow circle; the same series color still binds markers, lines, and asymptotes.
- Reduced line and asymptote width from `1.1`/`1.2` to `0.95`, marker size from `5` to `4.2`, and added a controlled marker-edge width.
- Made the legend more compact through a smaller font and restrained label/handle spacing.
- Reduced the canvas from `5.7 x 5.2` to `5.4 x 4.4` inches, modestly increased footer clearance, and retained the visible synthetic-data notice.

## Scatter changes

- Replaced the `FantasticFox1` role mapping with a single cohesive discrete `AsteroidCity2` mapping: warm burnt-orange simulation from package index `5`, dark teal experiment from index `4`, and red highlighted trace from index `0`.
- Preserved circle-versus-diamond source encoding and solid-line highlight encoding, so every role remains redundant with form rather than color alone.
- Reduced nominal marker areas and legend marker size while increasing the dark experiment layer's opacity. Sparse outliers remain separate and slightly smaller; no points were added, removed, interpolated, or invented.
- Reduced panel-letter and legend scale and shortened the local annotation to `Highlighted synthetic trace`.
- Increased GridSpec vertical spacing from `0.08` to `0.18`, added explicit label padding, and reduced the canvas from `6.5 x 8.2` to `6.2 x 7.4` inches. The panel `(a)` `$n_g$` label is now clearly visible between the upper and middle panels.
- Retained the visible synthetic-data notice and all source/provenance language.

## Formatting and static checks

The Conda PowerShell hook activated `wespy`, and `Get-Command python` resolved to `E:\conda\envs\wespy\python.exe`.

Commands and outcomes:

```console
python -m ruff format examples/fidelity_multi_parameter.py examples/scatter_with_simulation.py
python -m ruff format --check examples/fidelity_multi_parameter.py examples/scatter_with_simulation.py
python -m ruff check examples/fidelity_multi_parameter.py examples/scatter_with_simulation.py
```

- Formatting command: exit `0`; both owned scripts were formatted.
- Format verification: exit `0`; both files already formatted.
- Ruff lint: exit `0`; `All checks passed!`.
- A case-insensitive static search found no hard-coded six-digit hexadecimal color in either owned script.
- Static inspection confirms both scripts obtain semantic colors through `wes.get_palette(...)`.

## Render evidence

Commands:

```console
python examples/fidelity_multi_parameter.py --data-dir examples/data/fidelity_multi_parameter --output examples/figures/generated/candidate/fidelity_multi_parameter.png
python examples/scatter_with_simulation.py --data-dir examples/data/scatter_simulation --output examples/figures/generated/candidate/scatter_with_simulation.png
```

Both commands exited `0` and printed their expected save confirmations.

| Image | Dimensions | File size |
|---|---:|---:|
| Fidelity candidate | 972 x 792 | 92,736 bytes |
| Fidelity baseline | 1026 x 936 | 99,460 bytes |
| Scatter candidate | 1116 x 1332 | 93,546 bytes |
| Scatter baseline | 1170 x 1476 | 102,955 bytes |

Dimensions and file sizes are output-file properties only, not measurements extracted from plot content.

## Original-detail visual inspection

### Fidelity candidate versus reference

- The categorical intent is now explicit both in code and appearance. Adjacent legend cases have distinguishable hue/value roles, and the opposite triangle orientations plus hollow `j=8` circle remain effective redundant cues.
- The red-brown upper curve, dark green second curve, muted sage third curve, mustard fourth curve, and blue-green hollow-circle curve form a restrained family closer to the reference's publication-style balance than the saturated baseline.
- The smaller markers and tighter legend preserve readability while reducing competition with the curves. The reference remains more compact, but the candidate's hierarchy is materially closer without compressing labels or the synthetic footer.
- The `j=3` sage and `j=8` blue-green are both muted; they remain distinguishable through hue, marker fill, and shape, but this pair should receive particular attention during human accessibility review.

### Scatter candidate versus reference

- The source hierarchy now matches the intended grammar: warm simulation points, dark structural experimental diamonds, and a reserved red highlighted line. Dark experiment points and outliers remain legible on white and carry more of the branch structure than the baseline cyan layer.
- The simulation/experiment mapping is consistent across all three panels, and marker shapes remain clear after the size reduction.
- Panel `(a)`'s `$n_g$` label is visible at the enlarged boundary, while the panel tags, top legend, and footer remain separate from the axes.
- The shorter highlight annotation fits the middle strip more comfortably and remains explicitly synthetic.
- The branch and probability layers remain sparser than the reference because the bundled synthetic fixtures contain fewer points. The candidate does not conceal that limitation or invent additional samples.

## Acceptance matrix

| Criterion | Result | Evidence |
|---|---|---|
| Semantic colors come from `wesandersonpy` | Pass | Both scripts call `get_palette`; no hex literals found. |
| Fidelity uses a discrete API and distinct adjacent roles | Pass | `Cavalcanti1` tuple mapping plus five redundant markers; candidate inspected at original detail. |
| Scatter keeps warm/dark/red roles and redundant form | Pass | `AsteroidCity2` mapping, circle/diamond sources, solid red highlight. |
| Panel labeling is readable | Pass | Panel `(a)` `$n_g$` label is visible in the candidate. |
| Both owned scripts format and lint cleanly | Pass | Scoped Ruff format-check and lint both exited `0`. |
| Both scripts render in `wespy` | Pass | Both candidate commands exited `0`. |
| Candidate/reference pairs inspected at original detail | Pass | Both candidate PNGs and both corresponding references were inspected. |
| Synthetic values remain unchanged | Pass | No fixture or data file was edited; no point-generation code was added. |

## Files changed and produced

Changed:

- `examples/fidelity_multi_parameter.py`
- `examples/scatter_with_simulation.py`
- This result record.

Generated but intentionally ignored:

- `examples/figures/generated/candidate/fidelity_multi_parameter.png`
- `examples/figures/generated/candidate/scatter_with_simulation.png`

## Remaining limitations and next action

- Artistic palettes are not guaranteed to be perceptually uniform or color-vision-deficiency safe. Marker and line redundancy mitigates but does not eliminate the need for human accessibility review.
- Scatter trajectory density remains limited by the approved synthetic fixture. Any future density change must be a separately reviewed synthetic-data revision, not a transcription from the reference.
- The warm simulation markers and red highlight are intentionally related hues; marker-versus-line form keeps them separate, but the human should confirm the balance at intended publication size.
- The human maintainer should compare the candidates with the other revised examples, review confidentiality and image metadata, and explicitly approve any PNG before copying it from the ignored candidate directory into a committed exhibit path.
