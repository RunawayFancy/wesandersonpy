# T17: Lint, formatting, and type checks

## Context

Read `context/conversation-v006.md`, `pyproject.toml`, and `.pre-commit-config.yaml` if present.

## Scope

Activate `wespy` through the Conda PowerShell hook. Run Ruff lint, Ruff formatting verification, mypy, and any repository-local pre-commit checks that do not require downloading unavailable tools.

## Authorized inputs and outputs

Read the complete non-experimental repository. Tool caches may be generated. Write only `verification/V06-static-quality.md` as a durable report.

## Prohibited actions

Do not use auto-fix or formatting modes, edit implementation files, install tools, read experimental data, or access remote services.

## Acceptance criteria

- The active interpreter resolves inside `E:\conda\envs\wespy`.
- `python -m ruff check .`, `python -m ruff format --check .`, and `python -m mypy src/wesandersonpy` complete.
- Pre-commit execution is recorded when locally possible; inability to download a hook is reported separately from source-quality failures.
- The report gives a clear verdict.
