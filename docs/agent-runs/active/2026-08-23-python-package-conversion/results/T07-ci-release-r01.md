# T07 CI and release automation result r01

## Task and context

- Task: T07, CI, release automation, dependency updates, and publication documentation.
- Context used: `context/conversation-v004.md`, the approved `plan.md`, `tasks/T07-ci-and-release.md`, T04 and T06 result reports, `pyproject.toml`, `CONTRIBUTING.md`, `SECURITY.md`, and all current tests.
- Status: Static implementation complete. GitHub execution, the required `uv.lock`, account configuration, protected-environment approval, and publication remain human-controlled and unverified.

## Sources inspected

All external sources below are primary official documentation or official release metadata and were accessed on 2026-08-23.

- [GitHub: Building and testing Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python), for explicit Python setup and version/operating-system matrices.
- [GitHub: Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#release), for the `release` event and `published` activity type. A published event covers both stable releases and prereleases published from drafts and resolves `GITHUB_SHA` to the tagged release commit.
- [GitHub: Workflow syntax and token permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions), for workflow- and job-level least-privilege permissions.
- [GitHub: Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use), for read-only default token permissions and immutable full-length action SHA pins.
- [PyPA: Publishing package distributions with GitHub Actions](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/), for separate build/publish jobs, artifact transfer, a `pypi` environment, and Trusted Publishing.
- [PyPI: Publishing with a Trusted Publisher](https://docs.pypi.org/trusted-publishers/using-a-publisher/), for secret-free OIDC publishing, `id-token: write`, and the strongly encouraged GitHub environment.
- [PyPI: Adding a Trusted Publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/), for the exact GitHub owner, repository, workflow filename, and environment values that the human must configure.
- [GitHub: Dependabot version-update configuration](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates) and [supported ecosystems](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories), for weekly GitHub Actions updates and the current `uv` ecosystem identifier.
- [Astral: Using uv in GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/), for the official setup action, pinning the uv tool version, locked synchronization, caching, matrix use, and separating build from the OIDC-enabled publish job.
- Official GitHub releases and Git-reference API responses for every selected action and uv tool release. The release tag was resolved to the underlying commit rather than copied from an unofficial workflow. Exact selections are recorded below.

## Reviewed immutable action pins

| Action | Release tag | Full commit SHA |
|---|---|---|
| `actions/checkout` | [`v7.0.1`](https://github.com/actions/checkout/releases/tag/v7.0.1) | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| `actions/setup-python` | [`v7.0.0`](https://github.com/actions/setup-python/releases/tag/v7.0.0) | `5fda3b95a4ea91299a34e894583c3862153e4b97` |
| `astral-sh/setup-uv` | [`v10.0.1`](https://github.com/astral-sh/setup-uv/releases/tag/v10.0.1) | `20cfd1bf945f4377ade1205e4dbc17946fc9a30d` |
| `actions/upload-artifact` | [`v7.0.1`](https://github.com/actions/upload-artifact/releases/tag/v7.0.1) | `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` |
| `actions/download-artifact` | [`v8.0.1`](https://github.com/actions/download-artifact/releases/tag/v8.0.1) | `3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c` |
| `pypa/gh-action-pypi-publish` | [`v1.14.2`](https://github.com/pypa/gh-action-pypi-publish/releases/tag/v1.14.2) | `dc37677b2e1c63e2034f94d8a5b11f265b73ba33` |

The installed uv tool is separately pinned to official release [`0.12.5`](https://github.com/astral-sh/uv/releases/tag/0.12.5), published 2026-08-14. Every `uses:` reference is a 40-character lowercase hexadecimal commit SHA followed by its reviewed release tag as a comment.

## Work performed

- Added CI for pushes to `main`, pull requests, and manual runs with read-only repository contents permission, cancellation of stale branch runs, explicit timeouts, and credential persistence disabled at checkout.
- Added a dedicated quality job on Python 3.14 for Ruff formatting, Ruff linting, and strict mypy checks.
- Added nine test jobs: every supported CPython minor from 3.10 through 3.14 on Ubuntu, plus oldest/newest boundary coverage on both macOS and Windows. This tests the complete declared Python range while keeping non-Linux runner use proportionate.
- Added a CI build job that runs only after quality and all test jobs pass, builds one wheel and one source distribution, checks metadata with Twine, and retains the CI artifact for seven days.
- Made all CI environments synchronize from the committed lock using `uv sync --locked --extra dev`; commands then use `uv run --no-sync` so later steps cannot silently re-resolve dependencies.
- Added a `release: published` workflow with a technically enforced `verify -> build -> publish` graph. The verification job checks the released tag, synchronizes the locked environment, validates exact `v` plus metadata-version equality, and reruns Ruff formatting, Ruff linting, mypy, and pytest.
- The release build job runs only after verification, checks out the released tag, builds distributions exactly once, runs Twine metadata checks, and uploads a one-day artifact. The publish job downloads that same artifact and does not rebuild it.
- Restricted the publish job to the protected `pypi` environment and only `id-token: write`. It uses the PyPA publishing action through OIDC and contains no username, password, API token, or secret reference. Build and verification jobs inherit only `contents: read`.
- Added weekly Dependabot checks for immutable GitHub Action pins and uv-managed Python dependencies.
- Expanded `CONTRIBUTING.md` with one-time GitHub/PyPI configuration, protected-environment and branch-protection guidance, an exact release checklist, immutable PyPI-file handling, and a review process for Dependabot action-pin updates.
- Left `SECURITY.md` unchanged because its private-reporting instructions are already release-appropriate and no CI-specific security edit was essential.

## Files changed

- `.github/workflows/ci.yml`
- `.github/workflows/publish.yml`
- `.github/dependabot.yml`
- `CONTRIBUTING.md`
- `docs/agent-runs/active/2026-08-23-python-package-conversion/results/T07-ci-release-r01.md`

## Static checks and evidence

- A PowerShell-only scan found 19 `uses:` occurrences across both workflows. Every occurrence has a 40-character lowercase hexadecimal commit and a release-tag comment.
- The release workflow contains exactly one `python -m build` invocation, one artifact upload action, and one artifact download action.
- Static dependency-graph checks found `build` needs `verify` and `publish` needs `build`.
- Static policy checks found the `release`/`published` trigger, named `pypi` environment, and publish-job `id-token: write` permission. Workflow-level permission is only `contents: read`.
- The CI matrix explicitly contains all five supported Python versions and both Python-range boundaries on Ubuntu, macOS, and Windows.
- A text scan found no tab indentation, trailing whitespace, or credential/secret references in the workflow and release-documentation files. `actionlint` is not installed locally, so no claim is made that an executable GitHub Actions validator passed.
- `git diff --check` reported no whitespace errors. Git status was read with a command-local safe-directory exception only; no local or global Git configuration was changed.
- No Python interpreter, uv synchronization, test, formatter, linter, type checker, build tool, Twine operation, workflow, dependency installer, remote repository mutation, or publication command was executed by this agent.

## Mandatory human configuration and verification

1. Run `uv lock`, review the generated file, run `uv lock --check`, and commit `uv.lock`. The lock file is currently absent. Both CI and release workflows intentionally use `uv sync --locked`, so neither workflow can pass until a human generates, validates, and commits this file.
2. Run the complete T04 and T05/T06 human verification matrix locally before pushing. Return failures to the host without weakening expected checks.
3. Supply the final GitHub owner and repository name, create the remote repository, push the reviewed history, and enable GitHub Actions and Dependabot.
4. Protect `main` and require the CI quality, test, and build checks. Protect release-workflow changes with maintainer review or `CODEOWNERS` after ownership is known.
5. Create the GitHub environment named exactly `pypi`, add required reviewers, consider blocking administrator bypass, and restrict deployments to the intended release-tag pattern.
6. Create or claim the `wesandersonpy` PyPI project. Configure its GitHub Trusted Publisher with the exact final owner, repository, workflow filename `publish.yml`, and environment `pypi`; use a pending publisher if the PyPI project does not yet exist.
7. Recheck that the `wesandersonpy` distribution name is available immediately before publication. No availability claim in this report substitutes for that human check.
8. After CI and local release checks pass, create a GitHub release with a tag exactly matching `v` plus the `pyproject.toml` version. Publishing the release starts the workflow, but the protected environment must keep publication behind human approval.
9. Before approving the `pypi` job, inspect the workflow file at the release tag, verification and build logs, source commit, artifact names, and requested permissions. After publishing, verify the PyPI metadata and clean installations from both distribution formats.

## Limitations and unresolved evidence

- YAML syntax and GitHub runner behavior have been statically reviewed but not executed. The first remote CI run is required evidence.
- `uv.lock` is absent by policy because an agent may not generate it. This is the only known local prerequisite that will deliberately make the workflows fail before the human completes verification.
- The final GitHub owner, repository name, and public maintainer identity remain unknown. `CONTRIBUTING.md` therefore documents the exact fields without inventing values, and no external account was configured.
- Protected environments, required reviewers, branch rules, Trusted Publisher identities, and the PyPI project exist only as documented human steps until the owner configures them.
- The action pins are current as of the access date, not an instruction to merge future updates automatically. Dependabot changes require a new official-release and commit-SHA review.

## Recommended next action

The host should send these implementation files and this report to the independent T08 verifier, then ask the human to generate and commit `uv.lock` and execute the consolidated verification matrix. Do not create or publish a GitHub release until local checks, CI, archive inspection, README/exhibit approval, the protected `pypi` environment, and PyPI Trusted Publisher configuration are all confirmed.
