import os
import shutil
import filecmp

def scan_file():
    files = os.listdir()
    for f in files:
        if f.endswith(".zip"):
            return f


def unzip_file(f):
    folder_name = f.split(".")[0]
    target_path = "./" + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(f, target_path)


def delete(f):
    os.remove(f)


# while True:
#     f = scan_file()
#     if f:
#         unzip_file(f)
#         delete(f)


# 比较两个文件是否一致
path1 = "./ad_background-568h@2x.png"
path2 = "./ad_background-568h@2x2.png"
result = filecmp.cmp(path1, path2)
print(result)

