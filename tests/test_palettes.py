"""Behavioral tests for palette selection and interpolation."""

from __future__ import annotations

import pytest

import wesandersonpy as wes

ZISSOU_CONTINUOUS_SEED = (
    "#3a9ab2",
    "#6fb2c1",
    "#91bab6",
    "#a5c2a3",
    "#bdc881",
    "#dccb4e",
    "#e3b710",
    "#e79805",
    "#ec7a05",
    "#ef5703",
    "#f11b00",
)


def test_discrete_palette_uses_source_order_and_requested_count() -> None:
    assert wes.get_palette("Royal1", 2) == ("#899DA4", "#C93312")
    assert wes.get_palette("Royal1") == wes.PALETTES["Royal1"]


def test_discrete_palette_reverses_before_selecting() -> None:
    assert wes.get_palette("Royal1", 2, reverse=True) == ("#DC863B", "#FAEFD1")


def test_rushmore_alias_matches_canonical_palette() -> None:
    assert wes.get_palette("Rushmore") == wes.get_palette("Rushmore1")
    assert wes.get_palette("Rushmore", 3, reverse=True) == wes.get_palette(
        "Rushmore1", 3, reverse=True
    )


def test_zissou_continuous_palette_uses_the_dedicated_seed() -> None:
    colors = wes.get_palette("Zissou1", kind="continuous")

    assert colors == ZISSOU_CONTINUOUS_SEED
    assert colors[0] != wes.PALETTES["Zissou1"][0].lower()
    assert colors[-1] != wes.PALETTES["Zissou1"][-1].lower()


@pytest.mark.parametrize("count", [1, 2, 7, 32])
def test_continuous_palette_returns_requested_count(count: int) -> None:
    assert len(wes.get_palette("Royal1", count, kind="continuous")) == count


def test_continuous_interpolation_preserves_endpoints() -> None:
    colors = wes.get_palette("Royal1", 9, kind="continuous")

    assert colors[0] == wes.PALETTES["Royal1"][0].lower()
    assert colors[-1] == wes.PALETTES["Royal1"][-1].lower()


def test_continuous_interpolation_reverses_endpoints() -> None:
    colors = wes.get_palette("Royal1", 9, kind="continuous", reverse=True)

    assert colors[0] == wes.PALETTES["Royal1"][-1].lower()
    assert colors[-1] == wes.PALETTES["Royal1"][0].lower()


def test_single_continuous_color_is_first_selected_endpoint() -> None:
    colors = wes.get_palette("Royal1", 1, kind="continuous")
    reversed_colors = wes.get_palette("Royal1", 1, kind="continuous", reverse=True)

    assert colors == ("#899DA4",)
    assert reversed_colors == ("#DC863B",)


def test_discrete_request_cannot_exceed_source_palette() -> None:
    with pytest.raises(ValueError, match="offers 4 discrete colors"):
        wes.get_palette("Royal1", 5)


@pytest.mark.parametrize("name", ["royal1", "NotAPalette", ""])
def test_unknown_palette_has_available_name_guidance(name: str) -> None:
    with pytest.raises(KeyError, match="Available palettes:.*Royal1"):
        wes.get_palette(name)


@pytest.mark.parametrize("name", [None, 1, True])
def test_palette_name_must_be_a_string(name: object) -> None:
    with pytest.raises(TypeError, match="name must be a string"):
        wes.get_palette(name)  # type: ignore[arg-type]


@pytest.mark.parametrize("kind", ["categorical", "CONTINUOUS", ""])
def test_palette_kind_must_be_supported(kind: str) -> None:
    with pytest.raises(ValueError, match="kind must be either"):
        wes.get_palette("Royal1", kind=kind)  # type: ignore[arg-type]


@pytest.mark.parametrize("count", [True, 1.5, "3"])
def test_palette_count_must_be_an_integer(count: object) -> None:
    with pytest.raises(TypeError, match="n must be a positive integer"):
        wes.get_palette("Royal1", count)  # type: ignore[arg-type]


@pytest.mark.parametrize("count", [0, -1])
def test_palette_count_must_be_positive(count: int) -> None:
    with pytest.raises(ValueError, match="n must be at least 1"):
        wes.get_palette("Royal1", count)


@pytest.mark.parametrize("reverse", [1, 0, "yes", None])
def test_palette_reverse_must_be_boolean(reverse: object) -> None:
    with pytest.raises(TypeError, match="reverse must be a bool"):
        wes.get_palette("Royal1", reverse=reverse)  # type: ignore[arg-type]


def test_wes_palette_compatibility_alias_supports_positional_count() -> None:
    assert wes.wes_palette is wes.get_palette
    assert wes.wes_palette("Royal1", 3) == wes.get_palette("Royal1", 3)
