"""Checks for the supported import surface and installed metadata."""

from __future__ import annotations

from importlib import metadata, resources

import wesandersonpy as wes
import wesandersonpy.palettes as palettes


EXPECTED_EXPORTS = {
    "PALETTES",
    "__version__",
    "available_palettes",
    "get_colormap",
    "get_palette",
    "register_colormaps",
    "wes_palette",
}


def test_root_public_exports_are_exact_and_available() -> None:
    assert set(wes.__all__) == EXPECTED_EXPORTS
    assert all(hasattr(wes, name) for name in EXPECTED_EXPORTS)


def test_palette_module_exports_are_available_at_package_root() -> None:
    module_exports = set(palettes.__all__)

    assert module_exports == EXPECTED_EXPORTS - {"__version__"}
    assert all(getattr(wes, name) is getattr(palettes, name) for name in module_exports)


def test_version_matches_installed_distribution_metadata() -> None:
    distribution = metadata.distribution("wesandersonpy")
    requirements = tuple(
        requirement.lower().replace(" ", "")
        for requirement in distribution.requires or ()
    )

    assert wes.__version__ == "0.1.0"
    assert distribution.version == wes.__version__
    assert distribution.metadata["Name"] == "wesandersonpy"
    assert distribution.metadata["Requires-Python"] == ">=3.10"
    assert any(
        requirement.startswith("matplotlib")
        and ">=3.8" in requirement
        and "<4" in requirement
        for requirement in requirements
    )


def test_py_typed_marker_is_in_the_importable_package() -> None:
    marker = resources.files("wesandersonpy").joinpath("py.typed")

    assert marker.is_file()
