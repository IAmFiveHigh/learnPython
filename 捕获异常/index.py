while True:
    num = input("输入一个数字")

    try:
        print("200除以" + num + "等于:" + str(200 / int(num)))
    except ValueError:
        print("应该输入一个数字")
    except ZeroDivisionError:
        print("0不能为分母")