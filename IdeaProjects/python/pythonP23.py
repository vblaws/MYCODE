name = "www"
setense = "我叫%s" % name
print(setense)


class_num = 100
avg_money = 5000
message = "北京一共%s个城市,平均工资为%s" % (class_num, avg_money)
print(message)


name1 = "你好"
year = 2004
money = 12.14
message1 = "我是%s,今年是%d,我现在有%10.2f块钱" % (name1, year, money)
print(message1)
num1 = 19
# python可以这样写
if 10 < num1 < 20:
    print(f"num1大于10且小于20:{num1}")
