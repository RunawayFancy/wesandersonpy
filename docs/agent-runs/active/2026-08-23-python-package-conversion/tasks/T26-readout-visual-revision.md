# T26: Revise readout and Rabi composite example

## Context

Read `context/conversation-v007.md` and `results/T23-readout-visual-review-r01.md`.

## Scope and ownership

Edit only `examples/readout_calibration_rabi_subplots.py`. Preserve every synthetic fixture value and the four-region grammar. Rebuild the composition as a landscape left-calibration/right-dynamics hierarchy resembling the reference structure without copying measurements. Use stable package-derived roles for the target states across IQ and population panels, replace the too-similar light-cyan sage with a true muted green, reserve space for ladders/annotations, and clean up schematic labels. Display interpolation may be used only to render smooth paths through existing synthetic samples; it must not modify fixtures or imply new observations. Retain the visible synthetic-data notice. Render a candidate under `examples/figures/generated/candidate/` and format/check the owned script.

## Acceptance criteria

- All semantic colors come from `wesandersonpy`; no hard-coded hexadecimal colors are introduced.
- The composition is landscape, with calibration elements grouped left/top and duration dynamics given dominant space.
- State colors remain consistent across relevant panels and annotations do not obscure primary data.
- The script runs in `wespy`; the candidate/reference pair is inspected at original detail.
- Write `results/T26-readout-visual-revision-r01.md` with changes, commands, evidence, and remaining limitations.
