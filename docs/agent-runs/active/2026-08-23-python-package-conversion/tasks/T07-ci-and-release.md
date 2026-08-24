# T07: CI and release automation

## Context

Use `context/conversation-v001.md`, the approved plan, and T04 plus T06 outputs.

## Scope

Add GitHub Actions for quality checks, tests, builds, artifacts, and tag-driven PyPI Trusted Publishing, plus dependency update configuration and release documentation.

## Authorized inputs

Repository code and metadata, current GitHub, PyPA, and PyPI official documentation, and human-approved support targets.

## Prohibited inputs and actions

Do not create a GitHub repository, push commits, store credentials, configure PyPI, publish artifacts, or create a release without separate human action.

## Expected outputs

`.github/workflows/ci.yml`, `.github/workflows/publish.yml`, `.github/dependabot.yml`, and contributor/release instructions.

## Acceptance criteria

CI checks all supported environments, build artifacts are produced once and passed to publishing, release publishing uses OIDC with least privilege and a protected environment, and external actions are pinned to reviewed commit SHAs.

## Dependencies

T04 and T06.
