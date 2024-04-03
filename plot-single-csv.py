import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LOG = "logs/24-03-29-warehouse/csv/resample.csv"

radius = .205
reduction = 30

log = pd.read_csv(LOG,skiprows=[1])
print(log.keys())

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, layout='constrained')

log["MOTOR_A_ROLLING_CURRENT"] = log["CAN1.MOTOR_A_TPDO1.CURRENT"].rolling(50,center=True).mean()
log["MOTOR_B_ROLLING_CURRENT"] = log["CAN1.MOTOR_B_TPDO1.CURRENT"].rolling(50,center=True).mean()
log["MOTOR_C_ROLLING_CURRENT"] = log["CAN1.MOTOR_C_TPDO1.CURRENT"].rolling(50,center=True).mean()
log["MOTOR_D_ROLLING_CURRENT"] = log["CAN1.MOTOR_D_TPDO1.CURRENT"].rolling(50,center=True).mean()

ax1.plot(log["timestamps"],log["MOTOR_A_ROLLING_CURRENT"],label = "A")
ax1.plot(log["timestamps"],log["MOTOR_B_ROLLING_CURRENT"],label = "B")
ax1.plot(log["timestamps"],log["MOTOR_C_ROLLING_CURRENT"],label = "C")
ax1.plot(log["timestamps"],log["MOTOR_D_ROLLING_CURRENT"],label = "D")
ax1.set_xlabel('time (sec)')
ax1.set_ylabel('current (mA)')
ax1.legend()

log["MOTOR_A_ROLLING_TEMP"] = log["CAN1.MOTOR_A_SDO.TEMP"].rolling(50,center=True).mean()
log["MOTOR_B_ROLLING_TEMP"] = log["CAN1.MOTOR_B_SDO.TEMP"].rolling(50,center=True).mean()
log["MOTOR_C_ROLLING_TEMP"] = log["CAN1.MOTOR_C_SDO.TEMP"].rolling(50,center=True).mean()
log["MOTOR_D_ROLLING_TEMP"] = log["CAN1.MOTOR_D_SDO.TEMP"].rolling(50,center=True).mean()

ax2.plot(log["timestamps"],log["MOTOR_A_ROLLING_TEMP"],label = "A")
ax2.plot(log["timestamps"],log["MOTOR_B_ROLLING_TEMP"],label = "B")
ax2.plot(log["timestamps"],log["MOTOR_C_ROLLING_TEMP"],label = "C")
ax2.plot(log["timestamps"],log["MOTOR_D_ROLLING_TEMP"],label = "D")
ax2.set_xlabel('time (sec)')
ax2.set_ylabel('temp (C)')
ax2.legend()

log["MOTOR_A_VELOCITY"] = log["CAN1.MOTOR_A_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(70).mean()
log["MOTOR_B_VELOCITY"] = log["CAN1.MOTOR_B_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(70).mean()
log["MOTOR_C_VELOCITY"] = log["CAN1.MOTOR_C_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(70).mean()
log["MOTOR_D_VELOCITY"] = log["CAN1.MOTOR_D_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(70).mean()

ax3.plot(log["timestamps"],log["MOTOR_A_VELOCITY"],label = 'A')
ax3.plot(log["timestamps"],log["MOTOR_B_VELOCITY"],label = 'B')
ax3.plot(log["timestamps"],log["MOTOR_C_VELOCITY"],label = 'C')
ax3.plot(log["timestamps"],log["MOTOR_D_VELOCITY"],label = 'D')
ax3.set_xlabel('time (sec)')
ax3.set_ylabel('velocity (m/s)')
ax3.legend(loc = 2)

if "CAN1.PTO_0_RPDO1.REM_SPEED" in log.keys():
    ax4 = ax3.twinx()
    ax4.plot(log["timestamps"],log["CAN1.PTO_0_RPDO1.REM_SPEED"],label = 'PTO',color = "black")
    ax4.legend(loc = 1)

fig.tight_layout()
plt.show()
