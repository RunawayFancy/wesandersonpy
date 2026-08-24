# T20: Static-quality failure diagnosis

## Context

Read `context/conversation-v006.md` and `verification/V06-static-quality.md`.

## Scope

Activate `wespy` and diagnose the static-quality failures without changing files. Capture exact Ruff import-order findings and format diffs. Rerun mypy with an explicit Python 3.12 target only as a diagnostic comparison to determine whether package code has errors after bypassing the configured Python 3.10 versus NumPy-stub incompatibility.

## Authorized inputs and outputs

Read repository source, tests, examples, and configuration. Write only `verification/V09-static-quality-diagnosis.md`.

## Prohibited actions

Do not use Ruff fix or format-write modes, edit any implementation or configuration, install packages, or use network services.

## Acceptance criteria

- List every file and rule reported by Ruff lint.
- List every file Ruff would reformat without applying formatting.
- Distinguish configured-mypy failure from the Python 3.12 diagnostic result.
- Recommend possible fixes but do not apply them.
