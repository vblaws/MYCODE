def getMan(name, age, address):
    print(f"名字{name}年龄{age}地址{address}")


getMan('北京', 12, '北京')
getMan(age=99, address='南京', name='王朔')

# 元组


def user_info(*args):
    print(args)


# 数量不受限
user_info('tom', 19, 19, 19, 24)

# 键值对,存储为字典,数量都无限
# 字典对象


def users_info(**kwargs):
    print(kwargs)


# key=value
users_info(name='tom', age=18, address='北京')
