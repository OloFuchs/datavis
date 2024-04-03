import pandas as pd
import utils
import plot_method 

LOG = "logs/24-04-01-warehouse2/csv/resample.csv"

log_raw = pd.read_csv(LOG,skiprows=[1])
print(log_raw.keys())

# log = utils.time_filter(log_raw,10,60)

plot_method.plot_current_temp_velocity_power(log_raw)

list = ['CAN1.MOTOR_A_TPDO2.BATT_POWER','CAN1.MOTOR_B_TPDO2.BATT_POWER','CAN1.MOTOR_C_TPDO2.BATT_POWER','CAN1.MOTOR_D_TPDO2.BATT_POWER']

for item in list:
    ave = utils.average_in_time_range(log_raw,1213,1227,item)
    print(f"{ave}")