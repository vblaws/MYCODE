import random
num = random.randint(1, 10)

guess_number = int(input("请输入你猜的数字"))

if guess_number == num:
    print("第一次就猜对了")
else:
    if guess_number > num:
        print("你猜大了")
    else:
        print("你猜小了")

    guess_number = int(input("请输入你第二次猜的数字"))
    if guess_number == num:
        print("你第二次猜对了")
    else:
        if guess_number > num:
            print("你猜大了")
        else:
            print("你猜小了")
    guess_number = int(input("请输入你第三次猜的数字"))
    if guess_number == num:
        print("你第三次猜对了")
    else:
        print("三次机会用完了,没有猜中")
print(f"游戏结束,答案为{num}")
