# T08: Human verification and release handoff

## Context

Use `context/conversation-v001.md`, the approved plan, and all completed implementation tasks.

## Scope

Prepare exact human-run checks, review returned evidence, resolve implementation defects through versioned follow-up work, and document the steps the human must perform to publish safely.

## Authorized inputs

Repository implementation and human-returned command outputs and approved images that contain no confidential or experimental data.

## Prohibited inputs and actions

The agent must not execute Python files, access experimental results, push to GitHub, configure external accounts, or publish to PyPI.

## Expected outputs

Verification instructions, versioned verification records, an implementation final summary, and a release checklist for GitHub and PyPI.

## Acceptance criteria

The human reports successful lint, type, test, build, archive, clean-install, example, and README checks; all reported failures are resolved or explicitly documented; privacy is confirmed; and remaining publishing actions and rollback guidance are clear.

## Dependencies

T04, T05, T06, and T07.
