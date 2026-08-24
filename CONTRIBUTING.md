# Contributing

Thank you for helping improve `wesandersonpy`. By participating, you agree to follow `CODE_OF_CONDUCT.md` and to license your contribution under the project's MIT License.

## Development setup

Install Python 3.10 or newer and `uv`, then synchronize the reproducible development environment from the committed lock file:

```console
uv sync --locked --extra dev --extra examples
```

When dependency declarations intentionally change, regenerate the lock file and verify the locked environment before committing both changes:

```console
uv lock
uv sync --locked --extra dev --extra examples
```

Do not hand-edit or fabricate `uv.lock`. A human maintainer must review lock-file changes and run all validation commands before committing them.

## Quality checks

Before proposing a change, run:

```console
uv run ruff format --check .
uv run ruff check .
uv run mypy src/wesandersonpy
uv run pytest --cov=wesandersonpy --cov-report=term-missing
uv run python -m build
uv run twine check dist/*
```

Keep changes focused and add tests for behavior changes. Public functions should remain typed and documented. Do not commit credentials, private material, confidential figures, experimental data, or measurement-derived fixtures. Example data must be independently synthetic and clearly labeled.

## Upstream R reference

The unchanged upstream checkout is retained locally at `reference/wesanderson-r/`, including its nested Git history, and is intentionally ignored by the outer repository to avoid accidentally recording it as an embedded repository or gitlink. Python distributions also exclude `reference/`. Do not delete, rewrite, stage, or convert that nested checkout without a separate maintainer decision. Upstream provenance is recorded in `NOTICE.md` and `LICENSE`.

## Releases

Maintainers update `CHANGELOG.md`, verify wheel and source-distribution contents, and create a SemVer tag only after the human-run verification matrix passes. Publishing uses PyPI Trusted Publishing; never add a long-lived PyPI token to the repository.

### One-time GitHub and PyPI configuration

These steps require a human repository owner after the canonical GitHub owner and repository name are known:

1. Create the GitHub repository, push the reviewed `main` branch, and enable GitHub Actions. Keep the default `GITHUB_TOKEN` permission read-only.
2. Create a GitHub environment named exactly `pypi`. Add required reviewers, prevent administrators from bypassing protection where appropriate, and restrict deployment to release tags that follow the project's `vMAJOR.MINOR.PATCH` convention.
3. Create or claim the `wesandersonpy` PyPI project and configure a GitHub Trusted Publisher. Enter the final GitHub owner, repository name, workflow filename `publish.yml`, and environment name `pypi`. If the project does not yet exist, use PyPI's pending-publisher flow.
4. Enable branch protection for `main` and require the CI quality, test, and build jobs before merging. Protect changes to `.github/workflows/publish.yml` with maintainer review or an appropriate `CODEOWNERS` rule.
5. Enable Dependabot version updates. Dependabot will propose updates for GitHub Actions and the uv-managed Python dependencies from `.github/dependabot.yml`; a human must review and merge each proposal.

### Publishing a version

1. Update the single project version in `pyproject.toml` and add the release notes to `CHANGELOG.md`.
2. Run the complete human verification matrix, inspect the wheel and source archive, and confirm the README renders correctly from the built metadata.
3. Merge the reviewed release changes and wait for CI to pass on `main`.
4. Create a GitHub release whose tag is exactly `vMAJOR.MINOR.PATCH` for the version in `pyproject.toml`. Publishing the release triggers `.github/workflows/publish.yml`.
5. Approve the protected `pypi` environment deployment only after checking the workflow source, tag, commit, verification job, and build job. The release workflow independently checks formatting, linting, typing, and tests before it builds the distributions once, transfers them through a short-lived GitHub artifact, and publishes through OIDC without a stored PyPI token.
6. Verify the new PyPI page, metadata, wheel installation, and source-distribution installation. PyPI release files cannot be replaced; correct a faulty release with a new version rather than attempting to overwrite it.

The workflow rejects a release tag that does not exactly equal `v` plus the version in `pyproject.toml`. Account creation, environment approval, tag creation, release publication, and post-publication verification always remain human-controlled.

### Updating workflow action pins

All third-party actions are pinned to full commit SHAs, followed by comments naming the reviewed release tags. When Dependabot proposes an update, verify the new SHA and tag in the action's official repository, review its release notes and changed runtime, and keep the immutable full SHA in the merged workflow. Never replace a SHA pin with a floating branch or tag.

Release infrastructure guidance was last reviewed on 2026-08-23 against the [GitHub secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use), [GitHub release-event documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#release), [PyPA publishing guide](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/), [PyPI Trusted Publishers documentation](https://docs.pypi.org/trusted-publishers/using-a-publisher/), and [GitHub Dependabot documentation](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates).
