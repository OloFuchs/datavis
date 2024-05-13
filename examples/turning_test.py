from pathlib import Path

import pandas as pd
import params
from plot_utils import plot_data

csv_path = Path("logs/05-13-24-warehouse-turning-test-2/csv/resample.csv")

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

# complete log
# panda_log = plot_data(data_input=csv_path,
#                       plot_params=[[params.amiga_tpdo_linear_params,params.amiga_tpdo_omega_params],params.motor_tpdo1_current_params,params.motor_temp_params],
#                       plot_title="04-15-2024 Nominal Turns at Warehouse",
#                       save_title="nomial_power_temp",
#                       show_plot=True)

# turn in place
# panda_log = plot_data(data_input=csv_path,
#                       plot_params=[[params.amiga_tpdo_linear_params,params.amiga_tpdo_omega_params],params.motor_tpdo1_current_params,params.motor_temp_params],
#                       start_stop_time=[0,120],
#                       plot_title="04-15-2024 Nominal Turns at Warehouse",
#                       save_title="turn_in_place",
#                       show_plot=True)

# 24 inch radius
# panda_log = plot_data(data_input=csv_path,
#                       plot_params=[[params.amiga_tpdo_linear_params,params.amiga_tpdo_omega_params],params.motor_tpdo1_current_params,params.motor_temp_params],
#                       start_stop_time=[120,210],
#                       plot_title="04-15-2024 Nominal Turns at Warehouse",
#                       save_title="24_radius",
#                       show_plot=True)

# 48 inch radius
panda_log = plot_data(
    data_input=csv_path,
    plot_params=[
        [params.amiga_tpdo_linear_params, params.amiga_tpdo_omega_params],
        params.motor_tpdo1_current_params,
        params.motor_temp_params,
    ],
    start_stop_time=[205, 300],
    plot_title="04-15-2024 Nominal Turns at Warehouse",
    save_title="48_radius",
    show_plot=True,
)
