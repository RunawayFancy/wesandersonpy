# T27: Independent verification of revised plotting examples

## Context

Read `context/conversation-v007.md`, baseline reports T21 through T23, and revision reports T24 through T26.

## Scope

Independently verify the five revised example scripts without relying on implementer conclusions. Activate `wespy`; render all five scripts into `examples/figures/generated/final-review/` using only bundled synthetic fixtures. Inspect every final-review PNG and its corresponding authorized reference PNG at original detail. Run Ruff lint and format checks on all five scripts and run the repository pytest suite. Search the five scripts for hard-coded hexadecimal colors.

## Prohibited actions

Remain read-only with respect to implementation, fixtures, references, prior reports, and plan files. Do not extract numerical data from references, use experimental data, apply fixes, promote images, or publish artifacts. Write only `verification/V10-visual-examples.md`.

## Acceptance criteria

- Every script exits successfully and visibly labels its data as synthetic/non-experimental.
- No label, legend, axis title, panel tag, inset, or footer has a blocking overlap or clipping defect.
- Each revised image preserves its reference's key plotting grammar and hierarchy without copying values.
- Package-derived color roles are intentional, consistent, harmonious on white, and paired with marker, line, opacity, or direct-label redundancy.
- Fidelity uses a discrete palette for categories; faded iterations separate navy/red/light-blue roles; scatter separates warm simulation/dark experiment/red highlight; readout uses a landscape layout and stable red/teal/green targets.
- Ruff, formatting, tests, and no-hard-coded-hex checks are recorded.
- The report gives an exhibit-readiness verdict and lists subjective limitations without asserting quantitative aesthetic superiority.
