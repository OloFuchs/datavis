from __future__ import annotations
from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

@dataclass
class PlotParameters:
    message_name: str
    field_name: str
    y_label: str
    motor_ids: list[str] = field(default_factory=lambda: ["A", "B", "C", "D"])
    rolling_window: int = 50
    scaling_factor: float = 1.0

def plot_data(log: pd.DataFrame, plot_params: list[PlotParameters]) -> None:
    # Check if there is only one plot to make or multiple
    if len(plot_params) == 1:
        fig, axs = plt.subplots(len(plot_params), layout='constrained')
        axs = [axs]  # Wrap it in a list to make it iterable in the loop
    else:
        fig, axs = plt.subplots(len(plot_params), 1, layout='constrained')
    
    for idx, params in enumerate(plot_params):
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
        
    plt.show()