# T18: Build and package validation

## Context

Read `context/conversation-v006.md`, `pyproject.toml`, `.gitignore`, and the packaging sections of `README.md` and `CONTRIBUTING.md`.

## Scope

Activate `wespy` through the Conda PowerShell hook. Build the source distribution and wheel, run Twine metadata validation, inspect both archives for intended and excluded content, and install the wheel into an isolated temporary environment for an import and public-API smoke test. Prefer offline/no-dependency installation for the built wheel and use the active environment's dependencies only when necessary.

## Authorized inputs and outputs

Read repository packaging files. Build artifacts under `dist/`, build caches, and a temporary isolated smoke-test environment are authorized. Write only `verification/V07-package-validation.md` as a durable report.

## Prohibited actions

Do not edit implementation or metadata files, apply fixes, publish or upload artifacts, read experimental data, or contact GitHub or PyPI.

## Acceptance criteria

- The active interpreter resolves inside `E:\conda\envs\wespy`.
- `python -m build`, `python -m twine check dist/*`, archive-content checks, and a wheel import/API smoke test complete.
- The smoke test demonstrates that `wesandersonpy` imports from the installed wheel rather than the source tree.
- The report gives a clear verdict and lists generated artifacts.
