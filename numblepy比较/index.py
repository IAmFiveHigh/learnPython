"""
  created by wugao on 2018-09-14
 """

import numpy as np
import os
import matplotlib.pyplot as plt

__author__ = "IAmFiveHigh"

data_path = './bikeshare'
data_filenames = [
    '2017-q1_trip_history_data.csv',
    '2017-q2_trip_history_data.csv',
    '2017-q3_trip_history_data.csv',
    '2017-q4_trip_history_data.csv',
]


def collect_data():
    """
        数据收集
    """
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)
        data_arr_list.append(data_arr)

    return data_arr_list


def process_data(data_list_array):
    duration_in_min_list = []

    for data_list in data_list_array:
        duration_str_col = data_list[:, 0]
        # 去掉双引号
        duration_in_ms = np.core.defchararray.replace(duration_str_col, '"', '')
        # 类型转换
        duration_in_min = duration_in_ms.astype('float') / 1000 / 60
        duration_in_min_list.append(duration_in_min)

    return duration_in_min_list


def analyse_data(duration_list):
    duration_mean_list = []
    for index, duration in enumerate(duration_list):
        duration_mean = np.mean(duration)
        print('第{}季度平均行驶时间: {:.2f}分钟'.format(index + 1, duration_mean))
        duration_mean_list.append(duration_mean)
    return duration_mean_list


def show_result(duration_mean_list):
    plt.figure()
    plt.bar(range(len(duration_mean_list)), duration_mean_list)
    plt.show()


def main():
    data_list_array = collect_data()

    duration_list = process_data(data_list_array)

    duration_mean_list = analyse_data(duration_list)

    show_result(duration_mean_list)


if __name__ == '__main__':
    main()