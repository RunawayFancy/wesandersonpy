# V09: Static-quality failure diagnosis

## Verification identity and verdict

- Task: T20, diagnosis of the V06 static-quality failures.
- Context: `context/conversation-v006.md` and immutable `verification/V06-static-quality.md`.
- Execution date: 2026-08-23.
- Environment: Conda environment `wespy`, `CONDA_PREFIX=E:\conda\envs\wespy`, interpreter `E:\conda\envs\wespy\python.exe`, Python 3.12.12.
- Diagnostic verdict: **the Ruff failures are five exact extra-blank-line import-block findings plus layout-only formatter drift in six files. The configured Python 3.10 mypy run remains blocked in NumPy 2.5.2's stub, while an explicit Python 3.12 mypy target successfully checks all three package source files with no issues.**

No fix mode, format-write mode, package installation, network operation, or implementation/configuration edit was performed. This report is the only durable project file written by T20.

## Exact commands

Every command was run from `E:\PhD_file\wesandersonpy` after loading Conda's PowerShell hook and activating `wespy`.

```powershell
python -m ruff check .
python -m ruff format --diff .
python -m ruff check --diff .
python -m mypy --no-incremental src/wesandersonpy
python -m mypy --no-incremental --python-version 3.12 src/wesandersonpy
```

The two Ruff `--diff` commands only displayed proposed changes. They did not apply them. `--no-incremental` kept the mypy comparison independent of incremental cache state while preserving the checked-in mypy configuration except for the explicitly overridden Python target in the second run.

## Ruff lint diagnosis

`python -m ruff check .` exited 1 with exactly five findings. Every finding is rule `I001`, "Import block is un-sorted or un-formatted," and Ruff marks all five as fixable.

| File and location | Rule | Exact proposed change from `ruff check --diff` |
|---|---|---|
| `src/wesandersonpy/_palette_data.py:3:1` | `I001` | Remove the second blank line between `from types import MappingProxyType` and the following palette-data comment. |
| `src/wesandersonpy/palettes.py:3:1` | `I001` | Remove the second blank line between the relative `_palette_data` import and `PaletteKind`. |
| `tests/test_palette_data.py:3:1` | `I001` | Remove the second blank line between `import wesandersonpy as wes` and `EXPECTED_PALETTES`. |
| `tests/test_palettes.py:3:1` | `I001` | Remove the second blank line between `import wesandersonpy as wes` and `ZISSOU_CONTINUOUS_SEED`. |
| `tests/test_public_api.py:3:1` | `I001` | Remove the second blank line between the two `wesandersonpy` imports and `EXPECTED_EXPORTS`. |

Ruff does not propose reordering or changing any import name in these five diffs. The entire lint correction is the removal of one surplus blank line in each file. Ruff's summary was `Found 5 errors` and `5 fixable with the --fix option`.

## Ruff formatter diagnosis

`python -m ruff format --diff .` exited 1 and reported six files that would be reformatted, with 70 files already formatted. Its complete semantic summary is below; every proposed hunk changes layout only.

### `examples/diagram_sequence_time_domain.py`

- Reformat the `time_domain_response.csv` `load_rows` call so the filename and required-column set occupy separate lines and the set line has a trailing comma.
- Apply the same multiline layout to the `population_sweeps.csv` `load_rows` call.

### `examples/fidelity_multi_parameter.py`

- Compact the parenthesized three-line `DEFAULT_OUTPUT` assignment to one 85-character path-expression line.

### `examples/multiple_iterations_faded.py`

- Compact the parenthesized three-line `DEFAULT_OUTPUT` assignment to one line.

### `examples/readout_calibration_rabi_subplots.py`

- Compact the four-line path division inside the parenthesized `DEFAULT_OUTPUT` assignment to one expression line inside the parentheses.
- Compact the two-line `x_values` list-comprehension body to one comprehension line.
- Compact the three-line `dict.fromkeys` generator body used for IQ cluster states to one generator line inside the call.

### `examples/scatter_with_simulation.py`

