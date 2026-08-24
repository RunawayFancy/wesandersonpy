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
import numpy as np
from matplotlib.patches import Circle

import wesandersonpy as wes

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data" / "readout_calibration_rabi"
DEFAULT_OUTPUT = (
    SCRIPT_DIR / "figures" / "generated" / "readout_calibration_rabi_subplots.png"
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
    ax.text(-0.12, 1.04, label, transform=ax.transAxes, fontsize=10, weight="bold")


def smooth_path(
    x_values: list[float],
    y_values: list[float],
    *,
    samples_per_interval: int = 18,
) -> tuple[np.ndarray, np.ndarray]:
    """Return a display-only smooth path through the existing synthetic samples."""
    smooth_x: list[float] = []
    smooth_y: list[float] = []
    for index in range(len(x_values) - 1):
        blend_position = np.linspace(
            0.0,
            1.0,
            samples_per_interval,
            endpoint=False,
        )
        blend_weight = (1.0 - np.cos(np.pi * blend_position)) / 2.0
        smooth_x.extend(
            x_values[index] + (x_values[index + 1] - x_values[index]) * blend_position
        )
        smooth_y.extend(
            y_values[index] + (y_values[index + 1] - y_values[index]) * blend_weight
        )
    smooth_x.append(x_values[-1])
    smooth_y.append(y_values[-1])
    return np.asarray(smooth_x), np.asarray(smooth_y)


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
            center_x = (x0 + x1) / 2
            x_values = [
                center_x
                + float(row["amplitude"])
                * math.sin(2 * math.pi * 6 * index / (points - 1))
                for index in range(points)
            ]
            y_values = [
                y0 + (y1 - y0) * index / (points - 1) for index in range(points)
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
        label = row["label"]
        if label:
            label_positions = {
                "Control": (x0, y0 + 0.15, "left"),
                "RO": ((x0 + x1) / 2, y0 + 0.15, "center"),
                "omega": (x1 + 0.02, y1, "left"),
            }
            label_x, label_y, alignment = label_positions[label]
            display_label = r"$\omega$" if label == "omega" else label
            ax.text(
                label_x,
                label_y,
                display_label,
                color=color,
                fontsize=7,
                ha=alignment,
                va="center",
            )
    ax.set(xlim=(0, 0.70), ylim=(-0.02, 1.12))
    ax.axis("off")
    panel_label(ax, "(a)")


def draw_tone_response(
    magnitude_ax: Axes,
    phase_ax: Axes,
    rows: list[dict[str, str]],
    ink: str,
) -> None:
    colormap = wes.get_colormap("GrandBudapest1", kind="continuous")
    state_colors: dict[int, object] = {}
    for state in range(8, -1, -1):
        state_rows = [row for row in rows if int(row["state"]) == state]
        state_rows.sort(key=lambda row: float(row["detuning_mhz"]))
        x_values = [float(row["detuning_mhz"]) for row in state_rows]
        magnitude = [float(row["magnitude_abs_s11"]) for row in state_rows]
        phase = [float(row["phase_rad"]) for row in state_rows]
        color = colormap((8 - state) / 8)
        state_colors[state] = color
        smooth_x, smooth_magnitude = smooth_path(x_values, magnitude)
        _, smooth_phase = smooth_path(x_values, phase)
        magnitude_ax.plot(smooth_x, smooth_magnitude, color=color, linewidth=1.0)
        phase_ax.plot(smooth_x, smooth_phase, color=color, linewidth=1.0)

    key_positions = np.linspace(0.08, 0.92, 9)
    for position, state in zip(key_positions, range(8, -1, -1), strict=True):
        magnitude_ax.text(
            position,
            0.06,
            f"$|{state}\\rangle$",
            transform=magnitude_ax.transAxes,
            color=state_colors[state],
            fontsize=6,
            ha="center",
        )

    for guide, label in ((-0.75, "Tone III"), (0.0, "Tone II"), (0.5, "Tone I")):
        phase_ax.axvline(guide, color=ink, linestyle=":", linewidth=0.7, alpha=0.55)
        phase_ax.text(
            guide,
            0.93,
            label,
            transform=phase_ax.get_xaxis_transform(),
            color=ink,
            fontsize=6,
            ha="center",
            va="top",
        )
    magnitude_ax.set(ylabel=r"$|S_{11}|$", xlim=(-1.5, 1.0), ylim=(3.0, 5.0))
    phase_ax.set(
        xlabel="Tone detuning (MHz)",
        ylabel=r"$\angle S_{11}$",
        xlim=(-1.5, 1.0),
        ylim=(-1.55, -0.85),
    )
    magnitude_ax.tick_params(labelbottom=False)
    magnitude_ax.tick_params(labelsize=7)
    phase_ax.tick_params(labelsize=7)
    panel_label(magnitude_ax, "(b)")


def draw_iq_panels(
    axes: list[Axes],
    rows: list[dict[str, str]],
    role_colors: dict[str, str],
    target_colors: dict[str, str],
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
            row["state"] for row in panel_rows if row["point_role"] == "cluster"
        )
        for state in states:
            cluster = [
                row
                for row in panel_rows
                if row["point_role"] == "cluster" and row["state"] == state
            ]
            color = target_colors.get(
                state,
                role_colors[cluster[0]["color_role"]],
            )
            x_values = [float(row["i_mv"]) for row in cluster]
            y_values = [float(row["q_mv"]) for row in cluster]
            ax.scatter(x_values, y_values, color=color, s=13, alpha=0.68)
            ax.text(
                sum(x_values) / len(x_values),
                sum(y_values) / len(y_values),
                f"$|{state}\\rangle$",
                color=color,
                fontsize=6,
                weight="bold",
            )
        ax.set(xlim=(-1.5, 0.9), ylim=(-1.0, 1.1))
        ax.set_xticks([])
        ax.set_yticks([])
        if index == 0:
            ax.set_ylabel("Q (mV)")
            panel_label(ax, "(c)")
        if index == 1:
            ax.set_xlabel("I (mV)")


def draw_energy_ladder(ax: Axes, color: str, state: str) -> None:
    level_count = int(state) + 2
    level_positions = np.linspace(0.12, 0.82, level_count)
    for index, y_position in enumerate(level_positions):
        ax.hlines(y_position, 0.10, 0.72, color=color, linewidth=0.8)
        ax.text(0.78, y_position, str(index), color=color, fontsize=5, va="center")
    ax.annotate(
        "",
        xy=(0.42, level_positions[-1] - 0.03),
        xytext=(0.42, level_positions[0] + 0.03),
        arrowprops={"arrowstyle": "->", "color": color, "linewidth": 0.9},
    )
    ax.text(0.06, 0.94, f"$|{state}\\rangle$", color=color, fontsize=6)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")


def draw_population_rows(
    axes: list[Axes],
    ladder_axes: list[Axes],
    rows: list[dict[str, str]],
    role_colors: dict[str, str],
    target_colors: dict[str, str],
) -> None:
    case_states = {"case_a": "2", "case_b": "4", "case_c": "7"}
    panel_rows = zip(
        axes,
        ladder_axes,
        ("case_a", "case_b", "case_c"),
        strict=True,
    )
    for index, (ax, ladder_ax, drive_case) in enumerate(panel_rows):
        case_rows = [row for row in rows if row["drive_case"] == drive_case]
        target_state = case_states[drive_case]
        for state in dict.fromkeys(row["state"] for row in case_rows):
            state_rows = [row for row in case_rows if row["state"] == state]
            state_rows.sort(key=lambda row: float(row["duration_ns"]))
            role = state_rows[0]["color_role"]
            dominant = state_rows[0]["trace_role"] == "dominant"
            color = target_colors.get(state, role_colors[role])
            x_values = [float(row["duration_ns"]) for row in state_rows]
            y_values = [float(row["population"]) for row in state_rows]
            smooth_x, smooth_y = smooth_path(x_values, y_values)
            ax.plot(
                smooth_x,
                smooth_y,
                linewidth=1.2 if dominant else 0.75,
                color=color,
                alpha=0.95 if dominant else 0.48,
            )
            ax.plot(
                x_values,
                y_values,
                linestyle="none",
                marker="o",
                markersize=2.6 if dominant else 1.8,
                color=color,
                alpha=0.95 if dominant else 0.55,
            )
        ax.axhline(1.0, color=role_colors["neutral"], linestyle=":", linewidth=0.6)
        ax.set(xlim=(0, 800), ylim=(-0.05, 1.08), yticks=(0, 1))
        ax.tick_params(labelsize=7, labelbottom=False)
        ax.text(
            0.02,
            0.78,
            r"$|0\rangle$",
            transform=ax.transAxes,
            color=role_colors["ink"],
            fontsize=6,
        )
        ax.text(
            0.17,
            0.78,
            f"$|{target_state}\\rangle$",
            transform=ax.transAxes,
            color=target_colors[target_state],
            fontsize=6,
        )
        draw_energy_ladder(
            ladder_ax,
            target_colors[target_state],
            target_state,
        )
        if index == 0:
            panel_label(ax, "(d)")
        if index == 1:
            ax.set_ylabel("Population")


def draw_spin_row(
    ax: Axes,
    annotation_ax: Axes,
    rows: list[dict[str, str]],
    role_colors: dict[str, str],
) -> None:
    for component in ("Jx", "Jy", "Jz"):
        component_rows = [row for row in rows if row["component"] == component]
        color = role_colors[component_rows[0]["color_role"]]
        x_values = [float(row["duration_ns"]) for row in component_rows]
        y_values = [float(row["expectation_j_units"]) for row in component_rows]
        smooth_x, smooth_y = smooth_path(x_values, y_values)
        ax.plot(
            smooth_x,
            smooth_y,
            linewidth=1.1,
            color=color,
            label=f"${component}$",
        )
        ax.plot(
            x_values,
            y_values,
            linestyle="none",
            marker="o",
            markersize=2.6,
            color=color,
        )
    ax.set(
        xlabel="Pulse duration (ns)",
        ylabel=r"$\langle J\rangle$",
        xlim=(0, 800),
        ylim=(-3.5, 3.5),
        yticks=(-3.5, 0, 3.5),
        yticklabels=(r"$-7/2$", "0", r"$7/2$"),
    )
    ax.tick_params(labelsize=7)
    ax.legend(frameon=False, loc="lower left", ncol=3, fontsize=6)

    annotation_ax.add_patch(
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
        annotation_ax.annotate(
            "",
            xy=destination,
            xytext=(0.5, 0.5),
            arrowprops={"arrowstyle": "->", "color": role_colors[role]},
        )
    for position, label, role in (
        ((0.82, 0.72), r"$J_x$", "coral"),
        ((0.20, 0.82), r"$J_y$", "teal"),
        ((0.52, 0.95), r"$J_z$", "sage"),
    ):
        annotation_ax.text(*position, label, color=role_colors[role], fontsize=5)
    annotation_ax.text(0.05, 0.08, "SU(2)", color=role_colors["ink"], fontsize=6)
    annotation_ax.set(xlim=(0, 1), ylim=(0, 1), aspect="equal")
    annotation_ax.axis("off")


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
    muted_green = wes.get_palette("Moonrise2")[0]
    role_colors = {
        "ink": ink,
        "neutral": ink,
        "coral": palette[4],
        "teal": palette[0],
        "sage": muted_green,
        "orange": palette[3],
    }
    target_colors = {
        "2": role_colors["coral"],
        "4": role_colors["teal"],
        "7": role_colors["sage"],
    }
    iq_state_colors = {
        **target_colors,
        "6": role_colors["orange"],
    }

    figure = plt.figure(figsize=(13.6, 6.4))
    outer = figure.add_gridspec(
        1,
        2,
        width_ratios=(1.02, 1.48),
        wspace=0.18,
    )

    calibration_grid = outer[0, 0].subgridspec(
        2,
        1,
        height_ratios=(1.12, 0.78),
        hspace=0.30,
    )
    calibration_top = calibration_grid[0, 0].subgridspec(
        1,
        2,
        width_ratios=(0.78, 1.32),
        wspace=0.34,
    )
    sequence_ax = figure.add_subplot(calibration_top[0, 0])
    tone_grid = calibration_top[0, 1].subgridspec(2, 1, hspace=0.03)
    magnitude_ax = figure.add_subplot(tone_grid[0, 0])
    phase_ax = figure.add_subplot(tone_grid[1, 0], sharex=magnitude_ax)

    iq_grid = calibration_grid[1, 0].subgridspec(1, 3, wspace=0.04)
    iq_axes = [figure.add_subplot(iq_grid[0, index]) for index in range(3)]

    duration_grid = outer[0, 1].subgridspec(
        4,
        2,
        width_ratios=(1.0, 0.19),
        hspace=0.06,
        wspace=0.03,
    )
    duration_axes: list[Axes] = []
    annotation_axes: list[Axes] = []
    for index in range(4):
        shared_axis = duration_axes[0] if duration_axes else None
        duration_axes.append(
            figure.add_subplot(duration_grid[index, 0], sharex=shared_axis)
        )
        annotation_axes.append(figure.add_subplot(duration_grid[index, 1]))

    draw_sequence(sequence_ax, sequence, role_colors)
    draw_tone_response(magnitude_ax, phase_ax, tone, ink)
    draw_iq_panels(iq_axes, iq_rows, role_colors, iq_state_colors)
    draw_population_rows(
        duration_axes[:3],
        annotation_axes[:3],
        populations,
        role_colors,
        target_colors,
    )
    draw_spin_row(duration_axes[3], annotation_axes[3], spin, role_colors)

    figure.text(
        0.5,
        0.025,
        (
            "Synthetic demonstration data: not experimental measurements "
            "or calibrated results"
        ),
        ha="center",
        fontsize=7,
        style="italic",
    )
    figure.subplots_adjust(bottom=0.12, left=0.055, right=0.985, top=0.95)
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
