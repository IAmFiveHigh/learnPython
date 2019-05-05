"""
  created by IAmFiveHigh on 2019-05-01
 """
import os
import numpy as np
import matplotlib.pyplot as plt

file_path = "../project1/bikeshare"


def collect_and_analyze_data():
    member_mean_duration_list = []
    casual_mean_duration_list = []

    file_list = [file_name for file_name in os.listdir(file_path) if '.csv' in file_name]
    for file_name in file_list:
        file_name = os.path.join(file_path, file_name)
        data_array = np.loadtxt(file_name, delimiter=',', dtype='str', skiprows=1)

        # 去掉双引号
        # 骑行时间
        duration_col = np.core.defchararray.replace(data_array[:, 0], '"', '')
        duration_col = duration_col.reshape(-1, 1)

        # 会员类型
        member_type_col = np.core.defchararray.replace(data_array[:, -1], '"', '')
        member_type_col = member_type_col.reshape(-1, 1)

        # 合并
        duration_member_data = np.concatenate([duration_col, member_type_col], axis=1)

        # 会员平均骑行时间
        member_arr = duration_member_data[duration_member_data[:, -1] == 'Member'][:, 0]
        member_type_duration_mean = np.mean(member_arr.astype('float') / 1000 / 60)
        member_mean_duration_list.append(member_type_duration_mean)

        # 非会员平均骑行时间
        casual_arr = duration_member_data[duration_member_data[:, -1] == 'Casual'][:, 0]
        casual_type_duration_mean = np.mean(casual_arr.astype('float') / 1000 / 60)
        casual_mean_duration_list.append(casual_type_duration_mean)

    return member_mean_duration_list, casual_mean_duration_list


def save_and_show_result(member_mean_duration_list, casual_mean_duration_list):

    bar_width = 0.35 # 柱子宽度
    bar_locals = np.arange(4)

    plt.figure()
    plt.bar(bar_locals, member_mean_duration_list, width=bar_width, color='g', label='会员')
    plt.bar(bar_locals + bar_width, casual_mean_duration_list, width=bar_width, color='r', label='非会员')
    plt.ylabel("平均骑行时间(min)", fontproperties='SimHei')
    plt.xticks(bar_locals + bar_width / 2, ('1-3', '4-6', '7-9', '10-12'))
    plt.title("会员非会员平均骑行时间", fontproperties='SimHei')
    plt.legend(loc='best')
    plt.savefig('./member_type_mean_duration.png')
    plt.show()


def main():
    member_mean_duration_list, casual_mean_duration_list = collect_and_analyze_data()

    save_and_show_result(member_mean_duration_list, casual_mean_duration_list)


if __name__ == '__main__':
    main()