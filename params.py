from plot_utils import PlotParameters, plot_data
import pandas as pd
from pathlib import Path
from utils import time_filter


motor_velocity_params = PlotParameters(
    message_name="RPM",
    message_type="TPDO1",
    field_name="motor",
    scaling_factor = 0.000715584993317675,
    y_label="velocity (m/s)"
)

pendant_y = PlotParameters(
    message_name="y_pos",
    message_type="tpdo1",
    field_name="pendant",
    y_label="pendant y"
)

pto_status = PlotParameters(
    message_name="status",
    message_type="rpdo1",
    field_name="pto",
    y_label="PTO Status"
)

pto_rpm = PlotParameters(
    message_name="rpm",
    message_type="tpdo1",
    field_name="pto",
    scaling_factor= 1/800,
    legend="pto status",
    y_label="PTO RPM"
)

# motor_current_params = PlotParameters(
#     message_name="CURRENT",
#     field_name="TPDO1",
#     y_label="Current(mA)"
# )

# motor_input_power_params = PlotParameters(
#     message_name = "MOTOR_IN_POWER",
#     field_name = "TPDO2",
#     y_label="Watts(w)"
# )


motor_tpdo1_rpm_params = PlotParameters(
    message_name="RPM",
    message_type="TPDO1",
    field_name="motor",
    # field_ids=["A"],
    legend = "measured",
    y_label="RPM",
)
motor_tpdo1_current_params = PlotParameters(
    message_name="current",
    message_type="TPDO1",
    field_name="motor",
    legend="current",
    y_label="Current (mA)",
)
motor_tpdo1_voltage_params = PlotParameters(
    message_name="voltage",
    message_type="TPDO1",
    field_name="motor",
    # field_ids=["A"],
    y_label="Voltage (Volts)"
)
motor_rpdo1_rpm_params = PlotParameters(
    message_name="RPM",
    message_type="RPDO1",
    field_name="motor",
    # field_ids=["A"],
    legend = "request",
    y_label="RPM",
    opacity=.5,
)
motor_tpdo1_velocity_params = PlotParameters(
    message_name="RPM",
    message_type="TPDO1",
    field_name="motor",
    # field_ids=["A"],
    scaling_factor=0.000715584993317675,
    y_label="Velocity (m/s)",
)

temp_params = PlotParameters(
    message_name="TEMP",
    message_type="SDO",
    field_name="motor",
    y_label="Temperature(c)"
)

batt_power_params = PlotParameters(
    message_type = "TPDO2",
    message_name = "BATT_POWER",
    field_name="motor",
    y_label="POWER(WATTS)",
)

pto_power_params = PlotParameters(
    message_type = "TPDO2",
    message_name = "BATT_POWER",
    field_name="PTO",
    legend="pto battery",
    y_label=" ",
)

amiga_tpdo_linear_params = PlotParameters(
    message_type = "TPDO1",
    message_name = "CURRENT_SPEED",
    field_name="AMIGA_STATUS",
    legend="linear",
    y_label="Linear Velocity",
)

amiga_tpdo_omega_params = PlotParameters(
    message_type = "TPDO1",
    message_name = "CURRENT_OMEGA",
    field_name="AMIGA_STATUS",
    legend="angular",
    y_label="Angular Velocity",
)

calc_battery_current_params = PlotParameters(
    message_name= " ",
    message_type = "MATH",
    field_name="BATTERY_CURRENT",
    y_label="Current (A)",
)

# batt_current_params = PlotParameters(
#     message_name="BATT_CURRENT",
#     field_name="TPDO2",
#     y_label="Current(mA)"
# )

# TPDO = [RPM_params,motor_current_params,voltage_params]
# PTO = []
# rpm = [RPM_params]
# velocity_current_temp = [velocity_params,motor_current_params,temp_params]
# battery = [batt_power_params, voltage_params, batt_current_params]
# rpm_current = [RPM_params, motor_current_params]
# power = [motor_input_power_params, batt_power_params]


# Assuming log data is in a CSV file for this example
# csv_path = Path("logs/24-05-01-jacobs-40amps/00000045/csv/resample.csv")

# panda_log = plot_data(data_input=csv_path,
#                       plot_params=[[motor_tpdo1_rpm_params,motor_rpdo1_rpm_params],batt_power_params,motor_tpdo1_current_params,motor_tpdo1_voltage_params],
#                       show_plot=False)

# # panda_log = plot_data(csv_path,show_plot=True,plot_params=[[motor_tpdo1_rpm_params,motor_rpdo1_rpm_params]])

# print(panda_log.keys())

# panda_log["BATTERY_CURRENT"] = panda_log["CAN1.MOTOR_A_TPDO2.BATT_POWER_ROLLING"] * (1000/panda_log["CAN1.MOTOR_A_TPDO1.VOLTAGE_ROLLING"])

# # print(panda_log.keys())

# panda_log = plot_data(data_input=panda_log,
#                       plot_params=[motor_tpdo1_velocity_params,calc_battery_current_params],
#                       show_plot=True)

# plot_data_test(csv_path,[[motor_velocity_params, pto_rpm], [batt_power_params, pto_power_params], amiga_status_params],save_title="Velocity_Power")

# plot_data([volts_params, mA_params])


## JACBOS CASE STUDY:

# csv_path = Path("logs/24-04-24-jacobs-new-spreader/csv/resample.csv")

# # panda_log = plot_data(data_input=csv_path,
# #                       plot_params=[[pto_rpm,amiga_tpdo_linear_params, amiga_tpdo_omega_params]],
# #                       plot_title="05-01-2024 Compost Spreading",
# #                       save_title="tpdo1_velocities",
# #                       show_plot=True)

# # panda_log = plot_data(csv_path,show_plot=True,plot_params=[[motor_tpdo1_rpm_params,motor_rpdo1_rpm_params]])
# window_size = 50

# a_rpdo = motor_rpdo1_rpm_params.copy(field_ids = ["A"],window=window_size)
# a_tpdo = motor_tpdo1_rpm_params.copy(field_ids = ["A"],window=window_size)
# b_rpdo = motor_rpdo1_rpm_params.copy(field_ids = ["B"],window=window_size)
# b_tpdo = motor_tpdo1_rpm_params.copy(field_ids = ["B"],window=window_size)
# c_rpdo = motor_rpdo1_rpm_params.copy(field_ids = ["C"],window=window_size)
# c_tpdo = motor_tpdo1_rpm_params.copy(field_ids = ["C"],window=window_size)
# d_rpdo = motor_rpdo1_rpm_params.copy(field_ids = ["D"],window=window_size)
# d_tpdo = motor_tpdo1_rpm_params.copy(field_ids = ["D"],window=window_size)
# panda_log = plot_data(data_input=csv_path,
#                       plot_params=[[amiga_tpdo_linear_params, amiga_tpdo_omega_params,pto_status],[a_rpdo, a_tpdo],[b_rpdo, b_tpdo],[c_rpdo, c_tpdo],[d_rpdo, d_tpdo],motor_tpdo1_current_params],
#                       plot_title="Sluggish Cultivator",
#                       save_title="post-flash",
#                       show_plot=True)