from plot_utils import PlotParameters, plot_data_test
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

# RPM_params = PlotParameters(
#     message_name="RPM",
#     field_name="TPDO1",
#     y_label="RPM",
# )

# velocity_params = PlotParameters(
#     message_name = "RPM",
#     field_name="TPDO1",
#     y_label="Velocity(m/s)",
#     scaling_factor = 0.000715584993317675
# )

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
    y_label=" ",
)

amiga_status_params = PlotParameters(
    message_type = "TPDO1",
    message_name = "CURRENT_SPEED",
    field_name="AMIGA_STATUS",
    y_label="Amiga Speed",
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
csv_path = Path("logs/24-04-24-jacobs-new-spreader/24-04-24-jacobs-new-spreader/csv/resample.csv")

plot_data_test(csv_path,[[motor_velocity_params, pto_rpm], [batt_power_params, pto_power_params], amiga_status_params],save_title="Velocity_Power")

# plot_data([volts_params, mA_params])