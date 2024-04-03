import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TPDO1_A = "logs/strawberry_0320/csv/extracted.ChannelGroup_0_CAN1_-_message_MOTOR_A_TPDO1_0x18A_EXT=False.csv"
RPDO1_A = "logs/strawberry_0320/csv/extracted.ChannelGroup_4_CAN1_-_message_MOTOR_A_RPDO1_0x20A_EXT=False.csv"
TEMP_A  = "logs/strawberry_0320/csv/extracted.ChannelGroup_8_CAN1_-_message_MOTOR_A_SDO_0x58A_EXT=False.csv"

TPDO1_B = "logs/strawberry_0320/csv/extracted.ChannelGroup_1_CAN1_-_message_MOTOR_B_TPDO1_0x18B_EXT=False.csv"
RPDO1_B = "logs/strawberry_0320/csv/extracted.ChannelGroup_5_CAN1_-_message_MOTOR_B_RPDO1_0x20B_EXT=False.csv"
TEMP_B  = "logs/strawberry_0320/csv/extracted.ChannelGroup_9_CAN1_-_message_MOTOR_B_SDO_0x58B_EXT=False.csv"

TPDO1_C = "logs/strawberry_0320/csv/extracted.ChannelGroup_2_CAN1_-_message_MOTOR_C_TPDO1_0x18C_EXT=False.csv"
RPDO1_C = "logs/strawberry_0320/csv/extracted.ChannelGroup_6_CAN1_-_message_MOTOR_C_RPDO1_0x20C_EXT=False.csv"
TEMP_C  = "logs/strawberry_0320/csv/extracted.ChannelGroup_10_CAN1_-_message_MOTOR_C_SDO_0x58C_EXT=False.csv"

TPDO1_D = "logs/strawberry_0320/csv/extracted.ChannelGroup_3_CAN1_-_message_MOTOR_D_TPDO1_0x18D_EXT=False.csv"
RPDO1_D = "logs/strawberry_0320/csv/extracted.ChannelGroup_7_CAN1_-_message_MOTOR_D_RPDO1_0x20D_EXT=False.csv"
TEMP_D  = "logs/strawberry_0320/csv/extracted.ChannelGroup_11_CAN1_-_message_MOTOR_D_SDO_0x58D_EXT=False.csv"

tpd01_A = pd.read_csv(TPDO1_A,skiprows=[1])
rpd01_A = pd.read_csv(RPDO1_A,skiprows=[1])
temp_A = pd.read_csv(TEMP_A,skiprows=[1])

tpd01_B = pd.read_csv(TPDO1_B,skiprows=[1])
rpd01_B = pd.read_csv(RPDO1_B,skiprows=[1])
temp_B = pd.read_csv(TEMP_B,skiprows=[1])

tpd01_C = pd.read_csv(TPDO1_C,skiprows=[1])
rpd01_C = pd.read_csv(RPDO1_C,skiprows=[1])
temp_C = pd.read_csv(TEMP_C,skiprows=[1])

tpd01_D = pd.read_csv(TPDO1_D,skiprows=[1])
rpd01_D = pd.read_csv(RPDO1_D,skiprows=[1])
temp_D = pd.read_csv(TEMP_D,skiprows=[1])

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, layout='constrained')

ax1.plot(tpd01_A["timestamps"],tpd01_A["CAN1.MOTOR_A_TPDO1.MOTOR_A"],label = "current_A")
ax1.plot(tpd01_B["timestamps"],tpd01_B["CAN1.MOTOR_B_TPDO1.MOTOR_B"],label = "current_B")
ax1.plot(tpd01_C["timestamps"],tpd01_C["CAN1.MOTOR_C_TPDO1.MOTOR_C"],label = "current_C")
ax1.plot(tpd01_D["timestamps"],tpd01_D["CAN1.MOTOR_D_TPDO1.MOTOR_D"],label = "current_D")
ax1.set_xlabel('time (sec)')
ax1.set_ylabel('current (mA)')
ax1.legend()

ax2.plot(temp_A["timestamps"],temp_A["CAN1.MOTOR_A_SDO.TEMP_A"],label="temp_A")
ax2.plot(temp_B["timestamps"],temp_B["CAN1.MOTOR_B_SDO.TEMP_B"],label="temp_B")
ax2.plot(temp_C["timestamps"],temp_C["CAN1.MOTOR_C_SDO.TEMP_C"],label="temp_C")
ax2.plot(temp_D["timestamps"],temp_D["CAN1.MOTOR_D_SDO.TEMP_D"],label="temp_D")
ax2.set_xlabel('time (sec)')
ax2.set_ylabel('temperature (c)')
ax2.legend()

ax3.plot(tpd01_A["timestamps"],tpd01_A["CAN1.MOTOR_A_TPDO1.RPM_A"],label = "rpm_A")
ax3.plot(tpd01_B["timestamps"],tpd01_B["CAN1.MOTOR_B_TPDO1.RPM_B"],label = "rpm_B")
ax3.plot(tpd01_C["timestamps"],tpd01_C["CAN1.MOTOR_C_TPDO1.RPM_C"],label = "rpm_C")
ax3.plot(tpd01_D["timestamps"],tpd01_D["CAN1.MOTOR_D_TPDO1.RPM_D"],label = "rpm_D")
ax3.set_xlabel('time (sec)')
ax3.set_ylabel('rpm')
ax3.legend()



fig.tight_layout()
plt.show()




