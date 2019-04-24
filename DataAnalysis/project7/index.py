"""
  created by IAmFiveHigh on 2019-04-24
 """

import os
import numpy as np
import matplotlib.pyplot as plt


file_path = '../project1/bikeshare'


m_range = (0, 180)
n_bins = 12


def collect_and_process_data():

    year_member_type_duration_list = []

    file_list = [file_name for file_name in os.listdir(file_path) if '.csv' in file_name]
    for file in file_list:
        file_name = os.path.join(file_path, file)
        data_array = np.loadtxt(file_name, delimiter=',', dtype='str', skiprows=1)

        # 持续时间
        duration_time_col = np.core.defchararray.replace(data_array[:, 0], '"', '')
        duration_time_col = duration_time_col.reshape(-1, 1)

        # 会员类型
        member_type_col = np.core.defchararray.replace(data_array[:, -1], '"', '')
        member_type_col = member_type_col.reshape(-1, 1)

        member_type_duration_array = np.concatenate([duration_time_col, member_type_col], axis=1)
        year_member_type_duration_list.append(member_type_duration_array)

    # 合并成一列ndarray
    year_member_type_duration_list = np.concatenate(year_member_type_duration_list)

    return year_member_type_duration_list


def analyze_data(year_member_type_duration_list):
    m_duration = year_member_type_duration_list[year_member_type_duration_list[:,-1] == 'Member']
    c_duration = year_member_type_duration_list[year_member_type_duration_list[:,-1] == 'Casual']

    # 取出时间单位转换成分钟
    m_duration = m_duration[:, 0].astype('float') / 1000 / 60
    c_duration = c_duration[:, 0].astype('float') / 1000 / 60

    m_duration_hist = np.histogram(m_duration, range=m_range, bins=n_bins)
    c_duration_hist = np.histogram(c_duration, range=m_range, bins=n_bins)
    print(m_duration_hist)
    print(c_duration_hist)

    return m_duration, c_duration


def save_and_show_result(m_duration, c_duration):
    # 10 5 宽高比
    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    # 会员直方图
    ax1.hist(m_duration, range=m_range, bins=n_bins)
    ax1.set_xticks(range(0, 181, 15))
    ax1.set_title('Member')
    ax1.set_ylabel('count')

    # 非会员直方图
    ax2.hist(c_duration, range=m_range, bins=n_bins)
    ax2.set_xticks(range(0, 181, 15))
    ax2.set_title('Casual')
    ax2.set_ylabel('count')

    plt.tight_layout()
    plt.savefig('./hist.png')
    plt.show()


def main():
    year_member_type_duration = collect_and_process_data()

    result = analyze_data(year_member_type_duration)

    save_and_show_result(result[0], result[1])


if __name__ == '__main__':
    main()