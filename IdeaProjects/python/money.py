import random

money = 10000

for man in range(1, 21):
    # 随机绩效
    jixiao = random.randint(1, 10)
    if jixiao <= 5:
        print(f"员工{man},绩效为{jixiao}<5,不发工资")
        if man == 20:
            print("领取工资环节结束")
            break
        continue
    else:
        money -= 1000
        print(f"员工{man}领取工资1000元,账户余额还剩{money}")
    if money == 0:
        print("工资发完了,结束发工资")
        break
    elif man == 20:
        print("领取工资环节结束")
        break
