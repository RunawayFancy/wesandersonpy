# Python package conversion plan

## Status

Approved for full implementation by the human on 2026-08-23. Static implementation and independent reverification are complete. T08 human execution remains pending; Python execution and remote GitHub/PyPI actions remain human-controlled.

## Objective

Convert the local R `wesanderson` palette source into a friendly, typed Python package with first-class Matplotlib support; prepare the repository for GitHub, reproducible development, versioning, testing, building, and PyPI publication; recreate each approved manufacturing plotting case as an individual script; and finish the root `README.md` with installation guidance, API documentation, a complete palette gallery, Matplotlib examples, and human-generated plot exhibits.

## Current repository evidence

- The repository root is not currently a Git repository.
- The root `README.md` is empty.
- `examples/` contained no files at the initial inventory. The human subsequently added five PNG references to `plotting_example/` and explicitly authorized their inspection for layout characterization and synthetic demonstration-data design.
- `scr/wesandersonpy/` exists but is empty. The conventional directory name is `src`, so the plan replaces the empty `scr` skeleton with `src/wesandersonpy/` after approval.
- The local R reference contains 24 public palette names in its README, the additional `Rushmore` alias, and the special `Zissou1Continuous` color sequence in the R source.
- The local R package declares MIT licensing and identifies Karthik Ram as copyright holder. A Python port must preserve provenance and the applicable MIT notice.
- The PyPI distribution name `wesanderson` is already occupied. The recommended distribution and import package name is therefore `wesandersonpy`, subject to a final availability check immediately before publication.

## Binding constraints

- Do not read, copy, transform, generate, or edit experimental data. This includes data that may later appear in `plotting_example/`.
- Do not fabricate experimental results or plot exhibits.
- The human user must run Python scripts and report the requested outputs. The agent may write code and test instructions after approval but will not execute Python files.
- Keep the original R source unchanged until the human approves how it should be retained or relocated.
- Do not initialize Git, create implementation files, install dependencies, run build tools, or configure external GitHub/PyPI state before this plan is approved.
- Cite upstream code, images, palette provenance, and technical documentation. Do not reuse an upstream image unless its license and attribution are suitable.
- Keep package runtime dependencies minimal and keep example/development dependencies separate.

## Recommended project decisions

### Name and version

- Use `wesandersonpy` for the PyPI distribution and import package: `import wesandersonpy as wes`.
- Start at version `0.1.0`, use semantic versioning, and keep one authoritative version value in package metadata.
- Recheck PyPI and GitHub name availability before creating remote publishing configuration because availability can change.

### Package API

The public API should be small and explicit:

```python
import wesandersonpy as wes

colors = wes.get_palette("Royal1")
colors_8 = wes.get_palette("Zissou1", n=8, kind="continuous")
cmap = wes.get_colormap("Zissou1", kind="continuous")
```

The proposed public surface is:

- `PALETTES`: a read-only mapping from canonical names to immutable tuples of hexadecimal colors.
- `available_palettes()`: return canonical public palette names in a stable order.
- `get_palette(name, n=None, *, kind="discrete", reverse=False)`: return colors and preserve the R behavior that discrete requests cannot exceed the source palette length.
- `get_colormap(name, *, kind="continuous", n=256, reverse=False)`: return a Matplotlib `ListedColormap` or interpolated `LinearSegmentedColormap` as appropriate.
- `register_colormaps(*, prefix="wesandersonpy", force=False)`: explicitly register names with Matplotlib without import-time global side effects.
- `wes_palette`: a documented compatibility alias for R users, delegating to `get_palette`.

Canonical palette names and hexadecimal values will match the local R source exactly. `Rushmore` will be documented as an alias of `Rushmore1`. `Zissou1Continuous` will remain an implementation seed rather than appearing as a separate movie palette in the main gallery. Invalid names, invalid `n`, and unsupported kinds will raise clear exceptions with available-name guidance.

### Layout

