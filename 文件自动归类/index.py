import shutil
import os


# 从分类里移动出来
def move_to_father(path_name):
    files = os.listdir("./" + path_name)
    for f in files:
        if not f.endswith(".DS_Store"):
            for sub_f in os.listdir("./" + path_name + "/" + f):
                shutil.move("./" + path_name + "/" + f + "/" + sub_f, "./" + path_name)


# 分类
def put_in_order(path_name):
    files = os.listdir(path_name)
    for f in files:
        if len(f.split(".")) == 2:
            folder_name = path_name + "/" + f.split(".")[-1]

            if os.path.exists(folder_name):
                shutil.move(path_name + "/" + f, folder_name)
            else:
                os.makedirs(folder_name)
                shutil.move(path_name + "/" + f, folder_name)


put_in_order("./problem2_files")
# move_to_father("problem2_files")