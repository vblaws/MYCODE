import ATM
money = 20000
name = None

name = input("请输入你的姓名")
# 定义查询函数


def check_money(harder):
    if harder:
        print("-------查询余额--------")
    print(f"{name}你好,余额还剩{money}元")
# 定义存款函数


def save_money(num):
    global money
    money += num
    print("-------存款--------")
    print(f"你好{name},你的{num}元存好了")


def out_money(num2):
    global money
    money -= num2
    print("-------取款--------")
    print(f"你好{name},你的{num2}元取好了")

# 定义主函数


def main():
    print("------------主菜单---------------")
    print("欢迎来到ATM,请选择你的操作")
    print("查询余额\t[1]")
    print("存款\t\t[2]")
    print("取款\t\t[3]")
    print("退出\t\t[4]")
    return int(input("请输入你的选择"))


while True:
    KeyboardInput = main()
    if KeyboardInput == 1:
        check_money(True)
        continue
    elif KeyboardInput == 2:
        num = int(input("请输入你要存多少钱,请输入"))
        save_money(num)
        continue
    elif KeyboardInput == 3:
        num = int(input("请输入你要取多少钱,请输入"))
        out_money(num)
        continue
    else:
        break
