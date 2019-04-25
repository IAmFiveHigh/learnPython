"""
  created by IAmFiveHigh on 2019-04-25
 """

import numpy as np
import matplotlib.pyplot as plt

# 统计不同气温的天数直方图

file_path = "../project2/temperate.csv"


def collect_data():
    data_array = np.loadtxt(file_path, delimiter=',', dtype='str', skiprows=1)
    return data_array


def analyze_data(data_array):
    data_array = np.core.defchararray.replace(data_array[:, -1], ' C', '')
    data_array_int = data_array.astype('int')

    return data_array_int


def save_and_show_result(data_array_int):

    plt.figure()
    # range是统计数组中数据的范围 bins是多少条柱状
    plt.hist(data_array_int, range=(min(data_array_int), max(data_array_int)), bins=len(data_array_int))
    plt.xlabel('temperate')
    plt.ylabel('number of days')
    plt.tight_layout()

    plt.savefig('./number_of_days.png')
    plt.show()


def main():
    data_array = collect_data()

    data_array_int = analyze_data(data_array)

    save_and_show_result(data_array_int)


if __name__ == '__main__':
    main()