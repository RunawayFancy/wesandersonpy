"""Render a multi-parameter fidelity-style plot from synthetic CSV fixtures.

All values are artificial and non-experimental.  They demonstrate layout and
color-map usage only; they are not measured, fitted, or scientifically valid.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt

import wesandersonpy as wes

if TYPE_CHECKING:
    from matplotlib.figure import Figure


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data" / "fidelity_multi_parameter"
DEFAULT_OUTPUT = SCRIPT_DIR / "figures" / "generated" / "fidelity_multi_parameter.png"


def load_rows(
    data_dir: Path, filename: str, required_columns: set[str]
) -> list[dict[str, str]]:
    """Load one fixed fixture and require its synthetic provenance marker."""
    path = data_dir / filename
    with path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        missing = required_columns - set(reader.fieldnames or ())
        if missing:
            names = ", ".join(sorted(missing))
            raise ValueError(f"{path.name} is missing required columns: {names}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path.name} contains no rows")
    if any(row["data_origin"] != "synthetic_non_experimental" for row in rows):
        raise ValueError(
            f"{path.name} does not contain the expected synthetic provenance marker"
        )
    return rows


def build_figure(data_dir: Path = DATA_DIR) -> Figure:
    """Build the deterministic logarithmic fidelity-style figure."""
    curves = load_rows(
        data_dir,
        "fidelity_curves.csv",
        {"parameter_j", "x_scaled", "marker_fidelity", "line_fidelity", "data_origin"},
    )
    asymptotes = load_rows(
        data_dir,
        "fidelity_asymptotes.csv",
        {"parameter_j", "x_start", "x_end", "asymptote_fidelity", "data_origin"},
    )

    parameter_order = (1, 2, 3, 4, 8)
    markers = {1: "o", 2: "s", 3: "v", 4: "^", 8: "o"}
    palette = wes.get_palette("Cavalcanti1")
    colors = {
        1: palette[4],
        2: palette[1],
        3: palette[2],
        4: palette[0],
        8: palette[3],
    }

    figure, ax = plt.subplots(figsize=(5.4, 4.4))
    for parameter in parameter_order:
        selected = [row for row in curves if int(row["parameter_j"]) == parameter]
        x_values = [float(row["x_scaled"]) for row in selected]
        marker_values = [float(row["marker_fidelity"]) for row in selected]
        line_values = [float(row["line_fidelity"]) for row in selected]
        marker_face = "none" if parameter == 8 else colors[parameter]
        ax.plot(x_values, line_values, color=colors[parameter], linewidth=0.95)
        ax.plot(
            x_values,
            marker_values,
            linestyle="none",
            marker=markers[parameter],
            markersize=4.2,
            markerfacecolor=marker_face,
            markeredgecolor=colors[parameter],
            markeredgewidth=0.9,
            label=f"$j={parameter}$",
        )

        guide = next(row for row in asymptotes if int(row["parameter_j"]) == parameter)
        ax.hlines(
            float(guide["asymptote_fidelity"]),
            float(guide["x_start"]),
            float(guide["x_end"]),
            color=colors[parameter],
            linestyle=":",
            linewidth=0.95,
        )

    ax.set_xscale("log")
    ax.set(
        xlabel=r"$2\pi/(\Omega T)$",
        ylabel="Fidelity",
        xlim=(0.055, 110),
        ylim=(-0.025, 1.025),
    )
    ax.legend(
        frameon=False,
        loc="lower left",
        fontsize=9,
        labelspacing=0.25,
        handletextpad=0.5,
        borderpad=0.2,
    )
    figure.text(
        0.5,
        0.015,
        "Synthetic demonstration data: not experimental measurements",
        ha="center",
        fontsize=7.5,
        style="italic",
    )
    figure.subplots_adjust(bottom=0.18, left=0.16, right=0.97, top=0.97)
    return figure


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DATA_DIR,
        help=f"Directory containing the two expected CSV files (default: {DATA_DIR})",
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
    input_paths = {
        (args.data_dir / filename).resolve()
        for filename in ("fidelity_curves.csv", "fidelity_asymptotes.csv")
    }
    if args.output.resolve() in input_paths:
        raise ValueError("--output must not overwrite an input CSV")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    figure = build_figure(args.data_dir)
    try:
        figure.savefig(args.output, dpi=180)
    finally:
        plt.close(figure)
    print(f"Saved synthetic demonstration figure to {args.output}")


if __name__ == "__main__":
    main()
