# T13: Readout-calibration/Rabi reverification

## Context

Read `context/conversation-v002.md`, `verification/V01-synthetic-data.md`, the T11 task contract, and `results/T11-readout-rabi-r02.md` after it is available.

## Scope

Independently verify the T11 r02 changes against the assigned reference image and the two moderate defects from V01: full shared detuning coverage for every tone-response state and a distinct sparse IQ background/outlier layer. Also verify that the spin expectation display scale is unambiguous and remains explicitly synthetic.

## Authorized inputs

The readout-calibration/Rabi PNG, its revised data directory and README, T11 r02, and V01.

## Prohibited actions

Remain read-only with respect to implementation and prior reports. Do not run Python, digitize reference values, or modify V01.

## Expected output

`docs/agent-runs/active/2026-08-23-python-package-conversion/verification/V02-readout-rabi.md`.

## Acceptance criteria

The report confirms whether every tone series spans the common domain, IQ background points are separately selectable, spin scaling is documented consistently, and the complete five-case synthetic-data set is ready for human review.

## Dependencies

T11 r02 and V01.