- Compact the parenthesized three-line `DEFAULT_OUTPUT` assignment to one line.
- Compact the three-line highlighted-simulation list-comprehension body to one comprehension line inside the brackets.

### `tests/test_matplotlib.py`

- Compact the two-line generator expression inside the `all(isinstance(...))` assertion to one generator line inside the call.

No formatter diff changes a literal, identifier, operator, call target, collection member, branch, or expected result. This establishes that V06-F01 is formatter drift rather than a behavioral defect, but the checked-in tree still fails the configured formatting gate until a separate authorized task applies and reviews the exact diff.

## Mypy target comparison

### Configured Python 3.10 target

Command:

```powershell
python -m mypy --no-incremental src/wesandersonpy
```

Exit code: 2.

```text
E:\conda\envs\wespy\Lib\site-packages\numpy\__init__.pyi:737: error: Type statement is only supported in Python 3.12 and greater  [syntax]
Found 1 error in 1 file (errors prevented further checking)
```

`pyproject.toml` supplies `python_version = "3.10"`. Mypy 2.3.1 therefore parses installed dependency stubs as Python 3.10 syntax even though the active interpreter is Python 3.12.12. Installed NumPy 2.5.2 contains a type statement requiring Python 3.12 in `numpy/__init__.pyi`. The dependency-stub syntax error stops analysis before mypy can establish a result for `src/wesandersonpy`.

### Explicit Python 3.12 diagnostic target

Command:

```powershell
python -m mypy --no-incremental --python-version 3.12 src/wesandersonpy
```

Exit code: 0.

```text
Success: no issues found in 3 source files
```

This confirms that the package's current annotations pass strict mypy when the analysis target matches the active Python 3.12 environment and its NumPy stub syntax. It does **not** prove Python 3.10 typing compatibility, because that target was explicitly bypassed for the diagnostic comparison. V06-F03 therefore remains a configuration/dependency-environment compatibility failure, not a confirmed package annotation defect and not a Python 3.10 typing pass.

## Diagnosis and possible fixes

### Ruff

The smallest correction is to apply the five one-line import-block blank-line removals and the exact six-file formatter diff, then rerun both Ruff commands without fix flags. Applying `ruff check --fix` and `ruff format` is also mechanically possible, but only in a separately authorized implementation task with a reviewed diff. No Ruff suppression or rule/configuration weakening is justified by the observed findings.

### Mypy

Possible approaches, requiring maintainer choice and separate implementation authorization, are:

1. Run the strict Python 3.10 mypy gate in a genuine Python 3.10 environment whose resolved Matplotlib/NumPy dependency set supports Python 3.10. This most directly validates the declared minimum version and avoids asking a newer interpreter's dependency stubs to parse as an older target.
2. Constrain the development/typing dependency resolution to NumPy and Matplotlib versions whose stubs remain parseable for the Python 3.10 mypy target, then verify that the constraint is compatible with every supported runtime and CI environment. A pin should not be guessed; it needs resolver and mypy evidence.
3. Move the configured mypy target to Python 3.12 only if the project intentionally stops claiming type-check coverage for Python 3.10/3.11. Runtime support could remain broader, but the reduced static-analysis guarantee must be documented explicitly. The successful diagnostic command alone is not sufficient justification for silently changing the target.
4. Split CI responsibilities: preserve runtime tests across Python 3.10-3.14 and add a dedicated Python 3.10 typing environment with compatible dependencies, while optionally retaining a current-Python typing job. This gives direct minimum-version evidence and current-stub coverage.

Ignoring site-package errors or disabling strict import following may bypass the symptom but would reduce useful Matplotlib-facing type coverage; it should not be the default response without evidence.

## Final decision

T20 acceptance criteria are satisfied. V06-F01 and V06-F02 have exact, mechanical Ruff diagnoses and remain unfixed. V06-F03 is isolated to the configured Python 3.10 target parsing the installed NumPy 2.5.2 stub; package source passes strict mypy under the explicit Python 3.12 diagnostic target. The host should assign a separate correction task, preserve V06 and V09 unchanged, and require a new verification report after corrections.
