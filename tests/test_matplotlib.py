"""Tests for Matplotlib colormap creation and explicit registration."""

from __future__ import annotations

import subprocess
import sys
from collections.abc import Iterator

import matplotlib as mpl
import pytest
from matplotlib.colors import LinearSegmentedColormap, ListedColormap, to_rgba

import wesandersonpy as wes


@pytest.fixture
def registry_prefix(request: pytest.FixtureRequest) -> Iterator[str]:
    prefix = f"_wesandersonpy_test_{request.node.name}"
    names = tuple(f"{prefix}.{name}" for name in wes.available_palettes())
    _unregister(names)
    yield prefix
    _unregister(names)


def _unregister(names: tuple[str, ...]) -> None:
    for name in names:
        if name in mpl.colormaps:
            mpl.colormaps.unregister(name)


def test_fresh_import_does_not_change_matplotlib_registry() -> None:
    script = "\n".join(
        (
            "import matplotlib as mpl",
            "before = tuple(mpl.colormaps)",
            "import wesandersonpy",
            "after = tuple(mpl.colormaps)",
            "assert after == before, (before, after)",
        )
    )

    completed = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr


def test_continuous_colormap_has_expected_type_size_name_and_endpoints() -> None:
    cmap = wes.get_colormap("Royal1", n=17)

    assert isinstance(cmap, LinearSegmentedColormap)
    assert cmap.N == 17
    assert cmap.name == "Royal1"
    assert cmap(0.0) == pytest.approx(to_rgba("#899DA4"))
    assert cmap(1.0) == pytest.approx(to_rgba("#DC863B"))


def test_reversed_continuous_colormap_has_reversed_name_and_endpoints() -> None:
    cmap = wes.get_colormap("Royal1", n=17, reverse=True)

    assert isinstance(cmap, LinearSegmentedColormap)
    assert cmap.name == "Royal1_r"
    assert cmap(0.0) == pytest.approx(to_rgba("#DC863B"))
    assert cmap(1.0) == pytest.approx(to_rgba("#899DA4"))


def test_zissou_continuous_colormap_uses_dedicated_endpoints() -> None:
    cmap = wes.get_colormap("Zissou1", n=11)

    assert cmap(0.0) == pytest.approx(to_rgba("#3A9AB2"))
    assert cmap(1.0) == pytest.approx(to_rgba("#F11B00"))


def test_discrete_colormap_has_expected_type_and_truncation() -> None:
    cmap = wes.get_colormap("Royal1", kind="discrete", n=2)

    assert isinstance(cmap, ListedColormap)
    assert cmap.N == 2
    assert tuple(cmap.colors) == wes.PALETTES["Royal1"][:2]


def test_discrete_colormap_repeats_colors_when_size_exceeds_source() -> None:
    cmap = wes.get_colormap("Royal1", kind="discrete", n=6)

    assert isinstance(cmap, ListedColormap)
    assert tuple(cmap.colors) == (
        *wes.PALETTES["Royal1"],
        *wes.PALETTES["Royal1"][:2],
    )


def test_reversed_discrete_colormap_starts_from_last_source_color() -> None:
    cmap = wes.get_colormap("Royal1", kind="discrete", n=2, reverse=True)

    assert tuple(cmap.colors) == ("#DC863B", "#FAEFD1")


def test_alias_colormap_uses_canonical_name_and_values() -> None:
    alias = wes.get_colormap("Rushmore", n=9)
    canonical = wes.get_colormap("Rushmore1", n=9)

    assert alias.name == "Rushmore1"
    assert alias(0.0) == pytest.approx(canonical(0.0))
    assert alias(0.5) == pytest.approx(canonical(0.5))
    assert alias(1.0) == pytest.approx(canonical(1.0))


def test_unknown_colormap_name_has_available_name_guidance() -> None:
    with pytest.raises(KeyError, match="Available palettes:.*Royal1"):
        wes.get_colormap("NotAPalette")


