"""Render faded repeated traces from synthetic, non-experimental CSV data.

The values are artificial visualization fixtures and must not be interpreted as
measurements.  The default input is ``data/multiple_iterations`` beside this
script, and the output is not allowed to overwrite the selected input.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import wesandersonpy as wes

if TYPE_CHECKING:
    from matplotlib.figure import Figure


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PATH = SCRIPT_DIR / "data" / "multiple_iterations" / "iteration_populations.csv"
DEFAULT_OUTPUT = SCRIPT_DIR / "figures" / "generated" / "multiple_iterations_faded.png"
REQUIRED_COLUMNS = {"iteration_id", "fade_rank", "series", "nbar_r_max", "population"}


def load_rows(input_path: Path) -> list[dict[str, str]]:
    """Load and validate the fixed synthetic fixture."""
    with input_path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or ())
        if missing:
            names = ", ".join(sorted(missing))
            raise ValueError(f"{input_path.name} is missing required columns: {names}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{input_path.name} contains no rows")
    return rows


def build_figure(input_path: Path = DATA_PATH) -> Figure:
    """Build a deterministic marker-only figure with chronology encoded by alpha."""
    rows = load_rows(input_path)
    series_colors = {
        "P0": wes.get_palette("BottleRocket2")[2],
        "P1": wes.get_palette("Royal1")[1],
        "P7": wes.get_palette("Zissou1")[1],
    }
    series_labels = {"P0": r"$P_0$", "P1": r"$P_1$", "P7": r"$P_7$"}
    guide_color = wes.get_palette("Moonrise2")[2]
    alpha_by_rank = {1: 0.25, 2: 0.42, 3: 0.63, 4: 0.92}

    figure, ax = plt.subplots(figsize=(8.4, 3.3))
    for fade_rank in sorted({int(row["fade_rank"]) for row in rows}):
        for series, color in series_colors.items():
            selected = [
                row
                for row in rows
                if int(row["fade_rank"]) == fade_rank and row["series"] == series
            ]
            ax.plot(
                [float(row["nbar_r_max"]) for row in selected],
                [float(row["population"]) for row in selected],
                linestyle="none",
                marker="o",
                markersize=3.7,
                color=color,
                alpha=alpha_by_rank[fade_rank],
                zorder=fade_rank,
            )

    ax.axvline(
        900,
        color=guide_color,
        linestyle="--",
        linewidth=1.0,
        alpha=0.85,
        zorder=0,
    )
    handles = [
        Line2D(
            [],
            [],
            linestyle="none",
            marker="o",
            color=color,
            label=series_labels[series],
        )
        for series, color in series_colors.items()
    ]
    ax.legend(handles=handles, frameon=False, loc="upper right", ncol=3)
    ax.set(
        xlabel=r"Illustrative control parameter, $\bar{n}_{r,\max}$",
        ylabel="Population",
        xlim=(-80, 2890),
        ylim=(-0.04, 0.94),
    )
    ax.text(-0.055, 1.01, "(a)", transform=ax.transAxes, fontsize=10, weight="bold")
    figure.text(
        0.5,
        0.015,
        "Synthetic demonstration data: not experimental measurements",
        ha="center",
        fontsize=8,
        style="italic",
    )
    figure.subplots_adjust(bottom=0.23, left=0.12, right=0.97, top=0.94)
    return figure


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=DATA_PATH,
        help=f"Synthetic iteration CSV path (default: {DATA_PATH})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Figure path (default: {DEFAULT_OUTPUT})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.output.resolve() == args.input.resolve():
        raise ValueError("--output must not overwrite the input CSV")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    figure = build_figure(args.input)
    try:
        figure.savefig(args.output, dpi=180)
    finally:
        plt.close(figure)
    print(f"Saved synthetic demonstration figure to {args.output}")


if __name__ == "__main__":
    main()
