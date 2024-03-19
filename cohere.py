import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')

TPDO1_A = "csv/extracted.ChannelGroup_0_CAN1_-_message_MOTOR_A_TPDO1_0x18A_EXT=False.csv"
RPDO1_A = "csv/extracted.ChannelGroup_4_CAN1_-_message_MOTOR_A_RPDO1_0x20A_EXT=False.csv"
TEMP_A = "csv/extracted.ChannelGroup_8_CAN1_-_message_MOTOR_A_SDO_0x58A_EXT=False.csv"


tpd01_A = pd.read_csv(TPDO1_A,skiprows=[1])
rpd01_A = pd.read_csv(RPDO1_A,skiprows=[1])
temp_A = pd.read_csv(TEMP_A,skiprows=[1])

ax1.plot(tpd01_A["timestamps"],tpd01_A["CAN1.MOTOR_A_TPDO1.RPM_A"],label = "tpd01_rpm_A")
ax1.plot(rpd01_A["timestamps"],rpd01_A["CAN1.MOTOR_A_RPDO1.REM_SPEED_A"],label = "rpd01_rpm_A")

color = 'tab:red'
ax2.plot(tpd01_A["timestamps"],tpd01_A["CAN1.MOTOR_A_TPDO1.MOTOR_A"],label = "current",color=color)
ax2.set_ylabel('current (mA)', color=color)

ax3 = ax2.twinx()
color = 'tab:blue'
ax3.plot(temp_A["timestamps"],temp_A["CAN1.MOTOR_A_SDO.TEMP_A"],label="temperature",color = color)
ax3.set_ylabel('temperature (c)', color=color)

ax1.set_xlabel("time (s)")
ax1.set_ylabel("motor speed (rpm)")
ax1.legend()

ax2.set_xlabel("time (s)")

fig.tight_layout()
plt.show()


