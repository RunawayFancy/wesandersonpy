# T03: Matplotlib integration

## Context

Use `context/conversation-v001.md`, the approved plan, and T02 outputs.

## Scope

Implement discrete and continuous Matplotlib colormap creation, reversal, resampling, and explicit optional registration.

## Authorized inputs

The core palette API and current official Matplotlib color and colormap documentation.

## Prohibited inputs and actions

Do not register colormaps as an import side effect. Do not execute plots or Python scripts.

## Expected outputs

Matplotlib-facing functions in `src/wesandersonpy/palettes.py` or a small dedicated module, re-exported through the public API.

## Acceptance criteria

Returned objects are correct Matplotlib colormap types, canonical names remain traceable, reversal and requested sizes are deterministic, repeated registration has defined behavior, and importing the package does not mutate Matplotlib global state.

## Dependencies

T02.
