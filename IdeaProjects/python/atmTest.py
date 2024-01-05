money = 20000
name = None

name = input("请输入你的名字")


def check_money(hader):
    if hader:
        print("------查询-------")
    print(f"你好{name},你还有{money}元钱")


def save_money(num):
    global money
    money += num
    print("------存款-------")
    print(f"你好{name},你的{num}元存好了")


def out_money(num):
    global money
    money -= num
    print("------取款-------")
    print(f"你好{name},你的{num}元取好了")


def main():
    print("------------主菜单---------------")
    print("欢迎来到ATM,请选择你的操作")
    print("查询余额\t[1]")
    print("存款\t\t[2]")
    print("取款\t\t[3]")
    print("退出\t\t[4]")
    return int(input("请输入你的选择"))


while True:
    keyboardInput = main()
    if keyboardInput == 1:
        check_money(True)
    elif keyboardInput == 2:
        num = int(input("请输入你要存的钱"))
        save_money(num)
    elif keyboardInput == 3:
        num = int(input("请输入你要取的钱"))
        out_money(num)
    else:
        break
