# T06 README and palette gallery result r02

## Task and context

- Task: T06 follow-up for V03-F03, generated-output hygiene in the root README.
- Context used: `context/conversation-v004.md`, the approved `plan.md`, `tasks/T06-readme-and-gallery.md`, `verification/V03-static-implementation.md`, and the concurrent final T05 correction.
- Status: Complete, pending independent static reverification and human rendering.

## Sources inspected

- `AGENT.md` and the approved T06 scope and context.
- `verification/V03-static-implementation.md`, specifically moderate finding V03-F03.
- The corrected `examples/README.md` and all five example `DEFAULT_OUTPUT` declarations after the T05 agent completed its concurrent correction.
- `.gitignore` rules for `examples/figures/generated/` and the current root `README.md`.

## Work performed

- Changed all five root README first-pass output paths from direct unignored files under `examples/figures/` to ignored staging files under `examples/figures/generated/`.
- Changed all five human rendering commands to pass `--output examples/figures/generated/<name>.png`.
- Expanded the example index to distinguish each ignored first-pass output from its eventual committed exhibit path under `examples/figures/`.
- Documented the required gate: a human must inspect a staged PNG for correctness and confidentiality, and only after explicit approval copy or move it to the named committed exhibit path and embed it in the README.
- Preserved the truthful statement that no example PNG has been generated, approved, or embedded.
- Did not change the palette gallery, its link, the 22 canonical names, or the 107 exact palette values.

## Evidence and checks

- A PowerShell-only scan found exactly five `uv run python examples/...` rendering commands in the root README and zero commands whose output bypasses `examples/figures/generated/`.
- The root README contains ten file-specific generated-path mentions: five in the example index and five in the rendering commands. It contains five direct PNG paths only in the explicitly labeled `Approved exhibit path` column.
- The root README contains the exact review-before-copy/move gate and zero embedded Markdown PNG images.
- `.gitignore` explicitly ignores `/examples/figures/generated/` while allowing human-approved exhibits directly under `examples/figures/`.
- After the concurrent T05 correction, static inspection confirmed that all five scripts default to `examples/figures/generated/*.png` and `examples/README.md` uses the same staging commands and promotion gate.
- The only existing file beneath `examples/figures/` at inspection time was `palette_gallery.svg`; no PNG was present.
- The README still contains one palette gallery SVG reference and all 107 exact palette hex strings.
- No Python file, interpreter, renderer, formatter, linter, test runner, build tool, or dependency command was executed.

## Files changed

- `README.md`
- This result record.

## Unchanged artifacts

- `examples/figures/palette_gallery.svg` was not modified.
- The prior `results/T06-readme-gallery-r01.md` remains immutable.
- T05-owned scripts and `examples/README.md` were changed only by the T05 agent, not by this task.

## Limitations and remaining gates

- Human rendering and visual review have not occurred. No example PNG may be promoted or embedded until that review confirms the output is correct, nonconfidential, based only on synthetic fixtures, and free of sensitive metadata.
- The final GitHub owner and repository URL remain unknown, so the separately documented release-time absolute-link work remains outstanding.

## Recommended next action

Have the independent verifier confirm that V03-F03 is resolved across all five script defaults, both README command sets, `.gitignore`, and the absence of unapproved PNGs. If the full correction set passes, the human can begin the documented runtime and rendering matrix using only the ignored staging paths.
