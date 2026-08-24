# V03: Complete static implementation verification

## Verification identity and verdict

- Task: T14, independent verification against `context/conversation-v004.md`, the approved plan, T01 through T07 contracts and latest result revisions, and V01/V02.
- Inspection date: 2026-08-23.
- Method: read-only PowerShell, static source review, XML parsing, CSV parsing, regular-expression comparisons, and command-local Git inspection.
- Overall verdict: **FAIL pending scoped corrections and reverification.** The core package, tests, metadata baseline, gallery value parity, and workflow graph are substantially complete, but three moderate implementation defects should be corrected before the human starts the full T08 matrix.
- T08 readiness: **not ready for efficient human execution yet.** Correct V03-F01 through V03-F03, produce a new static verification report, and then begin T08 with human generation of `uv.lock` followed by the documented runtime/build/render checks.

No Python interpreter, pytest, Ruff, mypy, uv, build, Twine, example renderer, GitHub workflow, or publishing action was run. No implementation file was modified, staged, or committed. This report is the only file written by this verifier.

## Scope and environment

I inspected all current package, test, example, metadata, documentation, and GitHub configuration candidates. In accordance with T14, I did not read the ignored upstream checkout or ignored plot-reference PNG contents; prior T02 exact-upstream evidence and V01/V02 fixture evidence were treated as consumed audit evidence. I inspected only their paths and ignore status.

The first ordinary Git query was refused because the sandbox account does not own the repository. I repeated Git checks with the command-local option `git -c safe.directory=E:/PhD_file/wesandersonpy`; this did not modify local or global Git configuration. The outer repository is an unborn `main` branch with no commits and every candidate file untracked. `git diff --check` produced no tracked-diff finding because there is no commit/index baseline.

Representative read-only methods included `Get-Content -Raw`, `Get-ChildItem -Force`, `Import-Csv`, `[xml]` parsing, `[IO.File]::ReadAllText(..., UTF8)`, `Select-String`, `git ... status --short --branch`, and `git ... check-ignore -v`. Static results below distinguish confirmed source defects from behavior that still requires human execution.

## Pass/fail matrix

| Area | Result | Static evidence |
|---|---|---|
| Repository structure and Git baseline | Pass with human gate | Conventional `src/wesandersonpy`, four test modules, exactly five example scripts, metadata files, and three GitHub configuration files exist. Branch is unborn `main`; no staging or commit exists. |
| Ignore and distribution hygiene | **Fail** | `plotting_example/`, `reference/wesanderson-r/`, credentials, caches, and `examples/figures/generated/` are ignored. However, every script defaults to an unignored PNG directly in `examples/figures/`; see V03-F03. |
| Metadata, version, license, and attribution | Pass | `wesandersonpy` 0.1.0, Python `>=3.10`, Matplotlib `>=3.8,<4`, MIT metadata/license, non-personal contributor fallback, and upstream attribution are mutually consistent. No personal identity or repository URL is fabricated. |
| Palette data and public API | Pass statically | 22 canonical names and 107 hex literals in package source exactly match the independent test oracle in case-sensitive order. `Rushmore` is private alias data for `Rushmore1`; the 11-color `Zissou1` continuous seed is not public. `PALETTES` is a `MappingProxyType` over tuple values. Public exports and version are consistent. |
| Validation and typing | Pass statically | Typed signatures cover the public API. Name, kind, positive integer count, strict boolean reversal/force, prefix, discrete limit, and unknown-name branches are present and reconciled with tests. The PEP 561 marker exists. Runtime type-checker evidence remains human-only. |
| Matplotlib construction and registration | Pass statically | Continuous construction returns `LinearSegmentedColormap`; discrete construction returns `ListedColormap`. Reversal and names are explicit. Registration is inside `register_colormaps`, performs a preflight conflict scan when not forced, and has no import-time registration call. Runtime registry behavior remains human-only. |
| Core test contract | Pass statically | Tests cover exact canonical data/order, immutability, alias/private-seed behavior, selection/interpolation, error branches, Matplotlib types/sizes/endpoints, import side effects, registration conflict/force behavior, root exports, installed metadata, and `py.typed`. Source constants and test constants are exactly equal. |
| Configured formatting/lint readiness | **Fail** | The tree contains 24 Python lines longer than the configured 88 columns, including package source and four examples, while CI runs `ruff format --check .` and `ruff check .`; see V03-F01. |
| Example CLI/schema/safety contract | Pass except findings | All five scripts expose the documented input option and `--output`, read the 14 existing synthetic CSVs with matching required headers, call the package palette API, save at 180 DPI, refuse exact input/output collisions, close successfully built figures in `finally`, and visibly label outputs synthetic. Two approved semantic color mappings are wrong; see V03-F02. |
| README and API documentation | Pass statically with release gates | The README documents every public export, discrete/continuous/reverse/discovery/registration behavior, accessibility limits, provenance, and all five scripts. Its 19 local targets exist. It explicitly labels the absent example PNGs and unresolved `<owner>` URL as human gates. |
| Gallery structure and value parity | Pass statically | The SVG parses as XML, has an accessible title/description and `viewBox="0 0 1200 1870"`, names all 22 canonical palettes, and contains 107 swatch-title hex values exactly matching source order. The README palette table also contains the same 107 values in the same case-sensitive order. Visual rendering remains human-only. |
| CI dependency graph and platform coverage | Pass statically with lock gate | CI covers CPython 3.10 through 3.14 on Ubuntu and boundary versions on macOS/Windows. Build needs quality and test. Release build needs verify; publish needs build and downloads the built artifact. All 19 `uses:` references are full 40-character lowercase SHAs. |
| Release permissions and secret handling | Pass statically with external gates | Workflow default is `contents: read`; publish job has only `id-token: write`, uses environment `pypi`, and contains no credential/secret reference. GitHub environment protection and PyPI Trusted Publisher configuration are explicitly human-only. |
| Reproducible dependency lock | Human gate, not fabricated | `uv.lock` is absent, as prior agents were prohibited from generating it. All five workflow sync steps require `uv sync --locked`, so CI/release cannot pass until the human generates, reviews, checks, and commits the lock. |

