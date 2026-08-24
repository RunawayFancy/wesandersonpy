# V08: Package reverification after isolated build

## Verification identity and verdict

- Task: T19, independent package validation using the host-built artifacts in `dist/`.
- Context: `context/conversation-v006.md`, T18, T19, and V07.
- Validation date: 2026-08-23.
- Overall verdict: **FAIL on source-distribution hygiene.**

Twine passes both artifacts, the wheel has the intended package/metadata contents, and an offline isolated wheel installation passes representative public palette and Matplotlib API checks while importing from the temporary environment. However, the source distribution contains the repository-only root `AGENT.md`, contrary to T19's requirement that repository-only agent content be excluded. V07 remains unchanged.

## Scope and constraints

This verifier used the existing host-built artifacts only:

- `dist/wesandersonpy-0.1.0-py3-none-any.whl`
- `dist/wesandersonpy-0.1.0.tar.gz`

The build was not rerun. No implementation, metadata, archive, fixture, or prior report was edited. No remote service or package index was contacted, and no experimental data or restricted reference image was read.

## Artifact identity

| Artifact | Size | SHA-256 |
|---|---:|---|
| `wesandersonpy-0.1.0-py3-none-any.whl` | 11,990 bytes | `E58E59C9454E4F0C6F6853EC4A1C69947258C5FE7559458F9D4707799E16A8DA` |
| `wesandersonpy-0.1.0.tar.gz` | 48,865 bytes | `7715CA6A77AA98D766D2AAB51322427370393AC5703C3D783806714F909A258B` |

## Environment and Twine validation

The Conda PowerShell hook was loaded and `wespy` was activated. Observed values:

- `CONDA_PREFIX=E:\conda\envs\wespy`
- `Python 3.12.12`

Command:

```powershell
& 'E:\conda\shell\condabin\conda-hook.ps1'
conda activate wespy
python -m twine check dist/*
```

Result: pass, exit code 0.

```text
Checking dist\wesandersonpy-0.1.0-py3-none-any.whl: PASSED
Checking dist\wesandersonpy-0.1.0.tar.gz: PASSED
```

Wheel `METADATA` and source-distribution `PKG-INFO` agree on `Name: wesandersonpy`, `Version: 0.1.0`, `License-Expression: MIT`, `Requires-Python: >=3.10`, runtime requirement `matplotlib<4,>=3.8`, and the declared development/example extras.

## Archive-content inspection

Member names were inspected with `tar -tf`; metadata text was inspected with `tar -xOf`. No restricted file content was opened.

### Wheel

The wheel contains exactly eight members:

- `wesandersonpy/__init__.py`
- `wesandersonpy/_palette_data.py`
- `wesandersonpy/palettes.py`
- `wesandersonpy/py.typed`
- `wesandersonpy-0.1.0.dist-info/METADATA`
- `wesandersonpy-0.1.0.dist-info/WHEEL`
- `wesandersonpy-0.1.0.dist-info/licenses/LICENSE`
- `wesandersonpy-0.1.0.dist-info/RECORD`

Required-wheel missing count: zero. Prohibited-wheel member count: zero.

### Source distribution

The source distribution contains 53 members. Required files are present, including `pyproject.toml`, `README.md`, `LICENSE`, `NOTICE.md`, `PKG-INFO`, the four package files under `src/wesandersonpy/`, tests, synthetic example fixtures/scripts, and the approved palette-gallery SVG.

The scan confirmed exclusion of:

- `.agents/`
- `docs/agent-runs/`
- `reference/`
- `plotting_example/`
- `examples/figures/generated/`
- Git/build/test/type/lint caches
- credential-like `.env`, `.pem`, `.key`, and `credentials.*` paths

One prohibited repository-only agent file remains:

```text
wesandersonpy-0.1.0/AGENT.md
```

Required-source-distribution missing count: zero. Prohibited-source-distribution member count: one.

## Isolated wheel installation and API smoke test

