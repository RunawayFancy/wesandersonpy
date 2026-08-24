# Conversation context v001

## Objective

Plan a conversion of the local `wesanderson` R palette project into a publishable Python package with Matplotlib integration, individual manufacturing plot examples, and a complete gallery-oriented README. The user explicitly requested planning first and prohibited implementation until human confirmation.

## Authorization

The user authorized loading `AGENT.md`, inspecting non-experimental project code and structure, researching current technical references, and writing the plan under `docs/`. The user has not yet authorized package implementation, Git initialization, dependency installation, Python execution, repository publishing, or external account changes.

## Restrictions

- Never read or write experimental data.
- Never fabricate experimental results.
- Do not run Python files; provide detailed commands for the human to run and request the relevant outputs.
- Remain inside the current project and permitted global instruction locations.
- Preserve provenance and avoid plagiarism.
- Do not make implementation changes before plan approval.

## Evidence state on 2026-08-23

- `examples/` contains no files. A final metadata-only check found `plotting_example/Fidelity_plots_with_multi_params.png` and `plotting_example/Multiple_subplots_readout_calibration_rabi_data.png`; the image contents were not opened or inspected because they may contain restricted experimental information.
- `scr/wesandersonpy/` is empty.
- The root `README.md` is empty.
- The root is not a Git repository.
- The R reference provides palette values, R API behavior, figures, MIT metadata, and upstream author information.
- The PyPI name `wesanderson` is occupied by an unrelated maintained distribution with latest indexed release 0.0.4 from 2025-06-06.
- Current PyPA guidance supports a `pyproject.toml`-based regular package and `src` layout; current Matplotlib documents listed and linearly segmented colormaps; current PyPI guidance supports GitHub OIDC Trusted Publishing.

## Proposed decisions

- Distribution and import name: `wesandersonpy`.
- Initial version: `0.1.0`.
- Layout: `src/wesandersonpy`.
- Build backend: Hatchling.
- Development lock: `uv.lock`; library runtime requirements remain ranged.
- Runtime dependency: Matplotlib only unless implementation proves another dependency essential.
- Python support: 3.10 and newer.
- Examples: one script per human-provided, nonconfidential plot-case specification; the human executes every script.

## Unresolved questions

- Human approval of package name, tool choices, and Python support floor.
- New author, maintainer, repository, email, and copyright metadata.
- Whether the unchanged R reference should be moved to `reference/wesanderson-r/` or retained in place.
- Nonconfidential layout and schema specifications for the two filename-identified plotting cases.

## Next action

Wait for the human to review `plan.md`. Do not implement until the human explicitly approves it.
