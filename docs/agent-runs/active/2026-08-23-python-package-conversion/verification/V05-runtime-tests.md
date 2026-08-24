# V05: Runtime tests and branch coverage

## Verification identity and verdict

- Task: T16, runtime tests and coverage.
- Context: `context/conversation-v006.md` and `tasks/T16-runtime-tests.md`.
- Execution date: 2026-08-23.
- Verdict: **PASS with a confirmed non-failing deprecation warning.** The complete configured test suite passed with 100% statement and branch coverage. No test failed or was skipped. The warning should be addressed before the declared Matplotlib dependency range reaches a version that removes the deprecated argument.

No source, test, configuration, documentation, or metadata fix was applied. Generated pytest and coverage artifacts were authorized by T16. This report is the only durable project file written by the verifier.

## Environment

The Conda PowerShell hook was loaded and environment `wespy` was activated before execution.

- `CONDA_PREFIX`: `E:\conda\envs\wespy`
- Interpreter: `E:\conda\envs\wespy\python.exe`
- Python: 3.12.12, Anaconda build, 64-bit Windows
- Platform reported by pytest: `win32`
- `wesandersonpy`: 0.1.0
- Matplotlib: 3.11.1
- pytest: 9.1.1
- pytest-cov: 7.1.0
- pluggy reported by pytest: 1.6.0

The interpreter path and `CONDA_PREFIX` both satisfy the acceptance requirement that execution occur inside `E:\conda\envs\wespy`.

## Exact command

From `E:\PhD_file\wesandersonpy` in PowerShell:

```powershell
(& conda 'shell.powershell' 'hook') | Out-String | Invoke-Expression
conda activate wespy
Write-Output "CONDA_PREFIX=$env:CONDA_PREFIX"
python -c "import sys; print(sys.executable); print(sys.version)"
python -m pytest --cov=wesandersonpy --cov-branch --cov-report=term-missing
```

The command exited with status 0 in 3.9 seconds including environment reporting. Pytest itself reported 1.95 seconds.

## Test outcome

Pytest discovered the repository root and `pyproject.toml`, used `tests` as the configured test path, and collected 79 cases.

| Test module | Outcome |
|---|---:|
| `tests/test_matplotlib.py` | 39 passed |
| `tests/test_palette_data.py` | 5 passed |
| `tests/test_palettes.py` | 31 passed |
| `tests/test_public_api.py` | 4 passed |
| **Total** | **79 passed** |

- Failures: 0
- Errors: 0
- Skips: 0
- Xfails/xpasses: 0
- Warnings: 3

## Coverage outcome

```text
Name    Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------
TOTAL      93      0     38      0   100%

3 files skipped due to complete coverage.
```

Confirmed coverage result: 93 statements executed with zero misses; 38 branches executed with zero missing or partial branches; total coverage 100%.

## Confirmed warning

Three tests emitted the same `MatplotlibDeprecationWarning` from `src/wesandersonpy/palettes.py:101`:

- `test_discrete_colormap_has_expected_type_and_truncation`
- `test_discrete_colormap_repeats_colors_when_size_exceeds_source`
- `test_reversed_discrete_colormap_starts_from_last_source_color`

Matplotlib 3.11.1 reports that passing `N` to `ListedColormap` has been deprecated since Matplotlib 3.11 and is scheduled for removal in 3.13. The warning does not affect the current pass result: all discrete-colormap assertions succeeded. It is nevertheless a confirmed forward-compatibility risk because `pyproject.toml` currently permits Matplotlib versions from 3.8 up to, but excluding, 4.

This report does not claim that failure under Matplotlib 3.13 is already demonstrated; that future failure mode is a risk inferred from Matplotlib's runtime deprecation message. No fix was attempted under the verifier's read-only contract.

## Final decision

T16 acceptance criteria are satisfied. Runtime tests and branch coverage **pass** in `wespy`. The host should preserve the warning as a scoped follow-up item, without changing the successful test evidence, and continue with the separately assigned lint/type/build/package verification tasks.
