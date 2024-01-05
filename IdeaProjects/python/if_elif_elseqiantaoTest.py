age = int(input("请输入你的年龄"))
year = int(input("请输入你的工龄"))
vip = int(input("请输入你的级别"))
if age > 18 and age < 30:
    print("满足年龄条件，继续判断")
    if year > 2:
        print("工龄大于两年,可以领取")
    elif vip > 3:
        print("你的级别大于3,可以领取")
    else:
        print("对不起，领取不了")
else:
    print("未成年，不能领取")
