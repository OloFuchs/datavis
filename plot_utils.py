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


def plot_data(csv_path: Path, plot_params: list[PlotParameters], save_title: str = None, start_stop_time: tuple[int, int] | None = None) -> None:

    try:
        # read CSV as panda
        log = pd.read_csv(csv_path,skiprows=[1])
        print(log.keys())
        
        # crop log for smaller plot
        if start_stop_time is not None:
            save_title += "_"+str(start_stop_time[0]) + "_" + str(start_stop_time[1])
            log = time_filter(log,start_stop_time[0],start_stop_time[1])
            

    # Check if there is only one plot to make or multiple
        if len(plot_params) == 1:
            fig, axs = plt.subplots(len(plot_params), layout='constrained')
            axs = [axs]  # Wrap it in a list to make it iterable in the loop
        else:
            fig, axs = plt.subplots(len(plot_params), 1, layout='constrained')
        
        title = ""

        for idx, params in enumerate(plot_params):
            title += str(params.y_label)
            for motor in params.motor_ids:
                field = params.field_name
                message = params.message_name
                window = params.rolling_window
                motor_field_name = f"MOTOR_{motor.upper()}_ROLLING_{field.upper()}"
                source_column_name = f"CAN1.MOTOR_{motor.upper()}_{field.upper()}.{message.upper()}"
                if source_column_name in log.columns:
                    log[motor_field_name] = log[source_column_name].rolling(window, center=True).mean() * params.scaling_factor
                    axs[idx].plot(log["timestamps"], log[motor_field_name], label=f"{motor.upper()}")
                else:
                    print(f"Column {source_column_name} not found in the log.")
            axs[idx].set_ylabel(params.y_label)
            axs[idx].legend()

        if save_title is not None:

            figures_path = csv_path.parent.parent / "figures"
            figures_path.mkdir(parents=True, exist_ok=True)
            file_path = figures_path / save_title

            plt.savefig(file_path)

        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def plot_data_new(csv_path: Path, plot_params: list, save_title: str = None, start_stop_time: tuple[int, int] | None = None) -> None:

    try:
        # read CSV as panda
        log = pd.read_csv(csv_path, skiprows=[1])
        print(log.keys())
        
        # crop log for smaller plot
        if start_stop_time is not None:
            save_title += "_" + str(start_stop_time[0]) + "_" + str(start_stop_time[1])
            log = time_filter(log, start_stop_time[0], start_stop_time[1])

        # Create subplots
        fig, axs = plt.subplots(len(plot_params), 1, layout='constrained')

        for idx, item in enumerate(plot_params):
            params_list = item if isinstance(item, list) else [item]
            ax = axs[idx] if len(plot_params) > 1 else axs

            for params in params_list:
                title = params.y_label
                for motor in params.ids:
                    field = params.field_name
                    message = params.message_name
                    window = params.rolling_window
                    motor_field_name = f"{motor.upper()}_ROLLING_{field.upper()}"
                    source_column_name = f"CAN1.{motor.upper()}_{field.upper()}.{message.upper()}"
                    if source_column_name in log.columns:
                        log[motor_field_name] = log[source_column_name].rolling(window, center=True).mean() * params.scaling_factor
                        ax.plot(log["timestamps"], log[motor_field_name], label=f"{motor.upper()}")
                    else:
                        print(f"Column {source_column_name} not found in the log.")
                ax.set_ylabel(title)
                ax.legend()

        if save_title is not None:
            figures_path = csv_path.parent.parent / "figures"
            figures_path.mkdir(parents=True, exist_ok=True)
            file_path = figures_path / save_title
            plt.savefig(file_path)

        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def plot_data_test(csv_path: Path, plot_params: list, save_title: str = None, start_stop_time: tuple[int, int] | None = None) -> None:
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
            fig, axs = plt.subplots(len(plot_params), layout='constrained')
            axs = [axs]  # Wrap it in a list to make it iterable in the loop
        else:
            fig, axs = plt.subplots(len(plot_params), 1, layout='constrained')

        for idx, item in enumerate(plot_params):
            params_list = item if isinstance(item, list) else [item]
            ax = axs[idx] if len(plot_params) > 1 else axs
            title = ""
            for params in params_list:
                title += f"{params.y_label.upper()} "
                (fields, labels) = build_plot_param(params)

                for idy, field in enumerate(fields):
                    motor_field_name = f"{field}_ROLLING"
                    if field in log.columns:
                        log[motor_field_name] = log[field].rolling(params.window, center=True).mean() * params.scaling_factor
                        print(labels[idy])
                        ax.plot(log["timestamps"], log[motor_field_name], label=labels[idy])
                    else:
                        print(f"Column {field} not found in the log.")
                ax.set_ylabel(title)
                ax.legend()                  

                print(fields)

        plt.show()

        return log

    except Exception as e:
        print(f"An error occurred: {e}")


def build_plot_param(params: PlotParameters) -> list:
    # Assign default ids based on field_name if field_ids is None
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
            string = f"CAN1.{params.field_name.upper()}_{id.upper()}_{params.message_type.upper()}.{params.message_name.upper()}"
            plot_params_list.append(string)

    return (plot_params_list, params.field_ids)
