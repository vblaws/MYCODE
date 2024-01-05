name_list = ['哈哈', '你好', '不好']

# print(name_list)
# print(type(name_list))


# mix_list = ['哈哈', 666, True]
# # print(mix_list)
# # print(type(mix_list))
# print(mix_list[0])
# print(mix_list[1])
# print(mix_list[2])

# print(mix_list[-1])
# print(mix_list[-2])
# print(mix_list[-3])


# age_list = [[1, 2], [3, 4], [5, 6]]

# print(age_list[2][1])


num_list = [i for i in range(0, 30) if i % 3 == 0]
print(num_list)

name = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
# 列表推导式
new_names = [name.upper()for name in name if len(name) > 3]
print(new_names)
# 字典推导式
dict = ['Queen', 'King', 'Jacket']
newdict = {key: len(key) for key in dict}
print(newdict)
