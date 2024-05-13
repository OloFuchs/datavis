from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from datavis.utils import time_filter


@dataclass
class PlotParameters:
    message_name: str
    message_type: str
    field_name: str
    y_label: str
    legend: str = None
    field_ids: list[str] = None
    window: int = 50
    scaling_factor: float = 1.0
    opacity: int = 1

    def copy(self, **kwargs):
        new_message_name = kwargs.get("message_name", self.message_name)
        new_message_type = kwargs.get("message_type", self.message_type)
        new_field_name = kwargs.get("field_name", self.field_name)
        new_y_label = kwargs.get("y_label", self.y_label)
        new_legend = kwargs.get("legend", self.legend)
        new_field_ids = kwargs.get("field_ids", self.field_ids)
        new_window = kwargs.get("window", self.window)
        new_scaling_factor = kwargs.get("scaling_factor", self.scaling_factor)
        new_opacity = kwargs.get("opacity", self.opacity)

        return PlotParameters(
            message_name=new_message_name,
            message_type=new_message_type,
            field_name=new_field_name,
            y_label=new_y_label,
            legend=new_legend,
            field_ids=new_field_ids,
            window=new_window,
            scaling_factor=new_scaling_factor,
            opacity=new_opacity,
        )


def plot_data(
    data_input: Path | pd.DataFrame,
    plot_params: list,
    plot_title: str = " ",
    y_label: str = " ",
    save_title: str = None,
    start_stop_time: tuple[int, int] | None = None,
    show_plot: bool = False,
    figsize: tuple[float, float] = (12, 8),
    figure_root: Path | None = None,
) -> None:
    if figure_root is not None:
        figure_path = figure_root / "figures"
    elif isinstance(data_input, Path):
        figure_path = data_input.parent.parent / "figures"
    else:
        raise ValueError("Figure Root is required if data_input ---")

    try:
        # Check if data_input is a path (str or Path) or a DataFrame
        if isinstance(data_input, (str, Path)):
            # Read CSV as pandas DataFrame
            log = pd.read_csv(data_input, skiprows=[1])
        elif isinstance(data_input, pd.DataFrame):
            # Directly use the DataFrame
            log = data_input
        else:
            raise ValueError(
                "Invalid input: data_input must be either a path to a CSV file or a pandas DataFrame."
            )
        print(log.keys())

        # crop log for smaller plot
        if start_stop_time is not None:
            # save_title += "_" + str(start_stop_time[0]) + "_" + str(start_stop_time[1])
            log = time_filter(log, start_stop_time[0], start_stop_time[1])

        # Create subplots
        if len(plot_params) == 1:
            fig, ax = plt.subplots(
                1, layout="constrained", figsize=figsize
            )  # Create a single subplot
            axs = [ax]  # Wrap it in a list to make it iterable in the loop
        else:
            fig, axs = plt.subplots(
                len(plot_params), 1, layout="constrained", figsize=figsize
            )
            # fig, axs = plt.subplots(len(plot_params), 1, layout='constrained')
            axs = (
                axs.ravel()
            )  # Ensure axs is always a flat list, even with multiple subplots

        for idx, item in enumerate(plot_params):
            params_list = item if isinstance(item, list) else [item]
            ax = axs[idx]  # Access the correct axis from the list
            title = ""
            for params in params_list:
                title += f"{params.y_label.upper()} "
                (fields, labels) = build_plot_param(params)
                # print(fields)
                print(f"param name: {params.message_name}")
                for idy, field in enumerate(fields):
                    motor_field_name = f"{field}_ROLLING"
                    legend = f"{params.field_ids[idy]} {params.legend}"
                    if field in log.columns:
                        log[motor_field_name] = (
                            log[field].rolling(params.window, center=True).mean()
                            * params.scaling_factor
                        )
                        ax.plot(
                            log["timestamps"],
                            log[motor_field_name],
                            label=legend,
                            alpha=params.opacity,
                        )
                    else:
                        print(f"Column {field} not found in the log.")
                # ax.set_ylabel(title)
                ax.legend()
        plt.xlabel("time (s)")
        fig.suptitle(plot_title)

        if save_title:
            figure_path.mkdir(parents=True, exist_ok=True)
            save_path = figure_path / f"{save_title}.png"
            print(f"saved: {save_path}")
            plt.savefig(save_path)
        if show_plot:
            plt.show()

        return log

    except Exception as e:
        print(f"An error occurred: {e}")


def build_plot_param(params: PlotParameters) -> list:
    # Assign default ids based on field_name if field_ids is None
    # print(params.field_ids)
    if params.field_ids is None:
        if params.field_name.upper() == "MOTOR":
            params.field_ids = ["A", "B", "C", "D"]
        elif params.field_name.upper() == "PTO":
            params.field_ids = ["0"]
        elif params.field_name.upper() == "PENDANT":
            params.field_ids = ["pendant"]  # Set field_ids to empty list for PENDANT
        elif params.field_name.upper() == "AMIGA_STATUS":
            params.field_ids = ["amiga"]
        elif params.message_type.upper() == "MATH":
            params.field_ids = ["A", "B", "C", "D"]

    # Build the list of strings based on the given parameters
    plot_params_list = []
    if params.field_name.upper() == "PENDANT":
        # Handle PENDANT specifically without IDs
        plot_params_list.append(
            f"CAN1.PENDANT_{params.message_type.upper()}.{params.message_name.upper()}"
        )
    elif params.field_name.upper() == "AMIGA_STATUS":
        plot_params_list.append(
            f"CAN1.{params.field_name.upper()}_{params.message_type.upper()}.{params.message_name.upper()}"
        )
    elif params.message_type.upper() == "MATH":
        for id in params.field_ids:
            plot_params_list.append(f"{params.field_name}_{id.upper()}")
    else:
        for id in params.field_ids:
            # print(f"ID: {id}")
            string = (
                f"CAN1.{params.field_name.upper()}"
                + f"_{id.upper()}_{params.message_type.upper()}.{params.message_name.upper()}"
            )
            plot_params_list.append(string)
    # print(params.field_ids)
    # print(plot_params_list)
    return (plot_params_list, params.field_ids)
