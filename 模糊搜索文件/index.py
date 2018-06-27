import os

files = os.listdir("/Users/woshiwugaoniganxin/Desktop/learnPython/模糊搜索文件")

for f in files:
    if "fish" in f and f.endswith(".png"):
        print("find it! " + f)
