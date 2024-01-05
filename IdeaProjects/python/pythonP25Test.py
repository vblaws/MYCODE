name = "王硕"
# 当前股价
stock_price = 19.99
# 股票代码
stock_code = '003032'
# 股票每日增长系数
stock_price_daily_growth_factor = 1.2
# 增长天数
growth_days = 7
final_money = stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司:{name},股票代码{stock_code},现在的股价为{stock_price}")
print("每日增长系数为%.2f,经过%d天后的增长,变成了%.2f" % (
      stock_price_daily_growth_factor, growth_days, final_money))


age = int(input("请输入你的年龄"))
print(f"你的年龄类型为{type(age)}")
