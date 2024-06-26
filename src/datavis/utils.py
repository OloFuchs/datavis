from __future__ import annotations

import numpy as np
import pandas as pd

# from dataclasses import dataclass, field


def average_in_time_range(df, start_stop_time: tuple[int, int], column_name):
    # Filter the DataFrame for the specified time range
    filtered_df = df[
        (df["timestamps"] >= start_stop_time[0])
        & (df["timestamps"] <= start_stop_time[1])
    ]

    # Calculate and return the average of the specified column
    return filtered_df[column_name].mean()


def int_in_time_range(df, start_stop_time: tuple[int, int], column_name):
    # Filter the DataFrame for the specified time range
    filtered_df = df[
        (df["timestamps"] >= start_stop_time[0])
        & (df["timestamps"] <= start_stop_time[1])
    ]

    filtered_df = filtered_df.sort_values(by="timestamps")

    # Get the y-values from the specified column
    y_values = filtered_df[column_name].values

    # Get the x-values from the timestamps column
    x_values = filtered_df["timestamps"].values

    # Calculate the trapezoidal integral using numpy's trapz function
    integral = np.trapz(y=y_values, x=x_values)

    return integral


def peaks(df, column_name):
    # index of max value
    max_index = df[column_name].idxmax()

    # Retrieve the timestamp and maximum value
    max_timestamp = df.loc[max_index, "timestamps"]
    max_value = df.loc[max_index, column_name]

    return (max_timestamp, max_value)


def time_filter(df, start_time, end_time) -> pd.DataFrame:
    filtered = pd.DataFrame()

    start_index = min(
        range(len(df["timestamps"])),
        key=lambda i: abs(df["timestamps"][i] - start_time),
    )
    end_index = min(
        range(len(df["timestamps"])), key=lambda i: abs(df["timestamps"][i] - end_time)
    )

    for key in df.keys():
        filtered[key] = df[key][start_index : end_index + 1].copy()

    return filtered


def find_timestamp_index(df, time):
    timestamps = df["timestamps"]
    return min(range(len(timestamps)), key=lambda i: abs(timestamps[i] - time))
