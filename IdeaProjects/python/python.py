# print("-"*3)
# # split是以...隔开(...指的是空格，逗号等)
# a, b = input("输入两个数字，用逗号隔开").split(',')
# trueOrFalse = a > b
# if trueOrFalse:
#     print("a >b")
# else:
#     print("a<b")

# n = 100
# # 定义一个变量作为总和
# sum = 0
# cus = 1
# while cus <= n:
#     sum = sum+cus
#     cus += 1
# print("1到%d的总和%d" % (n, sum))

# count = 0
# while count < 5:
#     print(count, "<5")
#     count += 1
# else:
#     print(count, ">=5")
# for的三种遍历\
# range包头不包尾
# for i in range(1, 100):
#     print(i)
# # 会遍历字符串
# for j in "zhou jian sheng":
#     print(j)
# # 遍历数组内的内容
# A = [1, 2, 3, 4, 5]
# for k in A:
#     print(k)


# answer = 87
# guess = -1
# count = 0
# while count < 5:
#     guess = int(input("请猜一个数字"))
#     count += 1
#     if guess == answer:
#         print("你答对了")
#     elif guess < answer:
#         print("猜的小了")
#     elif guess > answer:
#         print("猜的大了")


# for i in range(1, 50):
#     print(i)
# else:
#     print("循环结束")


holidy_name = input("请输入节日:")
if holidy_name == "春节":
    print("过春节")
elif holidy_name == "中秋节":
    print("过中秋节")
elif holidy_name == "国庆节":
    print("过国庆节")
else:
    print("不过节")
