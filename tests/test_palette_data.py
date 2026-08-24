"""Parity and immutability checks for the public palette data."""

from __future__ import annotations

import pytest

import wesandersonpy as wes

EXPECTED_PALETTES = {
    "BottleRocket1": (
        "#A42820",
        "#5F5647",
        "#9B110E",
        "#3F5151",
        "#4E2A1E",
        "#550307",
        "#0C1707",
    ),
    "BottleRocket2": ("#FAD510", "#CB2314", "#273046", "#354823", "#1E1E1E"),
    "Rushmore1": ("#E1BD6D", "#EABE94", "#0B775E", "#35274A", "#F2300F"),
    "Royal1": ("#899DA4", "#C93312", "#FAEFD1", "#DC863B"),
    "Royal2": ("#9A8822", "#F5CDB4", "#F8AFA8", "#FDDDA0", "#74A089"),
    "Zissou1": ("#3B9AB2", "#78B7C5", "#EBCC2A", "#E1AF00", "#F21A00"),
    "Darjeeling1": ("#FF0000", "#00A08A", "#F2AD00", "#F98400", "#5BBCD6"),
    "Darjeeling2": ("#ECCBAE", "#046C9A", "#D69C4E", "#ABDDDE", "#000000"),
    "Chevalier1": ("#446455", "#FDD262", "#D3DDDC", "#C7B19C"),
    "FantasticFox1": ("#DD8D29", "#E2D200", "#46ACC8", "#E58601", "#B40F20"),
    "Moonrise1": ("#F3DF6C", "#CEAB07", "#D5D5D3", "#24281A"),
    "Moonrise2": ("#798E87", "#C27D38", "#CCC591", "#29211F"),
    "Moonrise3": ("#85D4E3", "#F4B5BD", "#9C964A", "#CDC08C", "#FAD77B"),
    "Cavalcanti1": ("#D8B70A", "#02401B", "#A2A475", "#81A88D", "#972D15"),
    "GrandBudapest1": ("#F1BB7B", "#FD6467", "#5B1A18", "#D67236"),
    "GrandBudapest2": ("#E6A0C4", "#C6CDF7", "#D8A499", "#7294D4"),
    "IsleofDogs1": (
        "#9986A5",
        "#79402E",
        "#CCBA72",
        "#0F0D0E",
        "#D9D0D3",
        "#8D8680",
    ),
    "IsleofDogs2": ("#EAD3BF", "#AA9486", "#B6854D", "#39312F", "#1C1718"),
    "FrenchDispatch": ("#90D4CC", "#BD3027", "#B0AFA2", "#7FC0C6", "#9D9C85"),
    "AsteroidCity1": ("#0A9F9D", "#CEB175", "#E54E21", "#6C8645", "#C18748"),
    "AsteroidCity2": (
        "#C52E19",
        "#AC9765",
        "#54D8B1",
        "#b67c3b",
        "#175149",
        "#AF4E24",
    ),
    "AsteroidCity3": ("#FBA72A", "#D3D4D8", "#CB7A5C", "#5785C1"),
}


def test_palette_mapping_exactly_matches_upstream_values_and_order() -> None:
    assert tuple(wes.PALETTES) == tuple(EXPECTED_PALETTES)
    assert dict(wes.PALETTES) == EXPECTED_PALETTES


def test_available_palettes_is_stable_and_canonical_only() -> None:
    names = wes.available_palettes()

    assert names == tuple(EXPECTED_PALETTES)
    assert "Rushmore" not in names
    assert "Zissou1Continuous" not in names


def test_palette_mapping_does_not_allow_item_assignment() -> None:
    with pytest.raises(TypeError):
        wes.PALETTES["Royal1"] = ("#000000",)


def test_palette_color_sequences_are_immutable_tuples() -> None:
    colors = wes.PALETTES["Royal1"]

    assert isinstance(colors, tuple)
    with pytest.raises(TypeError):
        colors[0] = "#000000"


def test_palette_lookup_does_not_expose_mutable_data() -> None:
    colors = wes.get_palette("Royal1")

    assert isinstance(colors, tuple)
    assert colors == EXPECTED_PALETTES["Royal1"]
    assert wes.PALETTES["Royal1"] == EXPECTED_PALETTES["Royal1"]
