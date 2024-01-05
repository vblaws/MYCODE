import random
num = random.randint(1, 100)
count = 0
while 1:
    guess_number = int(input("请输入你猜的数字"))
    count += 1
    if guess_number == num:
        print("你猜对了")
        break
    else:
        if guess_number > num:
            print("你猜大了")
        else:
            print("你猜小了")

print("你猜了%d次" % count)
