import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TPDO1_A = "csv/extracted.ChannelGroup_0_CAN1_-_message_MOTOR_A_TPDO1_0x18A_EXT=False.csv"
RPDO1_A = "csv/extracted.ChannelGroup_4_CAN1_-_message_MOTOR_A_RPDO1_0x20A_EXT=False.csv"

tpd01_A = pd.read_csv(TPDO1_A,skiprows=[1])
rpd01_A = pd.read_csv(RPDO1_A,skiprows=[1])

plt.plot(tpd01_A["timestamps"],tpd01_A["CAN1.MOTOR_A_TPDO1.RPM_A"],label = "tpd01_rpm_A",marker = "o")
plt.plot(rpd01_A["timestamps"],rpd01_A["CAN1.MOTOR_A_RPDO1.REM_SPEED_A"],label = "rpd01_rpm_A",marker = "x")

plt.xlabel("time (s)")
plt.ylabel("motor speed (rpm)")
plt.legend()
plt.show()


