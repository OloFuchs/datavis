import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LOG = "logs/warehouse_0326/csv/resample.csv"

radius = .205
reduction = 30

log = pd.read_csv(LOG,skiprows=[1])
print(log.keys())

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, layout='constrained')

ax1.plot(log["timestamps"],log["CAN1.MOTOR_A_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(50,center=True).mean(),label = "Measured")
ax1.plot(log["timestamps"],log["CAN1.MOTOR_A_RPDO1.REM_SPEED_A"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(50,center=True).mean(),label = "Request")
ax1.set_title('Motor A')
ax1.set_xlabel('time (sec)')
ax1.set_ylabel('velocity (m/s)')
ax1.legend()

ax2.plot(log["timestamps"],log["CAN1.MOTOR_B_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(50,center=True).mean(),label = "Measured")
ax2.plot(log["timestamps"],log["CAN1.MOTOR_B_RPDO1.REM_SPEED_B"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)).rolling(50,center=True).mean(),label = "Request")
ax2.set_title('Motor B')
ax2.set_xlabel('time (sec)')
ax2.set_ylabel('velocity (m/s)')
ax2.legend()

ax3.plot(log["timestamps"],log["CAN1.MOTOR_C_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)),label = "Measured")
ax3.plot(log["timestamps"],log["CAN1.MOTOR_C_RPDO1.REM_SPEED_C"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)),label = "Request")
ax3.set_title('Motor C')
ax3.set_xlabel('time (sec)')
ax3.set_ylabel('velocity (m/s)')
ax3.legend()

ax4.plot(log["timestamps"],log["CAN1.MOTOR_D_TPDO1.RPM"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)),label = "Measured")
ax4.plot(log["timestamps"],log["CAN1.MOTOR_D_RPDO1.REM_SPEED_D"].apply(lambda x: (x*(2*np.pi*radius))/(60*reduction)),label = "Request")
ax4.set_title('Motor D')
ax4.set_xlabel('time (sec)')
ax4.set_ylabel('velocity (m/s)')
ax4.legend()

fig.tight_layout()
plt.show()
