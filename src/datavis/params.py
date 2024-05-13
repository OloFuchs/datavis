from datavis.plot_utils import PlotParameters

motor_velocity_params = PlotParameters(
    message_name="RPM",
    message_type="TPDO1",
    field_name="motor",
    scaling_factor=0.000715584993317675,
    y_label="velocity (m/s)",
)

motor_tpd01_status_params = PlotParameters(
    message_name="status",
    message_type="TPDO1",
    field_name="motor",
    window=1,
    legend="status",
    y_label="status",
)

pendant_y = PlotParameters(
    message_name="y_pos",
    message_type="tpdo1",
    field_name="pendant",
    y_label="pendant y",
)

pto_status = PlotParameters(
    message_name="status", message_type="rpdo1", field_name="pto", y_label="PTO Status"
)

pto_rpm = PlotParameters(
    message_name="rpm",
    message_type="tpdo1",
    field_name="pto",
    scaling_factor=1 / 800,
    legend="pto status",
    y_label="PTO RPM",
)

motor_tpdo1_rpm_params = PlotParameters(
    message_name="RPM",
    message_type="TPDO1",
    field_name="motor",
    # field_ids=["A"],
    legend="measured",
    y_label="RPM",
)
motor_tpdo1_current_params = PlotParameters(
    message_name="current",
    message_type="TPDO1",
    field_name="motor",
    window=300,
    legend="current",
    y_label="Current (mA)",
)
motor_tpdo1_voltage_params = PlotParameters(
    message_name="voltage",
    message_type="TPDO1",
    field_name="motor",
    # field_ids=["A"],
    legend="voltage",
    y_label="Voltage (Volts)",
)
motor_rpdo1_rpm_params = PlotParameters(
    message_name="RPM",
    message_type="RPDO1",
    field_name="motor",
    # field_ids=["A"],
    legend="request",
    y_label="RPM",
    opacity=0.5,
)
motor_tpdo1_velocity_params = PlotParameters(
    message_name="RPM",
    message_type="TPDO1",
    field_name="motor",
    # field_ids=["A"],
    scaling_factor=0.000715584993317675,
    y_label="Velocity (m/s)",
)

motor_temp_params = PlotParameters(
    message_name="TEMP",
    message_type="SDO",
    field_name="motor",
    y_label="Temperature(c)",
    legend="temp",
)

motor_tpd02_batt_power_params = PlotParameters(
    message_type="TPDO2",
    message_name="BATT_POWER",
    field_name="motor",
    legend="watts",
    y_label="POWER(WATTS)",
)

motor_tpdo2_motor_power_params = PlotParameters(
    message_type="TPDO2",
    message_name="Motor_POWER",
    field_name="motor",
    legend="power",
    y_label="POWER(WATTS)",
)

pto_power_params = PlotParameters(
    message_type="TPDO2",
    message_name="BATT_POWER",
    field_name="PTO",
    legend="pto battery",
    y_label=" ",
)

amiga_tpdo_linear_params = PlotParameters(
    message_type="TPDO1",
    message_name="CURRENT_SPEED",
    field_name="AMIGA_STATUS",
    legend="linear",
    y_label="Linear Velocity",
)

amiga_tpdo_omega_params = PlotParameters(
    message_type="TPDO1",
    message_name="CURRENT_OMEGA",
    field_name="AMIGA_STATUS",
    legend="angular",
    y_label="Angular Velocity",
)

calc_battery_current_params = PlotParameters(
    message_name=" ",
    message_type="MATH",
    field_name="BATTERY_CURRENT",
    y_label="Current (A)",
)

calc_motor_power_params = PlotParameters(
    message_name=" ",
    message_type="MATH",
    field_name="MOTOR_POWER",
    y_label="WATTS (A)",
    legend="watts",
)


# batt_current_params = PlotParameters(
#     message_name="BATT_CURRENT",
#     field_name="TPDO2",
#     y_label="Current(mA)"
# )
