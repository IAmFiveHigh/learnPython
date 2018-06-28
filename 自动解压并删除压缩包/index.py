import os
import shutil


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


while True:
    f = scan_file()
    if f:
        unzip_file(f)
        delete(f)


