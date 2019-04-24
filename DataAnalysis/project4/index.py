"""
  created by IAmFiveHigh on 2019-04-18
 """

import os
import numpy as np
import matplotlib.pyplot as plt

# 统计每月气温的最大值、最小值及平均值


file_name = '../project2/temperate.csv'


def collection_data_and_process():
    data_array = np.loadtxt(file_name, delimiter=',', dtype=str, skiprows=1)
    return data_array


def analyze_data(temperate_data_array, month):
    bool_array = temperate_data_array[:, 0] == month
    # 筛选出指定月份
    filter_array = temperate_data_array[bool_array]

    return calculate_data(filter_array[:, -1])


def calculate_data(month_data_array):
    month_data_array = np.core.defchararray.replace(month_data_array, ' C', '')
    month_data_array_int = month_data_array.astype('int')
    max = np.max(month_data_array_int)
    min = np.min(month_data_array_int)
    mean = np.mean(month_data_array_int)

    return (max, min, mean)


def save_and_show_result(*months):

    for i, month in enumerate(months):
        print("{}月最高温：{}摄氏度, 最低温: {}摄氏度, 平均温度: {:.2f}摄氏度".format(i + 1, month[0], month[1], month[2]))


def main():
    temperate_data_array = collection_data_and_process()

    january = analyze_data(temperate_data_array, '1')
    february = analyze_data(temperate_data_array, '2')
    march = analyze_data(temperate_data_array, '3')

    save_and_show_result(january, february, march)


if __name__ == '__main__':
    main()

