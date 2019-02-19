"""
  created by IAmFiveHigh on 2019-02-19
 """

# Hailstone


def hailstone(a, l=[]):
    l.append(a)
    if a <= 1:
        return l
    elif a % 2 == 1:
        l = hailstone(3 * a + 1, l)
    else:
        l = hailstone(a / 2, l)
    return l

# 冰雹序列
print("冰雹序列 输入42")
l1 = hailstone(42)
print(l1, '\n')
print("冰雹序列 输入7")
l1 = hailstone(7)
print(l1, '\n')
print("冰雹序列 输入27")
l1 = hailstone(27)
print(l1, '\n')