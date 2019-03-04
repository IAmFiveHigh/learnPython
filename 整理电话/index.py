"""
  created by IAmFiveHigh on 2019-03-04
 """
import csv
import re
import numpy

file = csv.reader(open('Sheet3-表格 1.csv'))

array1 = []
for s in file:
    a = s[0].replace(' ', '')
    a = a.replace('|', '')
    # extend 合并数组  findall查找所有匹配项  [\u4e00-\u9fa5]所有汉字
    array1.extend(re.findall(u'[\u4e00-\u9fa5][0-9]+', a))

print(array1)

a = numpy.array(array1)
b = numpy.savetxt('a.csv', a, fmt='%s', delimiter=',')








