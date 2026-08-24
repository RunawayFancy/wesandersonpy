# T14: Complete static implementation verification

## Context

Read `context/conversation-v004.md`, the approved plan, T01 through T07 result reports using the latest revision where applicable, and V01/V02 synthetic-data verification reports.

## Scope

Independently verify the complete repository implementation against the plan and task acceptance criteria using static inspection and read-only non-Python checks.

## Authorized inputs

All tracked-candidate project files except the ignored upstream nested checkout and ignored reference PNGs. The verifier may inspect filenames and Git ignore status for ignored paths but must not use their contents as implementation evidence.

## Prohibited actions

Do not modify implementation, plan, context, task, result, or earlier verification files. Do not run Python, pytest, Ruff, mypy, uv, build, Twine, examples, GitHub workflows, or publishing actions. Do not stage or commit files.

## Expected output

`docs/agent-runs/active/2026-08-23-python-package-conversion/verification/V03-static-implementation.md`.

## Required checks

- Repository structure, Git state, ignore behavior, metadata consistency, license, attribution, and absence of fabricated personal/remote metadata.
- Exact public palette coverage, aliases/private seed, immutability, typing, validation, Matplotlib types/registration/no import side effect by static code review.
- Test coverage of the documented contract and static source/test consistency.
- All five example scripts, input/output CLI contracts, fixture schemas, palette API use, output closing, overwrite protection, and synthetic labeling.
- README/API/gallery exactness, link existence, SVG structure/value parity, and explicit unresolved human render/URL gates.
- CI/release dependency graph, action SHA pins, permissions, secrets, locked dependency requirement, supported Python/OS coverage, and human-only external actions.
- Identify confirmed defects separately from human-run unknowns and optional improvements, then state whether the code is ready for T08 human execution.

## Dependencies

T01 through T07 and V02.
