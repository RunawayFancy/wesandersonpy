# T19: Package validation after isolated build

## Context

Read `context/conversation-v006.md`, `tasks/T18-package-validation.md`, and `verification/V07-package-validation.md`. The host subsequently ran the prescribed isolated `python -m build` with temporary network access for declared build dependencies; it produced `dist/wesandersonpy-0.1.0.tar.gz` and `dist/wesandersonpy-0.1.0-py3-none-any.whl` without changing source files.

## Scope

Activate `wespy`. Independently run Twine metadata validation, inspect both archives for intended and prohibited content, and install the wheel into an isolated temporary environment for an import and public-API smoke test. Confirm the imported module path comes from the isolated installation rather than the working tree.

## Authorized inputs and outputs

Read repository packaging files and `dist/`. An isolated temporary environment is authorized. Write only `verification/V08-package-reverification.md`.

## Prohibited actions

Do not edit implementation or metadata, apply fixes, publish artifacts, read experimental data, or use remote services.

## Acceptance criteria

- Twine passes both distributions.
- Archive contents include required package and metadata files and exclude repository-only agent, reference, source-example, generated, cache, and credential content according to `pyproject.toml`.
- An isolated wheel installation imports `wesandersonpy` from its environment and exercises representative palette and Matplotlib APIs.
- The report gives a clear verdict and preserves V07 as immutable history.
