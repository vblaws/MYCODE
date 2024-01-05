for i in range(1, 20):
    print(i)
    if i == 10:
        break  # 中途遇到break会直接退出执行后面的语句，不会执行else内的
else:
    print("执行到%d已退出" % i)
print("没有执行语句")

count = 0
while count < 10:
    print("执行到%d" % count)
    count += 1
else:
    print("退出是count为%d" % count)
