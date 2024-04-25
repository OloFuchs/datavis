import pandas as pd
import utils

LOG = "logs/24-04-12-warehouse/00000010/csv/resample.csv"

log_raw = pd.read_csv(LOG,skiprows=[1])
# print(log_raw.keys())

list = ['CAN1.MOTOR_A_TPDO1.CURRENT','CAN1.MOTOR_B_TPDO1.CURRENT','CAN1.MOTOR_C_TPDO1.CURRENT','CAN1.MOTOR_D_TPDO1.CURRENT']
# times = [(29,53), (65,90), (102,122), (134,157), (171,192), (214,237)]
# times = [(55,79), (95,120), (136,154), (169,192), (236,258), (271,293)]
times = [(35,59), (71,95), (108,126), (142, 164), (178,202), (216,239)]

for time in times:
    ave_str = ""
    for item in list:
        ave = utils.average_in_time_range(log_raw,time,item)
        ave_str += (f"{ave: .4f}\t")
    print(ave_str)