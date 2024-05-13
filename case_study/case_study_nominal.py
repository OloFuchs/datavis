from pathlib import Path

import datavis.params as params
import pandas as pd
from datavis.plot_utils import plot_data

csv_path = Path("logs/24-04-15-jacobs-compost-warehouse/csv/resample.csv")

log = pd.read_csv(csv_path, skiprows=[1])

lin_ang_pto = [
    params.pto_rpm,
    params.amiga_tpdo_linear_params,
    params.amiga_tpdo_omega_params,
]
# motor_power = [params.motor_tpdo2_motor_power_params,]
motor_batt = params.motor_tpd02_batt_power_params.copy(opacity=0.5)
batt_power = [params.motor_tpd02_batt_power_params, params.pto_power_params]
temp = [params.motor_temp_params]

print(log.keys())
motors = ["A", "B", "C", "D"]
for motor in motors:
    voltage_str = f"CAN1.MOTOR_{motor}_TPDO1.VOLTAGE"
    current_str = f"CAN1.MOTOR_{motor}_TPDO1.CURRENT"
    power_str = f"MOTOR_POWER_{motor}"
    log[power_str] = log[voltage_str] * log[current_str] / 10000000

print(log.keys())
panda_log = plot_data(
    data_input=log,
    plot_params=[
        [params.amiga_tpdo_linear_params, params.amiga_tpdo_omega_params],
        params.calc_motor_power_params,
        params.motor_temp_params,
    ],
    plot_title="04-15-2024 Nominal at Warehouse",
    figure_root=csv_path.parent.parent,
    save_title="nomial_power_temp",
    show_plot=True,
)
