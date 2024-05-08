from plot_utils import plot_data
import params
import pandas as pd
from pathlib import Path

csv_path = Path("logs/24-04-24-jacobs-new-spreader/csv/resample.csv")

panda_log = plot_data(data_input=csv_path,
                      plot_params=[[params.pto_rpm, params.amiga_tpdo_linear_params, params.amiga_tpdo_omega_params]],
                      plot_title="05-01-2024 Compost Spreading",
                      save_title="tpdo1_velocities",
                      show_plot=True)

# panda_log = plot_data(csv_path,show_plot=True,plot_params=[[motor_tpdo1_rpm_params,motor_rpdo1_rpm_params]])
# window_size = 50


# a_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["A"],window=window_size)
# a_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["A"],window=window_size)
# b_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["B"],window=window_size)
# b_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["B"],window=window_size)
# c_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["C"],window=window_size)
# c_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["C"],window=window_size)
# d_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["D"],window=window_size)
# d_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["D"],window=window_size)
# panda_log = plot_data(data_input=csv_path,
#                       plot_params=[[params.amiga_tpdo_linear_params, params.amiga_tpdo_omega_params,params.pto_status],[a_rpdo, a_tpdo],[b_rpdo, b_tpdo],[c_rpdo, c_tpdo],[d_rpdo, d_tpdo],params.motor_tpdo1_current_params],
#                       plot_title="Sluggish Cultivator",
#                       save_title="post-flash",
#                       show_plot=True)