@pytest.mark.parametrize("name", [None, 1, True])
def test_colormap_name_must_be_a_string(name: object) -> None:
    with pytest.raises(TypeError, match="name must be a string"):
        wes.get_colormap(name)  # type: ignore[arg-type]


@pytest.mark.parametrize("kind", ["categorical", "Continuous", ""])
def test_colormap_kind_must_be_supported(kind: str) -> None:
    with pytest.raises(ValueError, match="kind must be either"):
        wes.get_colormap("Royal1", kind=kind)  # type: ignore[arg-type]


@pytest.mark.parametrize("count", [True, 1.5, "3", None])
def test_colormap_count_must_be_an_integer(count: object) -> None:
    with pytest.raises(TypeError, match="n must be a positive integer"):
        wes.get_colormap("Royal1", n=count)  # type: ignore[arg-type]


@pytest.mark.parametrize("count", [0, -1])
def test_colormap_count_must_be_positive(count: int) -> None:
    with pytest.raises(ValueError, match="n must be at least 1"):
        wes.get_colormap("Royal1", n=count)


@pytest.mark.parametrize("reverse", [1, 0, "yes", None])
def test_colormap_reverse_must_be_boolean(reverse: object) -> None:
    with pytest.raises(TypeError, match="reverse must be a bool"):
        wes.get_colormap("Royal1", reverse=reverse)  # type: ignore[arg-type]


def test_register_colormaps_registers_all_canonical_names(
    registry_prefix: str,
) -> None:
    expected = tuple(f"{registry_prefix}.{name}" for name in wes.available_palettes())

    registered = wes.register_colormaps(prefix=registry_prefix)

    assert registered == expected
    assert all(name in mpl.colormaps for name in expected)
    assert all(
        isinstance(mpl.colormaps[name], LinearSegmentedColormap)
        for name in expected
    )


def test_registration_conflict_is_detected_before_any_write(
    registry_prefix: str,
) -> None:
    requested = tuple(f"{registry_prefix}.{name}" for name in wes.available_palettes())
    conflicting_name = requested[1]
    foreign = ListedColormap(["#010101"], name="foreign")
    mpl.colormaps.register(foreign, name=conflicting_name)

    with pytest.raises(ValueError, match="Cannot register existing"):
        wes.register_colormaps(prefix=registry_prefix)

    assert requested[0] not in mpl.colormaps
    assert conflicting_name in mpl.colormaps
    assert all(name not in mpl.colormaps for name in requested[2:])


def test_force_registration_replaces_existing_non_builtin_colormap(
    registry_prefix: str,
) -> None:
    requested = tuple(f"{registry_prefix}.{name}" for name in wes.available_palettes())
    first_name = requested[0]
    foreign = ListedColormap(["#010101"], name="foreign")
    mpl.colormaps.register(foreign, name=first_name)

    with pytest.warns(UserWarning, match="Overwriting"):
        registered = wes.register_colormaps(prefix=registry_prefix, force=True)

    assert registered == requested
    assert mpl.colormaps[first_name](0.0) == pytest.approx(
        wes.get_colormap(wes.available_palettes()[0])(0.0)
    )


@pytest.mark.parametrize("prefix", [None, True, 1])
def test_registration_prefix_must_be_a_string(prefix: object) -> None:
    with pytest.raises(TypeError, match="prefix must be a string"):
        wes.register_colormaps(prefix=prefix)  # type: ignore[arg-type]


@pytest.mark.parametrize("prefix", ["", " ", " leading", "trailing "])
def test_registration_prefix_must_be_nonempty_and_trimmed(prefix: str) -> None:
    with pytest.raises(ValueError, match="prefix must be a non-empty string"):
        wes.register_colormaps(prefix=prefix)


@pytest.mark.parametrize("force", [None, 0, 1, "yes"])
def test_registration_force_must_be_boolean(force: object) -> None:
    with pytest.raises(TypeError, match="force must be a bool"):
        wes.register_colormaps(force=force)  # type: ignore[arg-type]
