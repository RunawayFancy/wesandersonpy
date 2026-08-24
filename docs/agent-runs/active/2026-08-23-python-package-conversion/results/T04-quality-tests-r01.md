# T04 quality and tests result r01

## Task and context

- Task: T04, quality, tests, dependencies, and build preparation.
- Context used: `context/conversation-v004.md`, the approved `plan.md`, `tasks/T04-quality-tests-and-build.md`, the T01 through T03 result reports, `pyproject.toml`, and the complete current `src/wesandersonpy/` package.
- Status: Test implementation and static review complete. Human-run formatting, linting, typing, test, lock, build, metadata, and clean-install evidence remains required by project policy.

## Sources inspected

- `AGENT.md` for permissions, experimental-data restrictions, Python-execution restrictions, and result-record requirements.
- `pyproject.toml` for Python support, runtime and development dependency separation, build configuration, and Ruff, mypy, pytest, and coverage configuration.
- `src/wesandersonpy/_palette_data.py`, `src/wesandersonpy/palettes.py`, and `src/wesandersonpy/__init__.py` for the implemented public contract and every validation branch.
- T01 repository/metadata, T02 palette API, and T03 Matplotlib integration reports for intended behavior and known unexecuted areas.
- The exact canonical palette constants already ported from the non-experimental upstream R reference and verified by T02. No plotting image, experimental data, manufacturing data, or synthetic example fixture was read or used in this task.

## Work performed

- Added an exact public-data parity suite for all 22 canonical palettes, all 107 hexadecimal values in source order, stable discovery order, exclusion of the alias/private seed from canonical discovery, and immutable mapping and tuple behavior.
- Added palette API tests for discrete selection, reverse-before-selection behavior, the `Rushmore` alias, the dedicated 11-color `Zissou1` continuous seed, interpolation counts and endpoints, the one-color case, the discrete upper bound, actionable unknown-name errors, invalid types and values, and the `wes_palette` compatibility alias.
- Added Matplotlib tests for continuous and discrete return classes, colormap names, LUT sizes, forward and reversed endpoints, Zissou endpoints, discrete truncation and repetition, alias equivalence, and all applicable input-validation paths.
- Added isolated registry tests using per-test prefixes and teardown. They verify no default registration at package import, normal explicit registration, atomic conflict detection before any write, and `force=True` replacement of an existing non-built-in colormap including Matplotlib's overwrite warning.
- Added public-surface tests for exact root and module exports, version `0.1.0`, installed distribution version/name/Python/runtime-dependency metadata, and inclusion of the `py.typed` marker in the importable package.
- Reviewed the existing `pyproject.toml` configuration statically. Runtime and development dependencies are separated, and the configured Hatchling, Ruff, mypy, pytest, and coverage sections support this task. No material metadata/configuration defect requiring a T01 edit was found.
- Did not create or fabricate `uv.lock`. Generating it invokes Python package tooling and is therefore reserved for the human under the approved execution restrictions.

## Files changed

- `tests/test_palette_data.py`
- `tests/test_palettes.py`
- `tests/test_matplotlib.py`
- `tests/test_public_api.py`
- `docs/agent-runs/active/2026-08-23-python-package-conversion/results/T04-quality-tests-r01.md`

## Static evidence

- Four test modules contain 45 test functions and 79 expected pytest cases after parameter expansion.
- A PowerShell-only literal comparison found 107 canonical hexadecimal values in `_palette_data.py` and 107 in the test oracle; their case-sensitive sequences are identical.
- A PowerShell line-length scan found zero test lines longer than the configured 88 characters.
- A static content scan found no references from the tests to `plotting_example`, `examples/data`, experimental data, or measurement data.
- Static branch reconciliation confirmed that every asserted name, kind, count, reverse, prefix, and force validation path exists in the current implementation.
- `uv.lock` and `dist/` are absent, as expected before human lock generation and package builds.
- No Python interpreter, pytest, Ruff, mypy, uv Python workflow, Hatchling, build, Twine, or example script was run by this agent.

## Exact human-run verification commands

Run the following from the repository root in PowerShell. Stop at the first failure and return the complete command output rather than changing the implementation or expected results locally.

