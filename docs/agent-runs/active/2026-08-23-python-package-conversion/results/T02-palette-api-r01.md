# T02 core palette API result r01

## Task and context

- Task: T02, core palette API.
- Context used: `context/conversation-v004.md`, the approved `plan.md`, and `tasks/T02-core-palette-api.md`.
- Status: Complete, pending independent tests and human-run Python verification.

## Sources inspected

- `AGENT.md` for project permissions, data restrictions, code rules, and subagent reporting requirements.
- `reference/wesanderson-r/R/colors.R`, after the reference was moved from its original root location during this task.
- `reference/wesanderson-r/R/wesanderson.R`, `reference/wesanderson-r/R/globals.R`, `reference/wesanderson-r/man/wes_palette.Rd`, and the palette headings and calls in `reference/wesanderson-r/README.md`.
- The approved plan and T02 contract listed above.

## Work performed

- Added all 22 canonical movie palettes as immutable tuples in stable upstream source order.
- Added the upstream `Rushmore` name as an alias of canonical `Rushmore1` without duplicating it in the public canonical mapping.
- Retained `Zissou1Continuous` as a private 11-color interpolation seed associated with `Zissou1`, matching the R implementation rather than presenting it as a separate movie palette.
- Implemented the read-only `PALETTES` mapping, `available_palettes()`, and typed `get_palette()` API.
- Implemented discrete source limits, RGB interpolation, full-palette reversal, validation for names, kinds, and requested sizes, and actionable exceptions.
- Exposed `wes_palette` as a direct compatibility alias for R-style positional calls.
- Added package exports, version `0.1.0`, and the PEP 561 `py.typed` marker.

## Evidence and checks

- A read-only PowerShell parser found 24 R list entries: 22 canonical palettes, `Rushmore`, and `Zissou1Continuous`.
- A case-sensitive per-palette comparison checked all 107 canonical hexadecimal literals in sequence and passed.
- A separate case-sensitive sequence comparison checked all 11 `Zissou1Continuous` seed literals and passed.
- The parser confirmed that upstream `Rushmore` and `Rushmore1` contain identical values; static source inspection confirmed the Python alias maps `Rushmore` to `Rushmore1`.
- Static line-length inspection found no Python source line longer than 100 characters.
- No Python file, interpreter, formatter, linter, type checker, or test runner was executed, in accordance with `AGENT.md` and the approved context.

## Files changed

- `src/wesandersonpy/_palette_data.py`
- `src/wesandersonpy/palettes.py`
- `src/wesandersonpy/__init__.py`
- `src/wesandersonpy/py.typed`
- This result record.

## Limitations and unresolved questions

- Runtime behavior remains unexecuted. The human must run the test, lint, typing, build, and clean-install commands supplied by the host.
- Continuous interpolation is performed with Matplotlib's public RGB colormap implementation. The canonical source colors and special Zissou seed are exact, but intermediate colors are not claimed to be byte-for-byte identical to R's `grDevices::colorRampPalette` rounding behavior.
- The `wes_palette` alias intentionally uses Python's `kind=` keyword; R's `type=` keyword is not reproduced. Positional calls remain compatible.

## Recommended next action

Have an independent verifier exercise the immutable mapping, exact values, alias, all validation branches, discrete limits, interpolation endpoints and sizes, reversal, typing, and public exports when human-authorized Python verification is performed.
