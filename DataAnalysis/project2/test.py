"""
  created by IAmFiveHigh on 2019-04-17
 """
import numpy as np


a = [[2,3,9],
     [3,9,9],
     [4,8,9]]
a = np.array(a)
print(a)
print()
# 每列最大
print(np.max(a, axis=0))
# 每行最大
print(np.max(a, axis=1))

print(np.where(a == np.max(a)))

