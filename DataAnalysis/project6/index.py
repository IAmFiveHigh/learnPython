"""
  created by IAmFiveHigh on 2019-04-19
 """

import os
import numpy as np
import matplotlib.pyplot as plt

# 使用饼状图可视化不同气温的天数占比

file_path = "../project2/temperate.csv"


def collection_data():
    data_array = np.loadtxt(file_path, delimiter=',', dtype='str', skiprows=1)
    return data_array


def analyze_data(data_array):
    data_array = np.core.defchararray.replace(data_array[:, -1], ' C', '')
    data_array_int = data_array.astype('int')
    max = np.max(data_array_int)
    min = np.min(data_array_int)

    result_t = []
    result_sum = []

    for i in range(min, max):
        sum = np.sum(data_array_int == i)
        if sum == 0:
            continue
        result_sum.append(sum)
        result_t.append(i)
    #  数字温度转为字符串
    result_t = list(map(lambda x: str(x) + " C", result_t))
    return (result_t, result_sum)


def save_and_show_result(result_tuple):
    plt.figure()
    plt.pie(result_tuple[1], labels=result_tuple[0], autopct='%.2f%%')
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig('./不同气温的天数占比.png')
    plt.show()


def main():
    data_array = collection_data()

    result_tuple = analyze_data(data_array)

    save_and_show_result(result_tuple)

if __name__ == '__main__':
    main()