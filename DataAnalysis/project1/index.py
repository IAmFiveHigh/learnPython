"""
  created by IAmFiveHigh on 2019-04-16
 """
import os
import numpy as np
import matplotlib.pyplot as plt

data_path = './bikeshare'


def collection_data():
    # 数据收集
    data_array_list = []
    file_list = [filename for filename in os.listdir(data_path) if '.csv' in filename]
    for filename in file_list:
        filename = os.path.join(data_path, filename)
        data_array = np.loadtxt(filename, delimiter=',', dtype='str', skiprows=1)
        data_array_list.append(data_array)
    return data_array_list


def process_data(data_array_list):
    # 处理数据
    duration_in_min_list = []

    for data_array in data_array_list:
        # 获取所有行第一列数据
        duration_str_col = data_array[:, 0]
        # 把第一列数据的双引号替换成空
        duration_in_ms = np.core.defchararray.replace(duration_str_col, '"', '')
        # 类型转换
        duration_in_min = duration_in_ms.astype('float') / 1000 / 60

        duration_in_min_list.append(duration_in_min)
    return duration_in_min_list


def analyze_data(duratioin_in_min_list):
    # 数据分析

    duration_mean_list = []

    for i, duration in enumerate(duratioin_in_min_list):
        duration_mean = np.mean(duration)
        print('第{}季度平均骑行时间:{:.2f}分钟'.format(i + 1, duration_mean))
        duration_mean_list.append(duration_mean)
    return duration_mean_list


def show_result(duration_mean_list):
    # 结果展示
    plt.figure()
    plt.bar(range(len(duration_mean_list)), duration_mean_list)
    plt.show()


def main():
    data_array_list = collection_data()

    duration_list = process_data(data_array_list)

    duration_mean_list = analyze_data(duration_list)

    show_result(duration_mean_list)


if __name__ == '__main__':
    main()