### 1. Generate and synchronize the reproducible environment

```powershell
uv lock
uv lock --check
uv sync --locked --extra dev --extra examples
```

Expected evidence: `uv.lock` is created from `pyproject.toml`, `uv lock --check` exits successfully without changing it, the project and all declared development/example dependencies install successfully, and the generated lock diff contains no unexpected project or source references.

### 2. Check formatting, linting, and typing

```powershell
uv run ruff format --check .
uv run ruff check .
uv run mypy src/wesandersonpy
```

Expected evidence: all three commands exit with status 0; Ruff reports no formatting or lint findings, and mypy reports success with no issues in the package source files.

### 3. Run tests with branch coverage

```powershell
uv run pytest --cov=wesandersonpy --cov-branch --cov-report=term-missing --cov-report=xml
```

Expected evidence: pytest collects 79 cases, all cases pass, and the terminal output contains a branch-coverage table plus a generated `coverage.xml`. The registry force test should consume the expected Matplotlib overwrite warning rather than emit an unhandled warning. Return the complete pass summary and coverage table.

### 4. Build and check both distributions

Ensure `dist/` does not contain artifacts from a different version before running these commands.

```powershell
uv run python -m build
uv run twine check dist/*
uv run python -m zipfile -l dist/wesandersonpy-0.1.0-py3-none-any.whl
tar -tf dist/wesandersonpy-0.1.0.tar.gz
```

Expected evidence: build creates one wheel and one source archive for version `0.1.0`; Twine reports both archives as `PASSED`; the wheel contains only the import package and distribution metadata, including `wesandersonpy/py.typed`; and neither archive contains `docs/agent-runs`, `plotting_example`, `reference`, credentials, caches, or generated temporary figures.

### 5. Verify a clean wheel installation outside the working-tree import path

```powershell
uv venv --python 3.10 build/clean-wheel-env
$wheel = (Resolve-Path dist/wesandersonpy-0.1.0-py3-none-any.whl).Path
uv pip install --python build/clean-wheel-env/Scripts/python.exe $wheel
& ./build/clean-wheel-env/Scripts/python.exe -I -c "import importlib.metadata as m; import wesandersonpy as w; print(w.__version__, len(w.available_palettes()), m.version('wesandersonpy'), w.__file__)"
```

Expected evidence: the final line begins with `0.1.0 22 0.1.0`, and `w.__file__` resolves inside `build/clean-wheel-env` rather than the repository's `src/` directory. This proves the built wheel is independently importable.

### 6. Verify a clean source-distribution installation

```powershell
uv venv --python 3.10 build/clean-sdist-env
$sdist = (Resolve-Path dist/wesandersonpy-0.1.0.tar.gz).Path
uv pip install --python build/clean-sdist-env/Scripts/python.exe $sdist
& ./build/clean-sdist-env/Scripts/python.exe -I -c "import importlib.metadata as m; import wesandersonpy as w; print(w.__version__, len(w.available_palettes()), m.version('wesandersonpy'), w.__file__)"
```

Expected evidence: the source distribution builds and installs successfully; the final line again begins with `0.1.0 22 0.1.0`, and the loaded module path is inside `build/clean-sdist-env`.

## Limitations and unresolved evidence

- Runtime behavior is not claimed as verified. The suite was designed by static inspection only and must be executed by the human.
- The exact intermediate RGB values produced by Matplotlib remain implementation-dependent within the supported Matplotlib range; tests intentionally assert stable counts, source seed parity, endpoints, and types rather than fabricate byte-for-byte parity with R interpolation internals.
- `uv.lock` cannot be reviewed until the human generates it. The host should treat a generated lock as unverified until `uv lock --check` and the synchronized checks pass.
- Build archive contents, Core Metadata rendering, Twine validation, and isolation from working-tree imports remain unverified until the human returns the requested evidence.
- The two clean-check virtual environments are disposable human verification environments under the ignored `build/` directory and should not be committed.

## Recommended next action

Have the host integrate T04 with T05 through T07, then give the human the commands above as part of the consolidated T08 verification matrix. If any command fails, preserve its complete output and request a scoped correction before rerunning only the affected stage and its downstream checks.