## Findings ordered by severity

### Moderate V03-F01: the repository is statically inconsistent with its Ruff quality gate

`pyproject.toml:64` configures `line-length = 88`, and both workflows execute `ruff format --check .` followed by `ruff check .`. A PowerShell scan found 24 Python lines longer than 88 columns: one in `src/wesandersonpy/palettes.py`, thirteen in `examples/diagram_sequence_time_domain.py`, one in `examples/fidelity_multi_parameter.py`, seven in `examples/readout_calibration_rabi_subplots.py`, and two in `examples/scatter_with_simulation.py`. The affected lines include reflowable function definitions, calls, comprehensions, and exception construction, not only unavoidable URLs or identifiers.

This is a confirmed configuration/source mismatch and makes a clean human quality run implausible without a formatting revision. Because executable Ruff confirmation is prohibited, the exact formatter/linter output remains unobserved; the source-width violation itself is confirmed.

Reproduction: use a PowerShell line counter over `Get-ChildItem src,tests,examples -Recurse -Filter *.py` and report lines whose `.Length -gt 88`. Representative locations are `src/wesandersonpy/palettes.py:125`, `examples/diagram_sequence_time_domain.py:55`, `examples/readout_calibration_rabi_subplots.py:181`, and `examples/scatter_with_simulation.py:64`.

Required correction: manually reflow the 24 lines without running Python, or have the human run Ruff formatting and return its diff for reviewed application. Then repeat the same static width scan before T08.

### Moderate V03-F02: two example scripts violate approved semantic color roles

The scatter fixture contract says simulation is orange, experiment is a dark diamond layer, and `highlight_simulation` is a solid red line (`examples/data/scatter_simulation/README.md:15`). The implementation maps `FantasticFox1` indices 3, 0, and 1 respectively (`examples/scatter_with_simulation.py:181-183`). Those exact package colors are `#E58601` (orange), `#DD8D29` (another orange), and `#E2D200` (yellow). Thus the experiment and simulation layers have poor categorical separation and the specifically required red highlight is yellow, despite `FantasticFox1` containing red `#B40F20` at index 4.

The readout/Rabi fixture contract says the state-zero `ink` role is black (`examples/data/readout_calibration_rabi/README.md:54`). The implementation sets both `ink` and `neutral` from `wes.get_palette("Moonrise1")[0]` (`examples/readout_calibration_rabi_subplots.py:361-364`), which is pale yellow `#F3DF6C`, rather than the near-black `#24281A` available at the last index. This affects state-zero traces, neutral IQ background points, tone guides, and annotations on Matplotlib's default light background.

