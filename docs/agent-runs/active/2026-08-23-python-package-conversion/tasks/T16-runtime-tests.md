# T16: Runtime tests and coverage

## Context

Read `context/conversation-v006.md` and `pyproject.toml`.

## Scope

Activate `wespy` through the Conda PowerShell hook. Run the complete pytest suite with branch coverage and report the exact command, test counts, coverage result, warnings, and failures.

## Authorized inputs and outputs

Read repository source and tests. Test caches and coverage artifacts may be generated. Write only `verification/V05-runtime-tests.md` as a durable report.

## Prohibited actions

Do not edit source, tests, configuration, documentation other than the assigned report, or apply fixes. Do not read experimental data or use network services.

## Acceptance criteria

- The active interpreter resolves inside `E:\conda\envs\wespy`.
- `python -m pytest --cov=wesandersonpy --cov-branch --cov-report=term-missing` completes.
- The report separates confirmed failures from hypotheses and gives a clear verdict.
