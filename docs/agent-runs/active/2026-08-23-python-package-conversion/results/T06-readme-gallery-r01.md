# T06 README and palette gallery result r01

## Task and context

- Task: T06, README and palette gallery.
- Context used: `context/conversation-v004.md`, the approved `plan.md`, and `tasks/T06-readme-and-gallery.md`.
- Status: Static implementation complete; example plot exhibits, runtime rendering, and final absolute repository links remain human-controlled release gates.

## Sources inspected

- `AGENT.md` for project permissions, documentation style, provenance, synthetic-data restrictions, the no-Python-execution rule, and subagent reporting requirements.
- `src/wesandersonpy/__init__.py`, `_palette_data.py`, and `palettes.py` for the authoritative version, exports, exact canonical palette values, alias behavior, interpolation seed, validation, colormap construction, and registration semantics.
- `pyproject.toml`, `NOTICE.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, `CITATION.cff`, and `SECURITY.md` for supported Python versions, dependencies, development commands, release state, licensing, and attribution.
- T02 and T03 result reports for the static API and Matplotlib implementation evidence.
- The latest T09, T10 r02, and T11 r02 characterization reports and all five `examples/data/*/README.md` files for the approved synthetic plot cases, schemas, limitations, and provenance statements.
- All five final example scripts and `examples/README.md` for actual command-line options, default output paths, palette calls, and human verification requirements.
- The official Matplotlib color API, Matplotlib colormap creation guide, PyPA packaging tutorial, upstream R project, and `uv` documentation already cited by the approved plan or repository metadata; technical and provenance references are labeled as last reviewed on 2026-08-23.

## Work performed

- Replaced the empty root README with PyPI-renderable Markdown covering the pre-release state, Python support, future PyPI installation, clearly labeled placeholder GitHub installation, editable installation, quick start, complete public API, discrete behavior, continuous interpolation, reversal, discovery, immutability, alias behavior, explicit registration, development checks, provenance, citation, license, non-endorsement, and accessibility limitations.
- Added a complete text reference for all 22 canonical palettes and all 107 exact source hex values, grouped by the 13 associated films. The `Rushmore` alias and the private extended `Zissou1` interpolation seed are documented without presenting either as an additional canonical gallery palette.
- Added a deterministic, hand-authored SVG gallery containing the same 22 palettes and 107 exact source stops in stable package order. The SVG includes a document title, description, per-group accessible labels, and a title for every swatch.
- Linked all five final example scripts and all five synthetic fixture directories. Added exact human rendering commands using each script's final `--data-dir` or `--input` option and `--output` path.
- Explicitly stated that example output PNGs have not been generated, approved, or embedded; a human must render, inspect, approve, and record the package/runtime versions and command before publication. No reference PNG was copied or linked.

## Evidence and checks

- A PowerShell-only parser extracted 22 canonical names and 107 source hex entries from the `PALETTE_DATA` portion of `_palette_data.py`.
- The SVG contains 107 swatch `<title>` hex entries with an exact, case-sensitive, ordered match to all 107 source entries. Every canonical name appears in the SVG.
- The README contains exactly 107 hex entries with an exact, case-sensitive, ordered match to all 107 source entries. Every canonical name appears in the README.
- PowerShell's XML parser accepted `examples/figures/palette_gallery.svg` without error.
- A Markdown link inventory found 23 link/image targets, including 19 local targets; every local target exists after T05 completion.
- Repository inventory confirmed five example scripts and five synthetic data README files.
- Static text checks found no `plotting_example` reference and no embedded Markdown PNG image in the root README.
- The available image inspector could not process the SVG format, so no claim is made that the gallery has been raster-rendered or visually approved.
- No Python file, interpreter, formatter, linter, type checker, test runner, build tool, Twine check, dependency installer, or example renderer was executed.

## Files changed

- `README.md`
- `examples/figures/palette_gallery.svg`
- This result record.

## Limitations and unresolved release gates

- The human has not supplied the GitHub owner, canonical repository URL, or public maintainer identity. The Git installation example is explicitly labeled as a non-working `<owner>` replacement placeholder rather than being presented as a real URL.
- The gallery and repository-document links are relative so they work in the source tree and on GitHub. After the canonical repository URL exists, the human should convert assets and document links needed on PyPI to absolute canonical URLs and verify them through the built long description. Until that metadata exists, visual gallery display on PyPI cannot be guaranteed even though the Markdown is syntactically suitable for its renderer and the complete text palette table remains available.
- None of the five plot PNG exhibits exists or is embedded. This is intentional: the human must run each script, review the nonconfidential output, and authorize committing and embedding it.
- Human visual review is still required for the SVG layout and for GitHub/PyPI rendering. The SVG passed XML and exact-value checks but was not rasterized under the no-Python-execution agreement.

## Recommended next action

Have an independent verifier compare the README and SVG against the T06 acceptance criteria and current API. Then have the human run the documented quality, build, long-description, and five example-rendering commands; review every generated image; provide the canonical GitHub URL; replace release placeholders and relative PyPI asset links; and approve only nonconfidential exhibits for embedding.
