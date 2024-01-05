# 迭代
dcit = {'name': '二毛', 'age': '23', 'sex': '男'}
for key in dcit:
    print(key, end=" ")
print('\n')
for value in dcit.values():
    print(value, end=' ')
print('\n')
list1 = [x*x for x in range(1, 50) if x % 2 == 0]
print(list1)
list2 = [(x, y) for x in range(1, 10) for y in range(1, 20)]
print(list2)

# 同时迭代两个列表
for list1, list2 in zip(list1, list2):
    print(list1, list2)
