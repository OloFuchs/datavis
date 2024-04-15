from plot_utils import PlotParameters, plot_data
import pandas as pd
from pathlib import Path
from utils import time_filter

voltage_params = PlotParameters(
    message_name="VOLTAGE",
    field_name="TPDO1",
    y_label="Voltage (V)"
)
motor_current_params = PlotParameters(
    message_name="CURRENT",
    field_name="TPDO1",
    y_label="Current(mA)"
)

RPM_params = PlotParameters(
    message_name="RPM",
    field_name="TPDO1",
    y_label="RPM",
)

velocity_params = PlotParameters(
    message_name = "RPM",
    field_name="TPDO1",
    y_label="Velocity(m/s)",
    scaling_factor = 0.000715584993317675
)

temp_params = PlotParameters(
    message_name="TEMP",
    field_name="SDO",
    y_label="Temperature(c)"
)

batt_power_params = PlotParameters(
    message_name = "BATT_POWER",
    field_name="TPDO2",
    y_label="watts",
)

batt_current_params = PlotParameters(
    message_name="BATT_CURRENT",
    field_name="TPDO2",
    y_label="Current(mA)"
)


TPDO = [RPM_params,motor_current_params,voltage_params]
rpm = [RPM_params]
velocity_current_temp = [velocity_params,motor_current_params,temp_params]
battery = [batt_power_params, voltage_params, batt_current_params]
rpm_current = [RPM_params, motor_current_params]


# Assuming log data is in a CSV file for this example
csv_path = Path("logs/24-04-12-warehouse/00000010/csv/resample.csv")

plot_data(csv_path,rpm_current)

# plot_data([volts_params, mA_params])