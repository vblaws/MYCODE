def say_hello():
    print("你好")


# 接收返回值,是为空f
result = say_hello()
print(f"返回的内容是{result}")

print(f"返回的内容的类型是{type(result)}")

# 定义一个方法检查年龄


def check_age(age):
    if age > 18:
        return "SUCCESS"
    # 在if中None等同于false
    return None


# 如果result为负，它会自动检查会负
result = check_age(10)
print(f"如果大于18岁，结果为{result}")

# 如果result为false,not result则指的是true
if not result:
    print("你没有成年")
else:
    print("成年了")
