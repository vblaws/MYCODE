# 传入一个函数作为参数
def test_func(computer):
    result = computer(1, 2)
    print(result)


# 匿名函数，只能使用一次
test_func(lambda x, y: x+y)
