import pandas as pd


def change_todatetime(data, format_data):
    data_changed = []

    for i in data:
        transformed_data = pd.to_datetime(i, format=format_data)
        data_changed.append(transformed_data)

    return data_changed[0], data_changed[1] 