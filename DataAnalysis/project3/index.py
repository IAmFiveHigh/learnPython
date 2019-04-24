"""
  created by IAmFiveHigh on 2019-04-18
 """

import numpy as np
import os
import matplotlib.pyplot as plt

file_path = '../project1/bikeshare'

# 比较共享单车各类用户的平均骑行时间趋势


def collection_data_and_process_data():
    # 数据获取和数据处理
    data_array_list = []
    file_list = [filename for filename in os.listdir(file_path) if '.csv' in filename]
    for filename in file_list:
        filename = os.path.join(file_path, filename)
        data_array = np.loadtxt(filename, delimiter=',', dtype='str', skiprows=1)
        clean_data_array = np.core.defchararray.replace(data_array, '"', '')

        data_array_list.append(clean_data_array)
    return data_array_list


def get_mean_time_by_type(data_list_array, member_type):
    mean_duration_array = []

    for data_list in data_list_array:
        bool_array = data_list[:, -1] == member_type
        filter_array = data_list[bool_array]

        mean_duration = np.mean(filter_array[:, 0].astype('float') / 1000 / 60)
        mean_duration_array.append(mean_duration)
    return mean_duration_array


def save_and_show_result(member_data_list, casual_data_list):
    # 保存结果并展示
    for i in range(len(member_data_list)):
        member_duration = member_data_list[i]
        casual_duration = casual_data_list[i]
        print('第{}季度，会员平均骑行时间:{:.2f}分钟，非会员骑行时间:{:.2f}分钟'.format(i + 1, member_duration, casual_duration))

    mean_duration_arr = np.array([member_data_list, casual_data_list]).transpose()
    np.savetxt('./会员非会员平均骑行时间.csv', mean_duration_arr, delimiter=',', header='会员平均骑行时间, 非会员平均骑行时间', fmt='%.4f', comments='')


    # 可视化
    plt.figure()
    plt.plot(member_data_list, color='g', linestyle='-', marker='o', label='member')
    plt.plot(casual_data_list, color='r', linestyle='--', marker='*', label='casual')
    plt.title("会员和非会员不同季度平均骑行时间")
    plt.xlabel('季度')
    plt.xticks(range(0, 4), ['1st', '2nd', '3rd', '4th'], rotation=45)
    plt.ylabel('平均骑行时间')
    plt.legend(loc='best')

    # 紧凑布局
    plt.tight_layout()

    plt.savefig('./会员和非会员不同季度平均骑行时间.png')
    plt.show()


def main():
    data_list_array = collection_data_and_process_data()
    # 会员平均时间
    mean_duration_array_member = get_mean_time_by_type(data_list_array, 'Member')
    # 非会员平均时间
    mean_duration_array_casual = get_mean_time_by_type(data_list_array, 'Casual')

    save_and_show_result(mean_duration_array_member, mean_duration_array_casual)

if __name__ == '__main__':
    main()