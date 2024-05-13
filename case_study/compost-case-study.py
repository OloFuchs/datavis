from pathlib import Path

import pandas as pd
import params
from plot_utils import plot_data

csv_path = Path("logs/24-04-24-jacobs-new-spreader/csv/resample.csv")

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

# Plotting linear and algular velocities, temperature in all the motors

# panda_log = plot_data(
#     data_input=csv_path,
#     plot_params=[
#         [
#             params.pto_rpm,
#             params.amiga_tpdo_linear_params,
#             params.amiga_tpdo_omega_params,
#         ],
#         params.motor_temp_params,
#     ],
#     plot_title="04-24-2024 Compost Spreading",
#     save_title="tpdo1_velocities_temp",
#     show_plot=False,
# )

# trial 1

# log = plot_data(
#     data_input=csv_path,
#     plot_params=[
#         lin_ang_pto,
#         params.motor_tpdo1_rpm_params,
#         params.motor_rpdo1_rpm_params,
#         params.motor_tpdo1_current_params,
#         batt_power,
#         temp,
#     ],
#     start_stop_time=[1500, 2300],
#     plot_title="04-24-2024 Compost Spreading Trial 1",
#     save_title="trial_1_power",
#     show_plot=True,
# )
# motor_list = [
#     "CAN1.MOTOR_A_TPDO2.BATT_POWER",
#     "CAN1.MOTOR_B_TPDO2.BATT_POWER",
#     "CAN1.MOTOR_C_TPDO2.BATT_POWER",
#     "CAN1.MOTOR_D_TPDO2.BATT_POWER",
#     "CAN1.PTO_0_TPDO2.BATT_POWER",
# ]
# motor_names = ["A", "B", "C", "D", "PTO"]
# times = [
#     (1570, 1660),
#     (1660, 1795),
#     (1795, 1884),
#     (1884, 2090),
#     (2090, 2182),
#     (2182, 2199),
#     (2200, 2281),
# ]
# labels = ["S1", "T1", "S2", "T2", "S3", "T3", "S4"]

# csv_output = []

# # Prepare the header with motor names
# header = "Label,Time(s)," + ",".join(motor_names)
# csv_output.append(header)

# # Iterate over each time interval and label
# for idx, time in enumerate(times):
#     dt = time[1] - time[0]
#     row = f"{labels[idx]},{dt}"  # Start the row with the label
#     for motor in motor_list:
#         power_integral = utils.int_in_time_range(log, time, motor)  # Calculate the integral
#         row += f",{power_integral:.4f}"  # Append each motor's integral to the row
#     csv_output.append(row)  # Append the row to the output list

# # Print each row as a new line in CSV format
# for line in csv_output:
#     print(line)


# plotting heating event:

# panda_log = plot_data(data_input=csv_path,
#                       plot_params=[lin_ang_pto,params.motor_tpdo1_rpm_params,params.motor_tpdo1_current_params,batt_power,temp],
#                       start_stop_time=[1800,2100],
#                       plot_title="04-24-2024 Compost Spreading",
#                       save_title="overheating_event",
#                       show_plot=True)

# motor_list = [
#     "CAN1.MOTOR_A_TPDO2.BATT_POWER",
#     "CAN1.MOTOR_B_TPDO2.BATT_POWER",
#     "CAN1.MOTOR_C_TPDO2.BATT_POWER",
#     "CAN1.MOTOR_D_TPDO2.BATT_POWER",
# ]
# motor_names = ["A", "B", "C", "D"]
# times = [(1840, 1876), (2022, 2050)]
# labels = ["A Event", "D Event"]

# csv_output = []

# # Prepare the header with motor names
# header = "Label,Time(s)," + ",".join(motor_names)
# csv_output.append(header)

# # Iterate over each time interval and label
# for idx, time in enumerate(times):
#     dt = time[1] - time[0]
#     row = f"{labels[idx]},{dt}"  # Start the row with the labe
#     for motor in motor_list:
#         power_integral = utils.int_in_time_range(log, time, motor)  # Calculate the integral
#         row += f",{power_integral:.4f}"  # Append each motor's integral to the row
#     csv_output.append(row)  # Append the row to the output list

# # Print each row as a new line in CSV format
# for line in csv_output:
#     print(line)


# Trial 2
panda_log = plot_data(
    data_input=csv_path,
    plot_params=[lin_ang_pto, batt_power, temp],
    plot_title="04-24-2024 Compost Spreading Trial 2",
    start_stop_time=[4350, 5050],
    save_title="trial2",
    show_plot=True,
)

# a_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["A"],window=window_size)
# a_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["A"],window=window_size)
# b_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["B"],window=window_size)
# b_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["B"],window=window_size)
# c_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["C"],window=window_size)
# c_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["C"],window=window_size)
# d_rpdo = params.motor_rpdo1_rpm_params.copy(field_ids = ["D"],window=window_size)
# d_tpdo = params.motor_tpdo1_rpm_params.copy(field_ids = ["D"],window=window_size)
# panda_log = plot_data(
#     data_input=csv_path,
#     plot_params=[
#         [a_rpdo, a_tpdo],
#         [b_rpdo, b_tpdo],
#         [c_rpdo, c_tpdo],
#         [d_rpdo, d_tpdo],
#         params.motor_tpdo1_current_params,
#     ],
#     plot_title="Sluggish Cultivator",
#     save_title="post-flash",
#     show_plot=True,
# )
