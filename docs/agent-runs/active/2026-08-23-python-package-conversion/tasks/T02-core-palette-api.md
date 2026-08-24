# T02: Core palette API

## Context

Use `context/conversation-v001.md`, the approved plan, and T01 outputs.

## Scope

Port the canonical hexadecimal palette data and implement the typed, immutable public palette API.

## Authorized inputs

`wesanderson/R/colors.R`, the upstream README palette list, and approved Python package metadata.

## Prohibited inputs and actions

Do not inspect data directories or copy upstream prose and figures without attribution and license review. Do not run Python files.

## Expected outputs

`src/wesandersonpy/_palette_data.py`, `src/wesandersonpy/palettes.py`, `src/wesandersonpy/__init__.py`, and `src/wesandersonpy/py.typed`.

## Acceptance criteria

Palette names and values match the R source, public objects cannot mutate internal data, documented aliases work, interpolation and discrete limits match the approved contract, public functions are typed and documented, and failures are informative.

## Dependencies

T01.
