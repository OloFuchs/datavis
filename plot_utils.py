from __future__ import annotations
from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

@dataclass
class PlotParameters:
    message_name: str
    field_name: str
    motor_ids: list[str] = ["A", "B", "C", "D"]
    rolling_window: int = 1
    scaling_factor:float = 1.0
    y_label: str


def plot_data(log: pd.DataFrame, plot_params: list[PlotParameters]) -> None:

    fig, axs = plt.subplots(len(plot_params), 1, layout='constrained')

    for idx, params in enumerate(plot_params):
        for motor in params.motor_ids:
            field = params.field_name
            message = params.message_name
            window = params.rolling_window
            log[f"MOTOR_{motor.upper()}_ROLLING_{field.upper()}"] = log[f"CAN1.MOTOR_{motor.upper()}_{message.upper()}.{field.upper()}"].rolling(window,center=True).mean()
            axs[idx].plot(log["timestamps"],log[f"MOTOR_{motor.upper()}_ROLLING_{field.upper()}"],label = f"{motor.upper()}")
        axs[idx].legend()
        # And so on


volts_params = PlotParameters(
    message_name="VOLTAGE",
    field_name="TPDO1",
    y_label="Voltage (V)"
)
mA_params = PlotParameters(
    message_name="CURRENT",
    field_name="TPDO1",
    y_label="Current (mA)"
)
RPM_params = PlotParameters(
    scaling_factor = 0.000715584993317675
)

plot_data([volts_params])
plot_data([volts_params, mA_params])