"""Render a synthetic readout-calibration and Rabi-style composite figure.

Every plotted value is artificial and non-experimental.  The figure recreates
plotting grammar only and makes no measurement, calibration, or physical-validity
claim.  Inputs default to ``data/readout_calibration_rabi`` beside this script.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

import wesandersonpy as wes

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data" / "readout_calibration_rabi"
DEFAULT_OUTPUT = (
    SCRIPT_DIR
    / "figures"
    / "generated"
    / "readout_calibration_rabi_subplots.png"
)


def load_rows(
    data_dir: Path, filename: str, required_columns: set[str]
) -> list[dict[str, str]]:
    """Load one fixed synthetic fixture and validate its schema."""
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
    return rows


def panel_label(ax: Axes, label: str) -> None:
    ax.text(-0.13, 1.03, label, transform=ax.transAxes, fontsize=11, weight="bold")


def draw_pulse_train(
    ax: Axes,
    x_start: float,
    x_end: float,
    baseline: float,
    amplitude: float,
    repeat_count: int,
    color: str,
) -> None:
    """Draw a square-pulse train from normalized schematic parameters."""
    period = (x_end - x_start) / repeat_count
    x_values = [x_start]
    y_values = [baseline]
    for index in range(repeat_count):
        left = x_start + index * period
        right = left + 0.55 * period
        x_values.extend((left, left, right, right, left + period))
        y_values.extend(
            (
                baseline,
                baseline + amplitude,
                baseline + amplitude,
                baseline,
                baseline,
            )
        )
    ax.plot(x_values, y_values, color=color, linewidth=1.1)


def draw_sequence(
    ax: Axes,
    rows: list[dict[str, str]],
    role_colors: dict[str, str],
) -> None:
    for row in rows:
        x0, y0 = float(row["x0"]), float(row["y0"])
        x1, y1 = float(row["x1"]), float(row["y1"])
        color = role_colors[row["color_role"]]
        kind = row["kind"]
        if kind == "pulse_train":
            draw_pulse_train(
                ax,
                x0,
                x1,
                y0,
                float(row["amplitude"]),
                int(row["repeat_count"]),
                color,
            )
        elif kind == "line":
            ax.plot((x0, x1), (y0, y1), color=color, linewidth=1.4)
        elif kind == "arrow":
            ax.annotate(
                "",
                xy=(x1, y1),
                xytext=(x0, y0),
                arrowprops={"arrowstyle": "->", "color": color},
            )
        elif kind == "meander":
            points = 100
            x_values = [
                x0 + (x1 - x0) * index / (points - 1)
                for index in range(points)
            ]
            y_values = [
                y0
                + (y1 - y0) * index / (points - 1)
                + float(row["amplitude"])
                * math.sin(2 * math.pi * 6 * index / (points - 1))
                for index in range(points)
            ]
            ax.plot(x_values, y_values, color=color, linewidth=1.2)
        elif kind == "cross":
            center_x = (x0 + x1) / 2
            center_y = (y0 + y1) / 2
            half_width = (x1 - x0) / 2
            half_height = (y1 - y0) / 2
            ax.plot(
                (center_x - half_width, center_x + half_width),
                (center_y, center_y),
                color=color,
                linewidth=1.3,
            )
            ax.plot(
                (center_x, center_x),
                (center_y - half_height, center_y + half_height),
                color=color,
                linewidth=1.3,
            )
        if row["label"]:
            ax.text(x0, y0 + 0.10, row["label"], color=color, fontsize=7)
    ax.set(xlim=(0, 0.72), ylim=(-0.02, 1.12))
    ax.axis("off")
    panel_label(ax, "(a)")


def draw_tone_response(
    magnitude_ax: Axes,
    phase_ax: Axes,
    rows: list[dict[str, str]],
    ink: str,
) -> None:
    colormap = wes.get_colormap("GrandBudapest1", kind="continuous")
    for state in range(8, -1, -1):
        state_rows = [row for row in rows if int(row["state"]) == state]
        state_rows.sort(key=lambda row: float(row["detuning_mhz"]))
        x_values = [float(row["detuning_mhz"]) for row in state_rows]
        magnitude = [float(row["magnitude_abs_s11"]) for row in state_rows]
        phase = [float(row["phase_rad"]) for row in state_rows]
        color = colormap((8 - state) / 8)
        magnitude_ax.plot(x_values, magnitude, color=color, linewidth=1.0)
        phase_ax.plot(x_values, phase, color=color, linewidth=1.0)
        minimum_index = magnitude.index(min(magnitude))
        magnitude_ax.text(
            x_values[minimum_index],
            magnitude[minimum_index] - 0.10,
            f"$|{state}\\rangle$",
            color=color,
            fontsize=6,
            ha="center",
        )

    for guide, label in ((-0.75, "Tone I"), (0.0, "Tone II"), (0.5, "Tone III")):
        phase_ax.axvline(guide, color=ink, linestyle=":", linewidth=0.7, alpha=0.55)
        phase_ax.text(guide, -0.89, label, color=ink, fontsize=6, ha="center")
    magnitude_ax.set(ylabel=r"$|S_{11}|$", xlim=(-1.5, 1.0), ylim=(3.0, 5.0))
    phase_ax.set(
        xlabel="Tone detuning (MHz)",
        ylabel=r"$\angle S_{11}$",
        xlim=(-1.5, 1.0),
        ylim=(-1.55, -0.85),
    )
    magnitude_ax.tick_params(labelbottom=False)
    panel_label(magnitude_ax, "(b)")


def draw_iq_panels(
    axes: list[Axes],
    rows: list[dict[str, str]],
    role_colors: dict[str, str],
) -> None:
    panels = zip(axes, ("left", "middle", "right"), strict=True)
    for index, (ax, panel) in enumerate(panels):
        panel_rows = [row for row in rows if row["iq_panel"] == panel]
        background = [row for row in panel_rows if row["point_role"] == "background"]
        ax.scatter(
            [float(row["i_mv"]) for row in background],
            [float(row["q_mv"]) for row in background],
            color=role_colors["neutral"],
            s=6,
            alpha=0.28,
        )
        states = dict.fromkeys(
            row["state"]
            for row in panel_rows
            if row["point_role"] == "cluster"
        )
        for state in states:
            cluster = [
                row
                for row in panel_rows
                if row["point_role"] == "cluster" and row["state"] == state
            ]
            color = role_colors[cluster[0]["color_role"]]
            x_values = [float(row["i_mv"]) for row in cluster]
            y_values = [float(row["q_mv"]) for row in cluster]
            ax.scatter(x_values, y_values, color=color, s=20, alpha=0.58)
            ax.text(
                sum(x_values) / len(x_values),
                sum(y_values) / len(y_values),
                f"$|{state}\\rangle$",
                color=color,
                fontsize=7,
                weight="bold",
            )
        ax.set(xlim=(-1.5, 0.9), ylim=(-1.0, 1.1))
        ax.set_xticks([])
        ax.set_yticks([])
        if index == 0:
            ax.set_ylabel("Q (mV)")
            panel_label(ax, "(c)")
        ax.set_xlabel("I (mV)")


def draw_energy_ladder(ax: Axes, color: str, state: str) -> None:
    inset = ax.inset_axes([0.85, 0.13, 0.12, 0.73])
    for index, y_position in enumerate((0.15, 0.38, 0.61, 0.84)):
        inset.hlines(y_position, 0.1, 0.7, color=color, linewidth=0.8)
        inset.text(0.76, y_position, str(index), color=color, fontsize=5, va="center")
    inset.annotate(
        "",
        xy=(0.4, 0.79),
        xytext=(0.4, 0.19),
        arrowprops={"arrowstyle": "->", "color": color, "linewidth": 0.8},
    )
    inset.text(0.04, 0.95, f"$|{state}\\rangle$", color=color, fontsize=6)
    inset.axis("off")


def draw_population_rows(
    axes: list[Axes],
    rows: list[dict[str, str]],
    role_colors: dict[str, str],
) -> None:
    case_states = {"case_a": "2", "case_b": "4", "case_c": "7"}
    for index, (ax, drive_case) in enumerate(
        zip(axes, ("case_a", "case_b", "case_c"), strict=True)
    ):
        case_rows = [row for row in rows if row["drive_case"] == drive_case]
        for state in dict.fromkeys(row["state"] for row in case_rows):
            state_rows = [row for row in case_rows if row["state"] == state]
            state_rows.sort(key=lambda row: float(row["duration_ns"]))
            role = state_rows[0]["color_role"]
            dominant = state_rows[0]["trace_role"] == "dominant"
            color = role_colors[role]
            ax.plot(
                [float(row["duration_ns"]) for row in state_rows],
                [float(row["population"]) for row in state_rows],
                marker="o",
                markersize=2.7 if dominant else 2.0,
                linewidth=1.1 if dominant else 0.7,
                color=color,
                alpha=0.95 if dominant else 0.38,
            )
        ax.axhline(1.0, color=role_colors["neutral"], linestyle=":", linewidth=0.6)
        ax.set(ylabel="$P$", xlim=(0, 800), ylim=(-0.05, 1.08), yticks=(0, 1))
        ax.tick_params(labelbottom=False)
        state = case_states[drive_case]
        draw_energy_ladder(ax, role_colors[case_rows[-1]["color_role"]], state)
        if index == 0:
            panel_label(ax, "(d)")


def draw_spin_row(
    ax: Axes,
    rows: list[dict[str, str]],
    role_colors: dict[str, str],
) -> None:
    for component in ("Jx", "Jy", "Jz"):
        component_rows = [row for row in rows if row["component"] == component]
        color = role_colors[component_rows[0]["color_role"]]
        ax.plot(
            [float(row["duration_ns"]) for row in component_rows],
            [float(row["expectation_j_units"]) for row in component_rows],
            marker="o",
            markersize=2.8,
            linewidth=1.0,
            color=color,
            label=f"${component}$",
        )
    ax.set(
        xlabel="Pulse duration (ns)",
        ylabel=r"$\langle J\rangle$",
        xlim=(0, 800),
        ylim=(-3.5, 3.5),
        yticks=(-3.5, 0, 3.5),
        yticklabels=(r"$-7/2$", "0", r"$7/2$"),
    )
    ax.legend(frameon=False, loc="lower left", ncol=3, fontsize=6)

    sphere = ax.inset_axes([0.85, 0.10, 0.12, 0.78])
    sphere.add_patch(
        Circle(
            (0.5, 0.5),
            0.37,
            fill=False,
            color=role_colors["neutral"],
            linewidth=0.7,
        )
    )
    for destination, role in (
        ((0.80, 0.70), "coral"),
        ((0.30, 0.80), "teal"),
        ((0.50, 0.93), "sage"),
    ):
        sphere.annotate(
            "",
            xy=destination,
            xytext=(0.5, 0.5),
            arrowprops={"arrowstyle": "->", "color": role_colors[role]},
        )
    sphere.set(xlim=(0, 1), ylim=(0, 1), aspect="equal")
    sphere.axis("off")


def build_figure(data_dir: Path = DATA_DIR) -> Figure:
    """Build the deterministic four-region composite."""
    sequence = load_rows(
        data_dir,
        "sequence_primitives.csv",
        {
            "primitive_id",
            "group",
            "kind",
            "x0",
            "y0",
            "x1",
            "y1",
            "amplitude",
            "repeat_count",
            "color_role",
            "label",
        },
    )
    tone = load_rows(
        data_dir,
        "tone_response.csv",
        {"state", "detuning_mhz", "magnitude_abs_s11", "phase_rad"},
    )
    iq_rows = load_rows(
        data_dir,
        "iq_scatter.csv",
        {"iq_panel", "state", "point_id", "i_mv", "q_mv", "color_role", "point_role"},
    )
    populations = load_rows(
        data_dir,
        "rabi_populations.csv",
        {
            "drive_case",
            "state",
            "duration_ns",
            "population",
            "color_role",
            "trace_role",
        },
    )
    spin = load_rows(
        data_dir,
        "spin_expectations.csv",
        {"component", "duration_ns", "expectation_j_units", "color_role"},
    )

    palette = wes.get_palette("Zissou1")
    ink = wes.get_palette("Moonrise1")[-1]
    role_colors = {
        "ink": ink,
        "neutral": ink,
        "coral": palette[4],
        "teal": palette[0],
        "sage": palette[1],
        "orange": palette[3],
    }

    figure = plt.figure(figsize=(11.0, 9.2))
    outer = figure.add_gridspec(3, 1, height_ratios=(1.25, 0.8, 2.5), hspace=0.28)
    top = outer[0].subgridspec(1, 2, width_ratios=(0.9, 1.4), wspace=0.28)
    sequence_ax = figure.add_subplot(top[0, 0])
    tone_grid = top[0, 1].subgridspec(2, 1, hspace=0.03)
    magnitude_ax = figure.add_subplot(tone_grid[0, 0])
    phase_ax = figure.add_subplot(tone_grid[1, 0], sharex=magnitude_ax)

    iq_grid = outer[1].subgridspec(1, 3, wspace=0.06)
    iq_axes = [figure.add_subplot(iq_grid[0, index]) for index in range(3)]
    duration_grid = outer[2].subgridspec(4, 1, hspace=0.06)
    duration_axes = [figure.add_subplot(duration_grid[index, 0]) for index in range(4)]

    draw_sequence(sequence_ax, sequence, role_colors)
    draw_tone_response(magnitude_ax, phase_ax, tone, ink)
    draw_iq_panels(iq_axes, iq_rows, role_colors)
    draw_population_rows(duration_axes[:3], populations, role_colors)
    draw_spin_row(duration_axes[3], spin, role_colors)

    figure.text(
        0.5,
        0.01,
        (
            "Synthetic demonstration data: not experimental measurements "
            "or calibrated results"
        ),
        ha="center",
        fontsize=8,
        style="italic",
    )
    figure.subplots_adjust(bottom=0.07, left=0.09, right=0.97, top=0.97)
    return figure


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DATA_DIR,
        help=f"Directory containing the five expected CSV files (default: {DATA_DIR})",
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
            "sequence_primitives.csv",
            "tone_response.csv",
            "iq_scatter.csv",
            "rabi_populations.csv",
            "spin_expectations.csv",
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
