"""
  created by IAmFiveHigh on 2019-04-17
 """
import numpy as np

# 创建一个批量温度转换器 摄氏度转华氏度

file_name = './temperate.csv'


def collection_data():
    # 获取csv文件转ndarray
    data_array = np.loadtxt(file_name, delimiter=',', dtype='str', skiprows=1)
    return data_array


def transform_data(data_array):
    c_temperate_str = data_array[:, 1]
    c_temperate_str = np.core.defchararray.replace(c_temperate_str, ' C', '')
    c_temperate_int = c_temperate_str.astype('int') * 1.8 + 32
    data_array[:, 1] = c_temperate_int.astype('str')
    return data_array


def main():
    data_array = collection_data()
    f_result = transform_data(data_array)
    return f_result

if __name__ == '__main__':
    main()