These are confirmed source/data-contract defects, not subjective render-only hypotheses. Required correction: choose package-derived indices that implement the documented roles, preserving the no-hard-coded-hex rule. A reasonable static target is `FantasticFox1` orange/blue-or-dark/red for simulation/experiment/highlight and `Moonrise1[-1]` for `ink`/`neutral`; final visual suitability remains for the human render review.

### Moderate V03-F03: default generated PNGs bypass the ignored generated-output path

`.gitignore:43-44` says generated outputs belong under the ignored `examples/figures/generated/`, with only human-approved exhibits living directly under `examples/figures/`. All five scripts instead default directly to unignored paths such as `examples/figures/scatter_with_simulation.png` (`examples/scatter_with_simulation.py:27`), and both READMEs instruct the human to use those paths before approval. The output files therefore become ordinary untracked commit candidates immediately after rendering, contrary to the plan's generated-output hygiene and the documentation's approval gate.

No unapproved PNG currently exists, so this finding concerns the implemented workflow rather than an existing leaked artifact. Required correction: default and documented first-pass renders to `examples/figures/generated/*.png`, then document moving/copying only human-approved nonconfidential exhibits to the committed figure paths. Alternatively, add precise ignore/negation rules for named approved assets after those assets exist.

## Low-severity documentation issue

`CHANGELOG.md:10` says the typed palette and Matplotlib APIs are "planned" even though they are already present in the unreleased tree. Update this line when making the scoped correction so the changelog describes implemented unreleased functionality accurately. This does not independently block T08.

## Confirmed passes and negative checks

- Package source, test oracle, README table, and SVG swatch titles contain 22 names/107 colors with exact ordered parity.
- `Rushmore` is absent from canonical discovery and maps to `Rushmore1`; `Zissou1Continuous` is not a public movie palette.
- The current API exposes no mutable color list or writable public palette mapping.
- No top-level call registers Matplotlib colormaps.
- All 14 synthetic fixture CSVs have headers matching their consuming scripts; PowerShell parsing produced the previously verified total of 904 rows.
- Every example has a synthetic disclaimer in its module text and a visible synthetic footer in its figure construction.
- No example contains a hard-coded hexadecimal palette literal.
- All README local links exist; no reference PNG is embedded or linked.
- The UTF-8 smart punctuation seen as mojibake in some sandbox console output is not file corruption: direct UTF-8 code-point inspection found the intended Unicode quotation marks/bullet.
- `plotting_example/` and `reference/wesanderson-r/` are ignored; `uv.lock` is not ignored and will be a commit candidate when generated.
- All 19 workflow action references use immutable full SHAs; build/publish transfer is one-way and the publish job does not rebuild.

## Human-run unknowns and release gates

The following are not defects established by this static review, but none may be claimed as passed until the human returns evidence:

1. Generate `uv.lock`, review it, run `uv lock --check`, and synchronize with `uv sync --locked --extra dev --extra examples`. Until then, both workflows are guaranteed to stop at their locked-sync steps.
2. Run Ruff formatting/linting and mypy after V03-F01 is corrected.
3. Run pytest with branch coverage. Static review cannot establish Matplotlib warning text, registry teardown behavior, subprocess import isolation, installed metadata, or test pass counts.
4. Build the wheel and source distribution, run Twine, inspect archive contents, and install both artifacts in clean isolated environments.
5. Render all five examples after V03-F02/F03 are corrected, inspect layout/contrast/labels/footers, and approve only nonconfidential synthetic PNGs.
6. Rasterize or browser-preview the SVG and render the built long description on both GitHub and PyPI. Relative asset/document links cannot be made final for PyPI until a canonical repository URL exists.
7. Supply the GitHub owner/repository URL, replace the explicitly non-working `<owner>` installation example, add final project URLs to metadata if desired, and recheck distribution-name availability.
8. Create commits and the remote repository; configure branch protection, the protected `pypi` environment, and PyPI Trusted Publishing; then let CI pass before creating a release. No external action is authorized for agents.
9. Confirm that no confidential or experimental data, restricted reference image, credential, or sensitive image metadata enters version control or returned logs.

## Required next action

Assign scoped implementation follow-ups for V03-F01 through V03-F03 and the changelog wording, preserving this report unchanged. Request a new numbered static verification report after those edits. If that report passes, the human can begin T08 with lock generation and the complete runtime/build/render matrix.
