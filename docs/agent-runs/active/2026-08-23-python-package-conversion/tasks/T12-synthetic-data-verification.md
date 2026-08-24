# T12: Independent synthetic-data verification

## Context

Read `context/conversation-v002.md`, T09 through T11 task contracts, the T09 r01 report, the T10 r02 report, and the T11 r01 report.

## Scope

Independently verify that the five reference figures are accurately characterized at a qualitative layout level and that every companion CSV is clearly synthetic, structurally usable, internally consistent, and sufficient to exercise the visible plot layers.

## Authorized inputs

The five reference PNGs, the five `examples/data/` subdirectories, and the T09 through T11 reports.

## Prohibited actions

Remain read-only with respect to all implementation and result files. Do not digitize exact values, run Python, or alter any existing artifact.

## Expected output

`docs/agent-runs/active/2026-08-23-python-package-conversion/verification/V01-synthetic-data.md`.

## Required report content

Record verification scope, methods, visual comparison, CSV schema/count observations, disclaimer/provenance checks, pass/fail results, findings ordered by severity, untested areas, and a clear verdict. Distinguish defects from optional improvements.

## Acceptance criteria

The verifier confirms or rejects each case independently, identifies any missing visible layer or unusable schema, confirms that no artifact claims experimental validity, and reports whether the data are ready for human review before plotting-script implementation.

## Dependencies

Completed T09, T10 r02, and T11 artifacts.
