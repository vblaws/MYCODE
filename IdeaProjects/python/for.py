# name = "itheima is a brand of itcat"
# count = 0
# for a in name:
#     if a == 'a':
#         count += 1
#     print(a)
# print(f"这段话中有{count}个a")
seten = "what are you doing"
count1 = 0
for i in seten:
    count1 += 1
    # 包括空格
print(f"这个字符串长度为{count1}")
print(f"字符串长度为{len(seten)}")


# 定义一个函数,作用获取字符串长度
def my_len(str):
    count = 0
    for i in str:
        count += 1
    print(f"字符串{str}长度为{count}")


my_len("你在干什么")


def say_hi():
    print("你好")


say_hi()


def get_max(a, b):
    if a > b:
        return a
    else:
        return b


max_num = get_max(2, 1)
print(f"两个数字中更大的是{max_num}")


def check_Temperature(Temperature):
    if Temperature <= 37.5:
        print("你可以过去")
    else:
        print("对不起，你需要隔离")


check_Temperature(39)
