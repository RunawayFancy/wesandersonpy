# T24: Revise diagram and faded-iteration examples

## Context

Read `context/conversation-v007.md` and `results/T21-diagram-iterations-visual-review-r01.md`.

## Scope and ownership

Edit only `examples/diagram_sequence_time_domain.py` and `examples/multiple_iterations_faded.py`. Preserve every synthetic fixture value and plotting grammar. Implement the T21 recommendations with package-derived semantic color roles, redundant state markers, clearer mathematical labels, muted guide colors, non-overlapping sequence annotations, a lighter response guide, a smaller/cleaner population inset, and tighter vertical allocation. Retain visible synthetic-data notices. Render candidates under `examples/figures/generated/candidate/` and format/check only the two owned scripts.

## Acceptance criteria

- No hard-coded hexadecimal colors or non-package categorical color sets are introduced.
- Diagram event labels do not overlap and use semantically connected, readable colors.
- State categories remain identifiable without relying only on close hues.
- Faded iterations use dark navy/ink, brick red, and light blue with a muted guide and readable fading.
- Both scripts run in `wespy`; both candidate/reference pairs are inspected at original detail.
- Write `results/T24-diagram-iterations-visual-revision-r01.md` with changes, commands, evidence, and remaining limitations.
