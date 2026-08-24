# T15: Complete static implementation reverification

## Context

Read `context/conversation-v004.md`, `verification/V03-static-implementation.md`, and the revision reports produced for T03, T05, T06, and repository metadata after V03.

## Scope

Independently reverify corrections for V03-F01 through V03-F03 and the low-severity changelog wording, then confirm that no regression affects prior V03 passes.

## Authorized inputs

The complete current repository implementation and the immutable V03 report.

## Prohibited actions

Remain read-only. Do not run Python or Python-based tooling, mutate files, stage changes, commit, or modify V03.

## Expected output

`docs/agent-runs/active/2026-08-23-python-package-conversion/verification/V04-static-implementation.md`.

## Acceptance criteria

- No Python source line exceeds the configured 88-column limit.
- Scatter and readout examples implement the approved semantic palette roles using the package API and no hard-coded hex values.
- Default and documented first-pass example outputs use the ignored `examples/figures/generated/` directory, with an explicit human promotion step for approved exhibits.
- The changelog describes implemented unreleased functionality accurately.
- No regression is found in core parity, tests, schemas, links, gallery values, metadata, or CI/release security.
- The report gives a clear T08 human-execution readiness verdict.
