"""
  created by IAmFiveHigh on 2019-01-09
 """

from bs4 import BeautifulSoup
import requests
import os
import numpy as np
import time

data_path = './'
data_filenames = [
    # '地推数据1 csv.csv'
    '地推数据2 csv.csv'
]

url = 'http://www.baidu.com/s?wd='

head = {
    'user-agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50'
}


for i in data_filenames:
    file_url = data_path + i

    data_file = os.path.join(data_path, i)
    data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)
    # print(data_arr.shape)
    array = data_arr[:,1]

    for index,i in enumerate(array):
        print(f'index = {index} tel = {i}')
        r = requests.get(url + i, headers=head)
        soup = BeautifulSoup(r.text, features='lxml')
        results = soup.find_all('div', {'class': 'c-gap-bottom-small'})
        if len(results) != 0:

            spans = results[0].find_all('span')
            if len(spans) == 2:
                address = ''.join(spans[1].text.split())

                data_arr[index][2] = address

                time.sleep(0.1)
        np.savetxt('推广2.csv', data_arr, fmt='%s', delimiter=',')



