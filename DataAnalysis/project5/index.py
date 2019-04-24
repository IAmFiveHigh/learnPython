"""
  created by IAmFiveHigh on 2019-04-19
 """

import numpy as np
import os
import matplotlib.pyplot as plt

# 比较全年啊共享单车用户类别（会员 非会员）比例

file_path = '../project1/bikeshare'


def collection_and_process_data():
    member_type_col_list = []
    file_list = [filename for filename in os.listdir(file_path) if '.csv' in filename]
    for file in file_list:
        file_name = os.path.join(file_path, file)
        data_array = np.loadtxt(file_name, delimiter=',', dtype='str', skiprows=1)

        # 获取单列数据默认是横向一行数据
        member_type_col = np.core.defchararray.replace(data_array[:, -1], '"', '')
        # 换成列
        member_type_col = member_type_col.reshape(-1, 1)
        member_type_col_list.append(member_type_col)
    year_member_type = np.concatenate(member_type_col_list)
    return year_member_type


def analyze_data(year_member_type):
    number_member = year_member_type[year_member_type == 'Member'].shape[0]
    number_casual = year_member_type[year_member_type == 'Casual'].shape[0]
    user = [number_member, number_casual]
    return user


def save_and_show_result(user):
    plt.figure()
    plt.pie(user, labels=['Member', 'Casual'], autopct='%.2f%%', shadow=True, explode=(0.02, 0))
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('./out_pie_img.png')
    plt.show()


def main():
    year_member_list = collection_and_process_data()

    users = analyze_data(year_member_list)

    save_and_show_result(users)


if __name__ == '__main__':
    main()