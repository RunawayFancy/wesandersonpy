"""Palette lookup and Matplotlib integration."""

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Literal, TypeAlias

import matplotlib as mpl
from matplotlib.colors import Colormap, LinearSegmentedColormap, ListedColormap, to_hex

from ._palette_data import ALIASES, CONTINUOUS_SEEDS, PALETTE_DATA

PaletteKind: TypeAlias = Literal["discrete", "continuous"]

PALETTES: Mapping[str, tuple[str, ...]] = MappingProxyType(dict(PALETTE_DATA))
"""Canonical palette names mapped to immutable hexadecimal color tuples."""


def available_palettes() -> tuple[str, ...]:
    """Return canonical palette names in stable upstream source order."""

    return tuple(PALETTES)


def get_palette(
    name: str,
    n: int | None = None,
    *,
    kind: PaletteKind = "discrete",
    reverse: bool = False,
) -> tuple[str, ...]:
    """Return colors from a named palette.

    Args:
        name: Canonical palette name or the ``Rushmore`` compatibility alias.
        n: Number of colors. If omitted, return the full source palette (or
            continuous interpolation seed). A discrete request cannot exceed
            the number of colors in its source palette.
        kind: ``"discrete"`` for source colors or ``"continuous"`` for RGB
            interpolation.
        reverse: Reverse the complete palette before selecting or interpolating.

    Raises:
        TypeError: If ``name`` is not a string or ``n`` is not an integer.
        KeyError: If ``name`` is not a known palette or alias.
        ValueError: If ``kind`` or ``n`` is invalid, or if a discrete request
            asks for more colors than the source palette contains.
    """

    canonical_name = _canonical_name(name)
    _validate_kind(kind)
    _validate_reverse(reverse)

    source = PALETTES[canonical_name]
    if kind == "continuous":
        source = CONTINUOUS_SEEDS.get(canonical_name, source)

    count = len(source) if n is None else _validate_n(n)
    colors = source[::-1] if reverse else source

    if kind == "discrete":
        if count > len(colors):
            raise ValueError(
                f"Palette {canonical_name!r} offers {len(colors)} discrete colors; "
                f"received n={count}. Use kind='continuous' to interpolate."
            )
        return colors[:count]

    return _interpolate(colors, count, name=_colormap_name(canonical_name, reverse))


def get_colormap(
    name: str,
    *,
    kind: PaletteKind = "continuous",
    n: int = 256,
    reverse: bool = False,
) -> Colormap:
    """Create a Matplotlib colormap without registering global state.

    Continuous colormaps interpolate through all source colors. Discrete
    colormaps use Matplotlib's public ``ListedColormap`` resampling behavior:
    a smaller ``n`` truncates the list and a larger ``n`` repeats it.
    """

    canonical_name = _canonical_name(name)
    _validate_kind(kind)
    _validate_reverse(reverse)
    count = _validate_n(n)
    cmap_name = _colormap_name(canonical_name, reverse)

    source = PALETTES[canonical_name]
    if kind == "continuous":
        source = CONTINUOUS_SEEDS.get(canonical_name, source)
    if reverse:
        source = source[::-1]

    if kind == "discrete":
        return ListedColormap(source, name=cmap_name, N=count)
    return LinearSegmentedColormap.from_list(cmap_name, source, N=count)


def register_colormaps(
    *,
    prefix: str = "wesandersonpy",
    force: bool = False,
) -> tuple[str, ...]:
    """Register every canonical palette as a continuous Matplotlib colormap.

    Registration names use ``"<prefix>.<palette>"``. The operation is
    explicit: importing :mod:`wesandersonpy` never changes Matplotlib's global
    colormap registry. With ``force=False``, any existing requested name causes
    a ``ValueError`` before registration begins; ``force=True`` replaces
    non-built-in registrations according to Matplotlib's public API.

    Returns:
        The registered Matplotlib names in stable palette order.
    """

    if not isinstance(prefix, str):
        raise TypeError(f"prefix must be a string, got {type(prefix).__name__}")
    if not prefix or prefix.strip() != prefix:
        raise ValueError(
            "prefix must be a non-empty string without surrounding whitespace"
        )
    if not isinstance(force, bool):
        raise TypeError(f"force must be a bool, got {type(force).__name__}")

    registered_names = tuple(f"{prefix}.{name}" for name in available_palettes())
    if not force:
        conflicts = tuple(name for name in registered_names if name in mpl.colormaps)
        if conflicts:
            rendered = ", ".join(repr(name) for name in conflicts)
            raise ValueError(
                f"Cannot register existing Matplotlib colormap name(s): {rendered}. "
                "Pass force=True to replace non-built-in registrations."
            )

    for palette_name, registered_name in zip(
        available_palettes(), registered_names, strict=True
    ):
        mpl.colormaps.register(
            get_colormap(palette_name),
            name=registered_name,
            force=force,
        )

    return registered_names


def _canonical_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError(f"name must be a string, got {type(name).__name__}")

    canonical_name = ALIASES.get(name, name)
    if canonical_name not in PALETTES:
        choices = ", ".join(available_palettes())
        raise KeyError(f"Unknown palette {name!r}. Available palettes: {choices}")
    return canonical_name


def _validate_kind(kind: str) -> None:
    if kind not in ("discrete", "continuous"):
        raise ValueError("kind must be either 'discrete' or 'continuous'")


def _validate_n(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"n must be a positive integer, got {type(n).__name__}")
    if n < 1:
        raise ValueError(f"n must be at least 1, got {n}")
    return n


def _validate_reverse(reverse: bool) -> None:
    if not isinstance(reverse, bool):
        raise TypeError(f"reverse must be a bool, got {type(reverse).__name__}")


def _colormap_name(canonical_name: str, reverse: bool) -> str:
    return f"{canonical_name}_r" if reverse else canonical_name


def _interpolate(colors: tuple[str, ...], n: int, *, name: str) -> tuple[str, ...]:
    if n == 1:
        return (colors[0],)

    cmap = LinearSegmentedColormap.from_list(name, colors, N=n)
    return tuple(to_hex(cmap(index / (n - 1)), keep_alpha=False) for index in range(n))


# R-compatible positional calls such as ``wes_palette("Royal1", 3)`` work,
# while the Python API's explicit ``kind`` keyword remains authoritative.
wes_palette = get_palette


__all__ = [
    "PALETTES",
    "available_palettes",
    "get_colormap",
    "get_palette",
    "register_colormaps",
    "wes_palette",
]
