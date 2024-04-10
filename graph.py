from plot_utils import PlotParameters, plot_data
import pandas as pd
from pathlib import Path
from utils import time_filter

voltage_params = PlotParameters(
    message_name="VOLTAGE",
    field_name="TPDO1",
    y_label="Voltage (V)"
)
current_params = PlotParameters(
    message_name="CURRENT",
    field_name="TPDO1",
    y_label="Current (mA)"
)

RPM_params = PlotParameters(
    message_name="RPM",
    field_name="TPDO1",
    y_label="RPM",
)

velocity_params = PlotParameters(
    message_name = "RPM",
    field_name="TPDO1",
    y_label="velocity (m/s)",
    scaling_factor = 0.000715584993317675
)

temp_params = PlotParameters(
    message_name="TEMP",
    field_name="SDO",
    y_label="Temperature (c)"
)

TPDO = [RPM_params,current_params,voltage_params]
rpm = [RPM_params]
velocity_current_temp = [velocity_params,current_params,temp_params]


# Assuming log data is in a CSV file for this example
csv_path = Path("logs/24-04-08-santa-maria/csv/resample.csv")

# Make sure to replace '/path/to/your/log_file.csv' with the actual path to your log file
if csv_path.is_file():
    # Read the CSV file into a DataFrame

    log_df = pd.read_csv(csv_path,skiprows=[1])
    print(log_df.keys())

    # Now log_df is a DataFrame and can be passed to plot_data
    # plot_params would be a list of PlotParameters objects you've defined elsewhere

    filtered = time_filter(log_df,74,443)

    plot_data(filtered,velocity_current_temp, csv_path)
else:
    print(f"File not found: {csv_path}")





# plot_data([volts_params, mA_params])