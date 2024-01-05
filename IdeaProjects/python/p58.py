def get_sum(x, y):
    """_summary_
    sum函数可以接收两个数字，并相加
    Args:
        x (_type_): 表示相加的其中一个数字
        y (_type_): 表示相加的其中一个数字
        :return:返回值是这两个数字的和
    """
    return x+y


sum = get_sum(10, 20)
print(sum)


def meth2():
    print("---2---")


def meth1():
    print("---1---")
    meth2()
    print("---3---")


meth1()
