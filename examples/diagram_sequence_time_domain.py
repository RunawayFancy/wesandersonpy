"""Render a sequence/time-domain demonstration from synthetic CSV fixtures.

The plotted values are artificial, non-experimental, and unsuitable for
scientific inference.  By default, this script reads the verified fixtures
stored beside it under ``data/diagram_sequence``.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

import wesandersonpy as wes

if TYPE_CHECKING:
    from collections.abc import Iterable

    from matplotlib.axes import Axes
    from matplotlib.figure import Figure


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data" / "diagram_sequence"
DEFAULT_OUTPUT = (
    SCRIPT_DIR / "figures" / "generated" / "diagram_sequence_time_domain.png"
)


def load_rows(
    data_dir: Path, filename: str, required_columns: set[str]
) -> list[dict[str, str]]:
    """Read one fixed synthetic fixture and validate its column names."""
    path = data_dir / filename
    with path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        columns = set(reader.fieldnames or ())
        missing = required_columns - columns
        if missing:
            names = ", ".join(sorted(missing))
            raise ValueError(f"{path.name} is missing required columns: {names}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path.name} contains no rows")
    return rows


def draw_panel_label(ax: Axes, label: str) -> None:
    ax.text(-0.12, 1.02, label, transform=ax.transAxes, fontsize=11, weight="bold")


def draw_sequence(
    ax: Axes,
    rows: Iterable[dict[str, str]],
    colors: tuple[str, ...],
) -> None:
    channel_y = {"transmon": 1.0, "resonator": 0.0}
    channel_colors = {"transmon": colors[0], "resonator": colors[4]}
    ink = colors[3]

    for channel, y_position in channel_y.items():
        color = channel_colors[channel]
        ax.hlines(y_position, 0.0, 14.0, color=color, linewidth=1.3)
        ax.text(
            -0.25,
            y_position,
            channel.title(),
            color=color,
            ha="right",
            va="center",
        )

    for row in rows:
        start = float(row["start_arb"])
        end = float(row["end_arb"])
        amplitude = float(row["amplitude_arb"])
        baseline = channel_y[row["channel"]]
        color = channel_colors[row["channel"]]
        filled = row["render_role"] != "outline_pulse"
        pulse = Rectangle(
            (start, baseline),
            end - start,
            amplitude,
            facecolor=color if filled else "none",
            edgecolor=color,
            linewidth=1.2,
            alpha=0.35 if filled else 1.0,
        )
        ax.add_patch(pulse)
        ax.text(
            (start + end) / 2,
            baseline + amplitude + 0.12,
            row["label"],
            color=ink,
            ha="center",
            va="bottom",
            fontsize=8,
        )

    ax.set_xlim(-2.0, 14.2)
    ax.set_ylim(-0.35, 2.25)
    ax.axis("off")
    draw_panel_label(ax, "(a)")


def draw_time_response(
    ax: Axes,
    rows: list[dict[str, str]],
    colors: tuple[str, ...],
) -> None:
    time = [float(row["time_us"]) for row in rows]
    data = [float(row["data_normalized"]) for row in rows]
    comparison = [float(row["fit_normalized"]) for row in rows]
    data_color = colors[4]

    ax.plot(time, comparison, color=data_color, linewidth=7, alpha=0.22, label="Guide")
    ax.plot(time, data, "o", color=data_color, markersize=3.4, label="Synthetic points")
    for guide in (0.0, 2.0):
        ax.axvline(guide, color=colors[2], linewidth=0.9, alpha=0.7)
    ax.set(
        xlabel="Time, $t$ (microseconds)",
        ylabel="Normalized response",
        ylim=(-0.05, 1.12),
    )
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    draw_panel_label(ax, "(b)")


def draw_level_sketch(ax: Axes, color: str, label: str) -> None:
    x_start, x_end = 0.81, 0.89
    for index, y_position in enumerate((0.63, 0.70, 0.77, 0.84)):
        ax.plot(
            [x_start, x_end],
            [y_position, y_position],
            transform=ax.transAxes,
            color=color,
        )
        ax.text(
            x_end + 0.015,
            y_position,
            str(index),
            transform=ax.transAxes,
            color=color,
            fontsize=6,
            va="center",
        )
    ax.annotate(
        "",
        xy=(0.85, 0.81),
        xytext=(0.85, 0.65),
        xycoords=ax.transAxes,
        arrowprops={
            "arrowstyle": "->",
            "color": color,
            "connectionstyle": "arc3,rad=-0.3",
        },
    )
    ax.text(0.76, 0.91, label, transform=ax.transAxes, color=color, fontsize=8)


def draw_population_panel(
    ax: Axes,
    rows: list[dict[str, str]],
    preparation: str,
    state_colors: dict[str, str],
    panel_label: str,
    show_legend: bool,
) -> None:
    selected = [row for row in rows if row["preparation"] == preparation]
    for state, color in state_colors.items():
        state_rows = [row for row in selected if row["state"] == state]
        x_values = [float(row["nbar_r_max"]) for row in state_rows]
        y_values = [float(row["population"]) for row in state_rows]
        ax.plot(
            x_values,
            y_values,
            "o",
            color=color,
            markersize=3.2,
            label=f"${state}$",
        )

    ax.axvline(900, color=state_colors["P9plus"], linestyle=":", linewidth=1.0)
    ax.set_xlim(-80, 2900)
    ax.set_ylim(-0.025, 1.0)
    ax.set_ylabel("Population")
    draw_panel_label(ax, panel_label)
    if show_legend:
        ax.legend(
            frameon=False,
            loc="lower left",
            bbox_to_anchor=(0.0, 1.01),
            ncol=5,
            borderaxespad=0,
            fontsize=8,
        )
        inset = ax.inset_axes([0.08, 0.10, 0.31, 0.29])
        for state, color in state_colors.items():
            if state == "P1":
                continue
            state_rows = [row for row in selected if row["state"] == state]
            inset.plot(
                [float(row["nbar_r_max"]) for row in state_rows],
                [float(row["population"]) for row in state_rows],
                "o",
                color=color,
                markersize=2,
            )
        inset.set(xlim=(-80, 2900), ylim=(-0.002, 0.055))
        inset.tick_params(labelsize=6)
        mark_inset(
            ax,
            inset,
            loc1=2,
            loc2=4,
            fc="none",
            ec=state_colors["P2"],
            linewidth=0.7,
        )

    prepared_state = "1" if preparation == "state_1" else "7"
    sketch_color = (
        state_colors["P1"] if preparation == "state_1" else state_colors["P7"]
    )
    draw_level_sketch(ax, sketch_color, f"Prepare $|{prepared_state}\\rangle$")


def build_figure(data_dir: Path = DATA_DIR) -> Figure:
    """Build the deterministic four-panel figure."""
    sequence_rows = load_rows(
        data_dir,
        "sequence_events.csv",
        {
            "channel",
            "event",
            "start_arb",
            "end_arb",
            "amplitude_arb",
            "render_role",
            "label",
        },
    )
    time_rows = load_rows(
        data_dir,
        "time_domain_response.csv", {"time_us", "data_normalized", "fit_normalized"}
    )
    population_rows = load_rows(
        data_dir,
        "population_sweeps.csv", {"preparation", "state", "nbar_r_max", "population"}
    )

    colors = wes.get_palette("Zissou1")
    state_colors = {
        "P1": colors[4],
        "P2": colors[0],
        "P7": colors[1],
        "P8": colors[3],
        "P9plus": colors[2],
    }
    figure, axes = plt.subplots(
        4,
        1,
        figsize=(7.2, 10.2),
        gridspec_kw={"height_ratios": (0.8, 1.0, 1.45, 1.45), "hspace": 0.34},
    )
    draw_sequence(axes[0], sequence_rows, colors)
    draw_time_response(axes[1], time_rows, colors)
    draw_population_panel(
        axes[2], population_rows, "state_1", state_colors, "(c)", True
    )
    draw_population_panel(
        axes[3], population_rows, "state_7", state_colors, "(d)", False
    )
    axes[2].tick_params(labelbottom=False)
    axes[3].set_xlabel(r"Illustrative control parameter, $\bar{n}_{r,\max}$")
    figure.text(
        0.5,
        0.01,
        "Synthetic demonstration data: not experimental measurements",
        ha="center",
        fontsize=8,
        style="italic",
    )
    figure.subplots_adjust(bottom=0.07, left=0.16, right=0.96, top=0.97)
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
            "sequence_events.csv",
            "time_domain_response.csv",
            "population_sweeps.csv",
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
