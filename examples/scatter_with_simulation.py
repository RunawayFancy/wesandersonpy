"""Compare synthetic scatter layers with illustrative simulation-style traces.

The fixture values are artificial, non-experimental, and not outputs from a
physical simulation.  The words "experiment" and "simulation" are retained
only as visual layer labels from the plotting case.
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
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data" / "scatter_simulation"
DEFAULT_OUTPUT = SCRIPT_DIR / "figures" / "generated" / "scatter_with_simulation.png"


def load_rows(
    data_dir: Path, filename: str, required_columns: set[str]
) -> list[dict[str, str]]:
    """Load one fixed synthetic fixture and validate provenance and schema."""
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


def panel_label(ax: Axes, label: str) -> None:
    ax.text(-0.14, 1.02, label, transform=ax.transAxes, fontsize=10, weight="bold")


def draw_branch_panel(
    ax: Axes,
    branches: list[dict[str, str]],
    outliers: list[dict[str, str]],
    source_colors: dict[str, str],
) -> None:
    markers = {"simulation": "o", "experiment": "D"}
    sizes = {"simulation": 9, "experiment": 7}
    for branch in dict.fromkeys(row["branch"] for row in branches):
        for source in ("simulation", "experiment"):
            selected = [
                row
                for row in branches
                if row["branch"] == branch and row["source"] == source
            ]
            selected.sort(key=lambda row: int(row["point_id"]))
            ax.scatter(
                [float(row["n_g"]) for row in selected],
                [float(row["n_r_crit"]) for row in selected],
                s=sizes[source],
                marker=markers[source],
                color=source_colors[source],
                alpha=0.9,
            )
    ax.scatter(
        [float(row["n_g"]) for row in outliers],
        [float(row["n_r_crit"]) for row in outliers],
        s=6,
        marker="D",
        color=source_colors["experiment"],
        alpha=0.78,
    )

    handles = [
        Line2D(
            [],
            [],
            linestyle="none",
            marker=markers[source],
            markersize=4,
            color=source_colors[source],
            label=source.title(),
        )
        for source in ("simulation", "experiment")
    ]
    ax.legend(
        handles=handles,
        frameon=False,
        loc="lower center",
        bbox_to_anchor=(0.5, 1.01),
        ncol=2,
        fontsize=8.5,
        handletextpad=0.45,
        columnspacing=1.4,
    )
    ax.set(ylabel=r"$n_{r,\mathrm{crit}}$", ylim=(280, 1650))
    panel_label(ax, "(a)")


def draw_probability_panel(
    ax: Axes,
    rows: list[dict[str, str]],
    panel: str,
    source_colors: dict[str, str],
) -> None:
    selected_panel = [row for row in rows if row["panel"] == panel]
    simulation = [row for row in selected_panel if row["source"] == "simulation"]
    experiment = [row for row in selected_panel if row["source"] == "experiment"]
    ax.scatter(
        [float(row["n_g"]) for row in simulation],
        [float(row["p0"]) for row in simulation],
        s=10,
        marker="o",
        color=source_colors["simulation"],
        label="Simulation",
    )
    ax.scatter(
        [float(row["n_g"]) for row in experiment],
        [float(row["p0"]) for row in experiment],
        s=7,
        marker="D",
        color=source_colors["experiment"],
        alpha=0.78,
        label="Experiment",
    )
    if panel == "b":
        highlight = [
            row for row in selected_panel if row["source"] == "highlight_simulation"
        ]
        highlight.sort(key=lambda row: float(row["n_g"]))
        ax.plot(
            [float(row["n_g"]) for row in highlight],
            [float(row["p0"]) for row in highlight],
            color=source_colors["highlight_simulation"],
            linewidth=1.5,
        )
        ax.plot(
            [0.075, 0.099],
            [0.12, 0.12],
            color=source_colors["highlight_simulation"],
            linewidth=1.5,
        )
        ax.text(
            0.104,
            0.12,
            "Highlighted synthetic trace",
            color=source_colors["highlight_simulation"],
            fontsize=6.8,
            va="center",
        )
    else:
        ax.legend(frameon=False, loc="lower center", ncol=2, fontsize=7)
    ax.set(ylabel="$P_0$", ylim=(-0.04, 1.04), yticks=(0, 1))
    panel_label(ax, f"({panel})")


def build_figure(data_dir: Path = DATA_DIR) -> Figure:
    """Build the deterministic three-panel scatter comparison."""
    branches = load_rows(
        data_dir,
        "panel_a_branches.csv",
        {"branch", "source", "point_id", "n_g", "n_r_crit", "data_origin"},
    )
    outliers = load_rows(
        data_dir,
        "panel_a_outliers.csv",
        {"outlier_group", "point_id", "n_g", "n_r_crit", "data_origin"},
    )
    probabilities = load_rows(
        data_dir,
        "panels_bc_probabilities.csv",
        {"panel", "source", "replicate_id", "n_g", "p0", "data_origin"},
    )

    palette = wes.get_palette("AsteroidCity2")
    source_colors = {
        "simulation": palette[5],
        "experiment": palette[4],
        "highlight_simulation": palette[0],
    }
    figure, axes = plt.subplots(
        3,
        1,
        figsize=(6.2, 7.4),
        sharex=True,
        gridspec_kw={"height_ratios": (2.6, 1.0, 1.0), "hspace": 0.18},
    )
    draw_branch_panel(axes[0], branches, outliers, source_colors)
    draw_probability_panel(axes[1], probabilities, "b", source_colors)
    draw_probability_panel(axes[2], probabilities, "c", source_colors)
    for ax in axes:
        ax.set_xlim(0, 0.25)
        ax.tick_params(direction="in", top=True, right=True)
    axes[0].set_xlabel("$n_g$", labelpad=3)
    axes[0].tick_params(labelbottom=True)
    axes[1].tick_params(labelbottom=False)
    axes[2].set_xlabel("$n_g$")
    figure.text(
        0.5,
        0.01,
        "Synthetic demonstration data: layer names do not imply measurement validity",
        ha="center",
        fontsize=7.5,
        style="italic",
    )
    figure.subplots_adjust(bottom=0.09, left=0.16, right=0.97, top=0.93)
    return figure


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DATA_DIR,
        help=f"Directory containing the three expected CSV files (default: {DATA_DIR})",
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
        for filename in (
            "panel_a_branches.csv",
            "panel_a_outliers.csv",
            "panels_bc_probabilities.csv",
        )
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
