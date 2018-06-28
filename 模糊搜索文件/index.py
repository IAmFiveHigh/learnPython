import os

files = os.listdir("./")

for f in files:
    if "fish" in f and f.endswith(".png"):
        print("find it! " + f)
