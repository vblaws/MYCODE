num = 10
if int(input("请输入第一次猜的数字")) == num:
    print("恭喜,第一次就猜对了")
elif int(input("不对,再猜一次")) == num:
    print("恭喜,猜对了")
elif int(input("不对,再再猜一次")) == num:
    print("恭喜你猜对了")
else:
    print("sorry,猜错了，最后答案为%d" % num)
