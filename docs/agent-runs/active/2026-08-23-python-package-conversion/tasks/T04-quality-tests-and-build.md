# T04: Quality, tests, dependencies, and build

## Context

Use `context/conversation-v001.md`, the approved plan, and T01 through T03 outputs.

## Scope

Add tests and configure formatting, linting, typing, coverage, reproducible development dependencies, wheel creation, source distribution creation, metadata checking, and clean-install checking.

## Authorized inputs

Implementation files, package metadata, current tool documentation, and non-data test fixtures limited to canonical palette constants and API inputs.

## Prohibited inputs and actions

Do not use experimental or measurement-derived fixtures. Do not run Python files; prepare human-run commands instead.

## Expected outputs

Tests under `tests/`, complete tool configuration in `pyproject.toml`, `uv.lock`, and a human verification command sheet incorporated into the final handoff.

## Acceptance criteria

Tests cover exact palette parity, errors, immutability, interpolation, Matplotlib types, registration, public exports, and distribution installation. Runtime and development dependencies remain separated.

## Dependencies

T02 and T03.
