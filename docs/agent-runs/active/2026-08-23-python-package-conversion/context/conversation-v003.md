# Conversation context v003

## Checkpoint status

The human-authorized image-characterization and synthetic-data preparation pass is complete. The broader Python package implementation remains behind the original plan approval gate.

## Completed plot cases

- Sequence/time-domain diagram and two population sweeps: `examples/data/diagram_sequence/`.
- Multiple iterations with opacity fading: `examples/data/multiple_iterations/`.
- Multi-parameter fidelity curves and asymptotes: `examples/data/fidelity_multi_parameter/`.
- Simulation/experiment branch scatter and two probability panels: `examples/data/scatter_simulation/`.
- Readout sequence, tone response, IQ scatter, Rabi populations, and spin expectations: `examples/data/readout_calibration_rabi/`.

Every directory contains a prominent statement that its values are synthetic, non-experimental, not digitized, and unsuitable for scientific inference. No Python files were run.

## Result records

- T09: `results/T09-sequence-iterations-r01.md`.
- T10: `results/T10-fidelity-scatter-r02.md`; r02 supersedes r01 for Markdown style only.
- T11: `results/T11-readout-rabi-r02.md`; r02 resolves the data-coverage findings in V01.

## Verification record

- `verification/V01-synthetic-data.md` passed four cases and found two moderate T11 coverage defects plus one low-severity scaling ambiguity.
- T11 r02 placed all nine tone states on one 11-point detuning grid spanning `-1.50..1.00 MHz`, added 18 separately selectable IQ background rows through `point_role`, and stored spin display values directly in `expectation_j_units` on the illustrative `[-3.5, 3.5]` scale.
- `verification/V02-readout-rabi.md` passed all revisions with no remaining defects. Combined with V01, the complete five-case set is ready for human qualitative review before plotting-script implementation.

## Next action

The human should review the five schema READMEs and may inspect the CSVs. If the characteristics and synthetic data are approved, the human can approve the full package plan and provide author/repository metadata. Plotting scripts will then be implemented against these fixtures but will be run by the human, consistent with `AGENT.md`.
