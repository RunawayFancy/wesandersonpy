# T01: Repository and metadata baseline

## Context

Use `context/conversation-v001.md` and the approved `plan.md`.

## Scope

Initialize Git, establish the `src` project layout, resolve the R reference location, and add packaging, licensing, provenance, versioning, contribution, citation, security, ignore, and dependency-control metadata.

## Authorized inputs

The root project structure, non-experimental R package source, approved plan, and human-provided public author and repository metadata.

## Prohibited inputs and actions

Do not read experimental data, publish a remote repository, configure accounts, or create releases. Do not move the R reference without explicit approval.

## Expected outputs

Git baseline; `pyproject.toml`; `src/wesandersonpy/`; `LICENSE`; `NOTICE.md`; `CHANGELOG.md`; `CONTRIBUTING.md`; `CITATION.cff`; `CODE_OF_CONDUCT.md`; `SECURITY.md`; `.gitignore`; `.gitattributes`; `.editorconfig`; `.pre-commit-config.yaml`; and development dependency definitions.

## Acceptance criteria

All metadata is internally consistent, upstream attribution is preserved, confidential and generated paths are ignored, and no placeholder identity or URL is presented as factual.

## Dependencies

Human approval of the plan and required metadata decisions.
