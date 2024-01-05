if int(input("请输入你的身高")) > 120:
    print("对不起,你的身高不满足要求")
    print("不过你VIP等级高的话也可以免费")
    if int(input("请输入你的VIP等级")) > 3:
        print("你好，你可以免费")
    else:
        print("依旧不能免费,需要补票十元")
else:
    print("身高不到120，可以免费")
