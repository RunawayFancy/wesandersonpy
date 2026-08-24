# V07: Build and package validation

## Verification identity and verdict

- Task: T18, build and package validation.
- Context: `context/conversation-v006.md` and `tasks/T18-package-validation.md`.
- Validation date: 2026-08-23.
- Overall verdict: **FAIL; package validation is blocked by a missing build backend in `wespy`.**

The active environment satisfies the interpreter-location gate, but `python -m build --no-isolation` cannot import `hatchling.build`. No source distribution or wheel was created, so Twine validation, archive-content inspection, isolated wheel installation, and the installed-wheel public-API smoke test could not complete. No fix, dependency installation, publication, upload, or external network access was attempted.

## Inputs inspected

- `context/conversation-v006.md`
- `tasks/T18-package-validation.md`
- `pyproject.toml`
- `.gitignore`
- Packaging, installation, development, and example sections of `README.md`
- Development setup, quality checks, and release sections of `CONTRIBUTING.md`

No experimental data or restricted plotting reference was read.

## Environment evidence

The Conda PowerShell hook was loaded from `E:\conda\shell\condabin\conda-hook.ps1`, followed by `conda activate wespy` for every Python command.

Observed environment:

- `CONDA_PREFIX=E:\conda\envs\wespy`
- `Python 3.12.12`
- `build 1.5.0` from `E:\conda\envs\wespy\Lib\site-packages\build`
- `twine 7.0.0`
- `python -m pip check`: `No broken requirements found.`
- `python -m pip show hatchling`: warning that the package was not found.

`dist/` was absent before the build attempt.

## Commands and outcomes

### Environment and tool check

```powershell
& 'E:\conda\shell\condabin\conda-hook.ps1'
conda activate wespy
Write-Output "CONDA_PREFIX=$env:CONDA_PREFIX"
python --version
python -m build --version
python -m twine --version
```

Result: pass. The interpreter resolved inside the required `wespy` environment and the build/Twine front ends were importable.

### Offline build

```powershell
& 'E:\conda\shell\condabin\conda-hook.ps1'
conda activate wespy
python -m build --no-isolation
```

Result: fail with exit code 1 while obtaining build dependencies for the source distribution.

Observed exception:

```text
pyproject_hooks._impl.BackendUnavailable: Cannot import 'hatchling.build'
ERROR Backend 'hatchling.build' is not available.
```

The `--no-isolation` option was used to honor the task's offline preference and prohibition on contacting PyPI. A standard isolated build was not retried because resolving the absent backend could contact an external package index. The failure is consistent with `python -m pip show hatchling`, which reported that Hatchling is not installed in `wespy`.

### Twine metadata validation

```powershell
& 'E:\conda\shell\condabin\conda-hook.ps1'
conda activate wespy
python -m twine check dist/*
```

Result: fail with exit code 1 because the build produced no files.

```text
ERROR InvalidDistribution: Cannot find file (or expand pattern): 'dist/*'
```

### Archive inventory and downstream gates

A read-only PowerShell inventory found `archive_count=0`. Therefore:

- Source-distribution content inspection: blocked because no source archive exists.
- Wheel content inspection: blocked because no wheel exists.
- Isolated wheel installation: blocked because no wheel exists.
- Import-path and public-API smoke test: blocked because no wheel could be installed.

## Acceptance-criteria matrix

| Criterion | Result | Evidence |
|---|---|---|
| Active interpreter is inside `E:\conda\envs\wespy` | Pass | `CONDA_PREFIX` and module paths resolve inside that environment. |
| Build source distribution and wheel | Fail | Hatchling backend unavailable; exit code 1. |
| Run Twine metadata validation | Fail downstream | No `dist/*` file exists. |
| Inspect intended and excluded archive contents | Blocked | Archive count is zero. |
| Install wheel into an isolated temporary environment | Blocked | No wheel exists. |
| Import from installed wheel rather than source tree | Blocked | No isolated wheel installation was possible. |
| Exercise the installed public API | Blocked | No isolated wheel installation was possible. |

## Generated artifacts and repository changes

- Build artifacts: none.
- `dist/`: absent after the failed build.
- Temporary isolated smoke-test environment: not created because no wheel existed.
- Implementation or metadata changes: none.
- Durable output created by this verifier: `verification/V07-package-validation.md` only.

## Finding

### V07-F01: required Hatchling build backend is unavailable in `wespy`

`pyproject.toml` declares `hatchling>=1.26` as its build-system requirement, but the active environment cannot import `hatchling.build`, and `pip show hatchling` finds no installed Hatchling distribution. `pip check` still passes because build-system requirements are not installed-project runtime dependencies. This is an environment-preparation failure; this verification run does not establish a defect in package source or metadata.

Reproduction:

```powershell
& 'E:\conda\shell\condabin\conda-hook.ps1'
conda activate wespy
python -m pip show hatchling
python -m build --no-isolation
```

## Required next action

The human maintainer should install or otherwise make the declared `hatchling>=1.26` backend available in `wespy` using an approved dependency-management path. After confirming `python -m pip show hatchling`, rerun T18 from the build step and create a new numbered verification report that includes Twine, archive-content, isolated wheel-installation, import-origin, version, palette, and colormap smoke-test evidence. Do not treat this V07 result as package-validation success.