A unique environment was created below the Windows temporary directory with `python -m venv --system-site-packages`. System site packages were necessary to reuse the already validated Matplotlib dependency without network access. The wheel was installed into the temporary environment with:

```powershell
<temporary-python> -m pip install --no-deps --no-index `
  --disable-pip-version-check --ignore-installed `
  E:\PhD_file\wesandersonpy\dist\wesandersonpy-0.1.0-py3-none-any.whl
```

The smoke script ran with the temporary directory as its working directory, outside the repository. Assertions and observations:

- `wesandersonpy.__file__` resolved to the temporary environment's `Lib\site-packages\wesandersonpy\__init__.py`, beneath `sys.prefix`, not to the working tree or base environment.
- `wesandersonpy.__version__ == "0.1.0"`.
- `available_palettes()` returned 22 canonical names.
- `get_palette("Royal1", n=3)` returned three expected source colors.
- `get_palette("Rushmore")` equaled `get_palette("Rushmore1")`.
- `get_colormap("Zissou1", kind="continuous", n=32)` returned `LinearSegmentedColormap` with `N=32`.
- `get_colormap("Darjeeling1", kind="discrete", n=5)` returned `ListedColormap` with `N=5`.

Observed import evidence:

```text
sys.prefix=C:\Users\Jiheng Duan\AppData\Local\Temp\wesandersonpy-v08-<unique-id>
wesandersonpy.__file__=C:\Users\Jiheng Duan\AppData\Local\Temp\wesandersonpy-v08-<unique-id>\Lib\site-packages\wesandersonpy\__init__.py
version=0.1.0
palette_count=22
continuous=LinearSegmentedColormap,N=32
discrete=ListedColormap,N=5
temporary_environment_removed=True
```

The first smoke invocation installed the wheel but did not execute package assertions because PowerShell stripped quotes from a `python -c` variable, causing a verifier-harness `SyntaxError`. Its temporary environment was removed. The verifier reran the unchanged assertions through Python standard input; that second invocation passed. This was a harness quoting defect, not a package failure.

## Acceptance-criteria matrix

| Criterion | Result | Evidence |
|---|---|---|
| Twine passes both distributions | Pass | Both files reported `PASSED`. |
| Required wheel/package metadata is present | Pass | Eight-member wheel has all required package and dist-info files. |
| Prohibited content is absent from wheel | Pass | Prohibited member count is zero. |
| Required source-distribution content is present | Pass | Required missing count is zero. |
| Repository-only and prohibited content is absent from source distribution | **Fail** | Root `AGENT.md` is included. |
| Offline isolated wheel installation succeeds | Pass | Wheel installed with `--no-deps --no-index` into a temporary venv. |
| Import originates in isolated installation | Pass | Resolved module path is beneath the temporary `sys.prefix`. |
| Representative palette and Matplotlib APIs work | Pass | Version, discovery, alias, palette, continuous, and listed-colormap assertions passed. |

## Finding

### V08-F01: root `AGENT.md` is packaged in the source distribution

Severity: moderate release-hygiene defect.

The source distribution includes `wesandersonpy-0.1.0/AGENT.md`. This is repository-only operational guidance for AI agents, not package source, user documentation, licensing, test, or example material. T19 explicitly requires repository-only agent content to be excluded. The current `pyproject.toml` source-distribution exclusions cover `/.agents` and `/docs/agent-runs` but do not cover `/AGENT.md`, which explains the observed member.

Reproduction:

```powershell
tar -tf dist/wesandersonpy-0.1.0.tar.gz |
  Select-String -Pattern '(^|/)AGENT\.md$'
```

## Generated artifacts and next action

- Existing host-built artifacts: unchanged.
- Temporary environments: both removed successfully.
- Durable output created by this verifier: `verification/V08-package-reverification.md` only.

Required next action: exclude the root `AGENT.md` from the source-distribution target, rebuild both artifacts, and perform another numbered package reverification. Preserve V07 and V08 as immutable history. Do not treat this verification as release-ready despite the passing Twine and wheel smoke results.
