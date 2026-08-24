# V04: Complete static implementation reverification

## Verification identity and verdict

- Task: T15, independent reverification of V03 corrections and regression scope.
- Inspection date: 2026-08-23.
- Inputs: `context/conversation-v004.md`, immutable `verification/V03-static-implementation.md`, T03 r03, T05 r02, T06 r02, T01 repository-metadata r02, and the complete current implementation.
- Method: read-only PowerShell source inspection, CSV parsing, XML parsing, regular-expression parity checks, path/ignore checks, and command-local Git inspection.
- Overall verdict: **PASS for static implementation.** V03-F01, V03-F02, V03-F03, and the changelog issue are resolved, and no regression was found in the previously passing static areas.
- T08 readiness: **ready for human execution of T08.** This is not a runtime, build, visual, privacy, remote, or publication pass; the human must now complete the outstanding gates listed below and return evidence.

No Python interpreter, Ruff, mypy, pytest, uv, build, Twine, example renderer, GitHub workflow, or publishing action was run. No implementation, prior report, plan, task, staging area, or commit was modified. This V04 report is the only file written by the verifier.

## Correction disposition

| V03 item | Result | Independent evidence |
|---|---|---|
| V03-F01: 88-column mismatch | Resolved | A PowerShell scan of all 12 Python files under `src/`, `tests/`, and `examples/` found zero lines longer than the configured 88 columns. The prior package-source and example locations are now reflowed. |
| V03-F02: scatter semantic colors | Resolved | `examples/scatter_with_simulation.py` maps `FantasticFox1[3]`, `[2]`, and `[4]` to simulation, experiment, and highlighted simulation. From the immutable package data these are orange `#E58601`, contrasting blue `#46ACC8`, and red `#B40F20`, matching the fixture contract. |
| V03-F02: readout ink/neutral | Resolved | `examples/readout_calibration_rabi_subplots.py` sets `ink = wes.get_palette("Moonrise1")[-1]` and derives `neutral` from it. The package value is near-black `#24281A`, matching the fixture contract. |
| V03-F02: package-only colors | Resolved | No `#[0-9A-Fa-f]{6}` literal occurs in any of the five example scripts. Corrected roles continue to use only the public package API. |
| V03-F03: ignored first-pass outputs | Resolved | All five script defaults resolve to `examples/figures/generated/<name>.png`. Both README command sets use those paths. `.gitignore` matches the staging directory, and zero PNG files currently exist below `examples/figures/`. |
| V03-F03: human promotion gate | Resolved | Both READMEs require human review for correctness, confidentiality, synthetic-only provenance, and sensitive metadata before copying or moving an approved PNG to the named committed path under `examples/figures/`. The root README distinguishes ignored first-pass paths from approved exhibit paths. |
| V03 changelog wording | Resolved | `CHANGELOG.md` has one `[Unreleased]` section, describes the typed palette and Matplotlib functionality as implemented, identifies 0.1.0 only as the target, and does not fabricate a release date, comparison link, URL, or identity. |

## Regression matrix

| Area | Result | Static evidence |
|---|---|---|
| Package data and test oracle | Pass | Package source still contains 22 canonical names and 107 hex values. Names and values exactly match `tests/test_palette_data.py` in case-sensitive order. |
| Alias, private seed, and immutability | Pass | `Rushmore` remains a read-only alias of `Rushmore1`; the special Zissou continuous data remain in private `CONTINUOUS_SEEDS`; `PALETTES`, aliases, and seeds use mapping proxies and tuple values. |
| Public API and Matplotlib behavior | Pass statically | The reflow in `palettes.py` preserves the invalid-prefix exception message and control flow. Public construction, validation, reversal, registration preflight, explicit registration, and no-import-registration structure remain present and aligned with the unchanged tests. |
| Test contract | Pass statically | Four test modules remain present and continue to cover exact data/order, immutability, alias/seed behavior, validation, interpolation, Matplotlib types and registration, import side effects, public exports, metadata, and `py.typed`. Execution remains human-only. |
| Example inventory and schemas | Pass | Exactly five scripts remain. All 14 CSVs parse with PowerShell, contain 904 rows total, and retain every column required by their consuming script. Input/output collision guards, 180-DPI saves, `finally` closing, and synthetic labels remain present. |
| README links and gallery | Pass | All 19 local root-README targets exist. The README table and SVG each retain all 107 source colors in exact case-sensitive order. The SVG parses as XML and retains all 22 canonical palette names. No unapproved PNG is embedded. |
| Metadata, license, and attribution | Pass | Version 0.1.0 remains consistent in project metadata, package export, CFF, README, and SVG. Python `>=3.10`, Matplotlib `>=3.8,<4`, MIT license metadata, non-personal contributor fallback, and upstream attribution remain intact. No personal or remote metadata was invented. |
| Ignore behavior | Pass | The restricted plot-reference directory, ignored upstream checkout, credentials, caches, and generated staging directory remain ignored. `uv.lock` is not ignored and will be reviewable when the human generates it. |
| CI support and graph | Pass statically | CI still covers CPython 3.10 through 3.14 on Ubuntu and boundary versions on macOS and Windows. CI build depends on quality/test; release build depends on verification; publish depends on build and downloads rather than rebuilds the artifact. |
| Workflow supply-chain and permissions | Pass statically | All 19 `uses:` references remain full 40-character lowercase SHA pins. Default permission is `contents: read`; the `pypi` publish job has only `id-token: write`, uses the `pypi` environment, and contains no secret, password, token, or username reference. |

## Findings

No confirmed blocking, moderate, or low-severity implementation defect was found in the T15 scope.

## Human-run unknowns and mandatory T08 gates

Static readiness does not establish executable correctness. The human should now perform T08 in this order, stop at the first failure, and return complete outputs without weakening checks:

1. Generate and review `uv.lock`, run `uv lock --check`, then synchronize the locked development and example environment. `uv.lock` is currently absent, so CI and release locked-sync steps cannot yet pass.
2. Run `ruff format --check .`, `ruff check .`, and strict mypy. The width scan passes, but formatter, lint-rule, import-order, and type-checker behavior remain unexecuted.
3. Run pytest with branch coverage and return the collected/pass count, warnings, and coverage table.
4. Build the wheel and source distribution, run Twine, inspect both archive manifests, and perform isolated clean installs from each artifact.
5. Render all five examples only to `examples/figures/generated/`; return console output plus Python, Matplotlib, and installed `wesandersonpy` versions. Inspect layout, contrast, labels, clipping, synthetic footer, confidentiality, and image metadata before promoting any exhibit.
6. Browser-preview the SVG and render the built long description on GitHub and PyPI. Relative PyPI asset/document links and the explicit `<owner>` installation placeholder remain release gates until the canonical repository URL is supplied.
7. Confirm no confidential or experimental data, restricted reference image, credential, unapproved PNG, or sensitive image metadata has entered candidate version-control content or returned logs.
8. Only after local evidence passes, create reviewed commits and the remote repository, configure branch protection, the protected `pypi` environment, and PyPI Trusted Publishing, and allow CI to pass. Agents remain unauthorized to perform these external actions.

## Final decision

The scoped V03 corrections are complete and the repository is **ready to enter T08 human verification**. Publication readiness remains pending the full human evidence matrix, canonical repository metadata, CI success, protected-environment configuration, and explicit release approval.
