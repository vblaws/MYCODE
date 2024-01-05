# 直接类的使用
class Student():

    var = '三点水'

    @classmethod
    def readBools(cls, age):
        print("原来var值为", cls.var)
        cls.var = input("请修改var值")
        print("现在var值", cls.var)

        print("年龄为", str(age))


Student.readBools(19)
Student.var = input("这是外部修改的值")
print('修改后', Student.var)

# 类的实例化


class Animal(object):
    var1 = '吃饭'

    def eatFood(self):
        print('我在', self.var1)


# 实例化，赋值给a
a = Animal()

a.eatFood()
print(a.var1)
