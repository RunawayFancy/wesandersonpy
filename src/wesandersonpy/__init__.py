"""Wes Anderson-inspired color palettes for Python and Matplotlib."""

from .palettes import (
    PALETTES,
    available_palettes,
    get_colormap,
    get_palette,
    register_colormaps,
    wes_palette,
)

__version__ = "0.1.0"

__all__ = [
    "PALETTES",
    "__version__",
    "available_palettes",
    "get_colormap",
    "get_palette",
    "register_colormaps",
    "wes_palette",
]
