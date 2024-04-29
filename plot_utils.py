from __future__ import annotations
from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import time_filter
from pathlib import Path

@dataclass
class PlotParameters:
    message_name: str
    message_type: str
    field_name: str
    y_label: str
    field_ids: list[str] = None
    window: int = 50
    scaling_factor: float = 1.0

def plot_data(csv_path: Path, plot_params: list, save_title: str = None, start_stop_time: tuple[int, int] | None = None) -> None:
    try:
        # read CSV as panda
        log = pd.read_csv(csv_path, skiprows=[1])
        print(log.keys())
        
        # crop log for smaller plot
        if start_stop_time is not None:
            # save_title += "_" + str(start_stop_time[0]) + "_" + str(start_stop_time[1])
            log = time_filter(log, start_stop_time[0], start_stop_time[1])

        # Create subplots
        if len(plot_params) == 1:
            fig, ax = plt.subplots(1, layout='constrained')  # Create a single subplot
            axs = [ax]  # Wrap it in a list to make it iterable in the loop
        else:
            fig, axs = plt.subplots(len(plot_params), 1, layout='constrained')
            axs = axs.ravel()  # Ensure axs is always a flat list, even with multiple subplots

        for idx, item in enumerate(plot_params):
            params_list = item if isinstance(item, list) else [item]
            ax = axs[idx]  # Access the correct axis from the list
            title = ""
            for params in params_list:
                title += f"{params.y_label.upper()} "
                (fields, labels) = build_plot_param(params)

                for idy, field in enumerate(fields):
                    motor_field_name = f"{field}_ROLLING"
                    if field in log.columns:
                        log[motor_field_name] = log[field].rolling(params.window, center=True).mean() * params.scaling_factor
                        ax.plot(log["timestamps"], log[motor_field_name], label=labels[idy])
                    else:
                        print(f"Column {field} not found in the log.")
                ax.set_ylabel(title)
                ax.legend()            
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
            params.field_ids = [f"{params.message_name}"]  # Set field_ids to empty list for PENDANT
        elif params.field_name.upper() == "AMIGA_STATUS":
            params.field_ids = [f"{params.message_name}"]

    # Build the list of strings based on the given parameters
    plot_params_list = []
    if params.field_name.upper() == "PENDANT":
        # Handle PENDANT specifically without IDs
        plot_params_list.append(f"CAN1.PENDANT_{params.message_type.upper()}.{params.message_name.upper()}")
    elif params.field_name.upper() == "AMIGA_STATUS":
        plot_params_list.append(f"CAN1.{params.field_name.upper()}_{params.message_type.upper()}.{params.message_name.upper()}")
    else:
        for id in params.field_ids:
            # print(f"ID: {id}")
            string = f"CAN1.{params.field_name.upper()}_{id.upper()}_{params.message_type.upper()}.{params.message_name.upper()}"
            plot_params_list.append(string)
    # print(params.field_ids)
    return (plot_params_list, params.field_ids)