```text
wesandersonpy/
|-- .github/
|   |-- workflows/ci.yml
|   |-- workflows/publish.yml
|   `-- dependabot.yml
|-- docs/
|   `-- agent-runs/...
|-- examples/
|   |-- README.md
|   |-- <one-script-per-approved-plot-case>.py
|   `-- figures/
|-- src/
|   `-- wesandersonpy/
|       |-- __init__.py
|       |-- _palette_data.py
|       |-- palettes.py
|       `-- py.typed
|-- tests/
|   |-- test_palette_data.py
|   |-- test_palettes.py
|   |-- test_matplotlib.py
|   `-- test_public_api.py
|-- CHANGELOG.md
|-- CITATION.cff
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- NOTICE.md
|-- README.md
|-- SECURITY.md
|-- pyproject.toml
|-- uv.lock
|-- .editorconfig
|-- .gitattributes
|-- .gitignore
`-- .pre-commit-config.yaml
```

The existing R reference should either remain excluded from distribution or be moved intact to `reference/wesanderson-r/`. Moving it is recommended to prevent confusion with the Python import package, but this requires explicit human approval.

### Packaging and dependency control

- Use the standard `pyproject.toml` `[project]` table and a `src` layout.
- Use Hatchling as the small build backend recommended in the current PyPA packaging tutorial.
- Declare compatible runtime ranges rather than exact pins for library consumers. The initial runtime dependency should be Matplotlib only.
- Put test, lint, build, and example tools in dependency groups or extras. The expected development set is `pytest`, `pytest-cov`, `ruff`, `mypy`, `build`, and `twine`; example-only dependencies will be selected after the plot cases are known.
- Commit `uv.lock` for reproducible contributor and CI environments while leaving published runtime requirements appropriately ranged.
- Configure Ruff for formatting and linting, mypy for public API typing, pytest for behavior, and pre-commit for local checks.
- Build both wheel and source distribution and inspect their contents before release.

### Git and release preparation

- Initialize Git only after approval, rename the default branch to `main`, and make logically separated commits rather than one opaque initial commit.
- Add ignore rules for virtual environments, caches, build outputs, local data, generated temporary figures, and credentials. Approved README exhibit images will be explicitly committed.
- Add CI for lint, type checks, tests, and package builds across supported Python versions and operating systems.
- Use a tag/release-driven GitHub Actions publishing workflow with PyPI Trusted Publishing and a protected `pypi` environment. Do not store a long-lived PyPI token in the repository.
- Pin third-party GitHub Actions to full commit SHAs in the release workflow and document how to update those pins.
- Prepare metadata for authors, maintainers, license, keywords, classifiers, repository URL, issue tracker, changelog, citation, and security reporting. Human-supplied identity and repository values are required.
- Publishing itself remains a human-controlled operation: create the GitHub repository, configure the PyPI trusted publisher, approve the protected environment, create the release tag, and verify the final PyPI page.

## Manufacturing example policy and workflow

The five intended plot cases are a sequence/time-domain multi-parameter diagram, a multi-parameter fidelity plot, repeated iteration data with fading, readout-calibration/Rabi subplots, and scattered data with a highlighted simulation result. The human explicitly authorized the agents to inspect these images for layout characteristics. Agents must not extract or claim exact measurements from pixels; generated values must be independently synthetic, visibly labeled as such, and used only for demonstration.

For each intended plot, the human should provide a nonconfidential case specification containing only the plot type, required column names and units, categorical/continuous color mapping, desired palette, legend/colorbar behavior, output filename, and a reference image that the human is permitted to share. The specification must not contain measurements or experimental values.

After the image-characterization reports and synthetic schemas are reviewed, the initial scripts will be `examples/diagram_sequence_time_domain.py`, `examples/fidelity_multi_parameter.py`, `examples/multiple_iterations_faded.py`, `examples/readout_calibration_rabi_subplots.py`, and `examples/scatter_with_simulation.py`. Each script will use `wesandersonpy`, accept an input path and output path through command-line arguments, validate expected columns without rewriting the source data, create a deterministic Matplotlib figure, save it at a documented size and DPI, and close the figure. Shared presentation helpers may be imported from a small clearly documented example utility, but plot construction will remain visible in each individual script.

The agent will not run these scripts. The human will run each documented command on the authorized data and return the console output, package version, Python version, and generated image for review. Only human-approved, nonconfidential images will be added to `examples/figures/` and embedded in the README.

## README content plan

- Project purpose, provenance, attribution, and a concise warning that artistic palettes are not guaranteed to be perceptually uniform or color-vision-deficiency safe.
- Installation from PyPI and GitHub, plus an editable contributor installation.
- A minimal quick start using `get_palette` and `get_colormap` with Matplotlib.
- API guide covering discrete colors, continuous interpolation, reversed palettes, named palette discovery, explicit Matplotlib registration, and the R-compatible alias.
- A complete palette gallery generated from package values, grouped by film as in the R README, with palette names and hexadecimal values available as text.
- Manufacturing plot exhibits linked to their individual scripts, only after the human generates and approves them.
- Development, testing, citation, license, contribution, changelog, and publishing links.
- Reproducibility details that identify the script and package version used to render each committed image.

## Task graph

| ID | Task | Depends on | State |
|---|---|---|---|
| T01 | Establish repository, naming, licensing, metadata, and source disposition | Plan approval and human metadata | Completed: repository_metadata |
| T02 | Implement palette data and the typed core API | T01 | Completed: palette_api |
| T03 | Implement Matplotlib colormaps and explicit registration | T02 | Completed: palette_api r03 |
| T04 | Add tests, quality configuration, dependency lock, and build checks | T02, T03 | Completed: quality_tests |
| T05 | Implement one example script per approved manufacturing plot specification | Human case specifications, T03 | Completed: plot_examples r02 |
| T06 | Produce the palette gallery and complete the README | T03, T05 human-rendered exhibits | Completed statically: readme_gallery r02; human plot exhibits pending |
| T07 | Add GitHub CI, release automation, and publication documentation | T04, T06 | Completed: ci_release |
| T08 | Conduct human-run verification and prepare the release handoff | T04, T05, T06, T07 | Pending |
| T09 | Characterize sequence/time-domain and faded-iteration references; create synthetic data | Human authorization | Completed |
| T10 | Characterize fidelity and scatter/simulation references; create synthetic data | Human authorization | Completed (r02) |
| T11 | Characterize readout-calibration/Rabi reference; create synthetic data | Human authorization | Completed (r02) |
| T12 | Independently verify plot-characterization and synthetic-data artifacts | T09, T10, T11 | Completed: V01 found two moderate T11 defects |
| T13 | Reverify the revised readout-calibration/Rabi artifacts | T11 r02, T12 | Completed: V02 pass |
| T14 | Independently verify the complete static implementation | T01 through T07, V02 | Completed: V03 fail with three moderate corrections |
| T15 | Reverify the corrected complete static implementation | T03/T05/T06 revisions, V03 | Completed: V04 pass |

Task contracts are stored in `tasks/` beside this plan. No subagents are assigned.

## Acceptance criteria

- A clean environment can install the built wheel and source distribution and import `wesandersonpy` without importing files from the working tree accidentally.
- All documented public palette names return the exact source hexadecimal sequences, aliases behave as documented, and bad inputs fail clearly.
- Discrete and continuous outputs are valid Matplotlib colors; returned colormaps work anywhere Matplotlib accepts `cmap=`; explicit registration is repeatable and does not occur automatically at import.
- Public functions are typed and documented, and package data is immutable through the public API.
- The repository includes complete build metadata, license and upstream attribution, versioning guidance, dependency control, tests, contributor documentation, CI, and a secret-free trusted-publishing workflow.
- Every approved plotting case has an individual readable script that uses the installed package rather than copying palette values.
- The README renders correctly on GitHub and PyPI, shows the complete palette gallery and approved example plots, and links each exhibit to reproducible source code.
- The human-run verification matrix passes, and the human confirms that no confidential or experimental data entered version control, logs, fixtures, documentation, or committed image metadata.

## Human-run verification contract

After implementation, the agent will give the human exact commands for these checks and will not execute the Python files itself:

1. Create/synchronize the development environment from `pyproject.toml` and `uv.lock`.
2. Run Ruff formatting and lint checks.
3. Run mypy on `src/wesandersonpy`.
4. Run pytest with coverage.
5. Build the wheel and source distribution.
6. Run Twine metadata checks and inspect archive contents.
7. Install the wheel into a clean environment and run a short import/API smoke check.
8. Run each example script on human-authorized input and return the requested console output and images.
9. Render or preview `README.md` through the built package metadata and confirm its GitHub/PyPI links and images.

## Human decisions required before implementation

1. Approve `wesandersonpy` as both the distribution and import name, or specify a different unoccupied name.
2. Approve moving the unchanged R reference from `wesanderson/` to `reference/wesanderson-r/`, or instruct that it remain in place and be excluded from distributions.
3. Provide the package author/maintainer name, public email if any, GitHub account or organization, intended repository name/URL, and copyright holder for new Python code.
4. Review and approve the T09 through T11 image-characterization reports and synthetic schemas before the plotting scripts are implemented.
5. Confirm the recommended Python support floor of 3.10 and the use of Hatchling plus `uv.lock`.

## References checked 2026-08-23

- [Original `karthik/wesanderson` R repository](https://github.com/karthik/wesanderson), upstream palette source and provenance.
- [PyPI `wesanderson` project](https://pypi.org/project/wesanderson/), evidence that the distribution name is occupied; the indexed latest release is 0.0.4 dated 2025-06-06.
- [PyPA Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/), current `pyproject.toml`, regular-package, `src`, build, wheel, source distribution, license, and metadata guidance.
- [PyPA discussion of `src` versus flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/), last updated 2026-07-23 when checked.
- [Matplotlib 3.11.1 color API](https://matplotlib.org/stable/api/colors_api.html), definitions for `ListedColormap` and `LinearSegmentedColormap`.
- [Matplotlib 3.11.1 creating colormaps guide](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html), current creation, access, and resampling behavior.
- [PyPA GitHub Actions publishing guide](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/), current build-artifact and Trusted Publishing workflow guidance.
- [PyPI Trusted Publishers documentation](https://docs.pypi.org/trusted-publishers/using-a-publisher/), current OIDC publishing and permission requirements.
- [GitHub building and testing Python guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python), current CI matrix, Ruff, pytest, artifact, and PyPI workflow examples.

## Approval gate

The human approved implementation on 2026-08-23 and accepted the plan as the execution baseline. Personal author identity, public email, and final repository URL were not supplied; implementation must omit unknown factual metadata or use the non-personal label `wesandersonpy contributors`. Any material scope change will be recorded here before code changes proceed.
