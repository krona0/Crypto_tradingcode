# 初始参数
initial_investment = 1000  # 投资金额（美元）
btc_initial_price = 60000  # 初始BTC价格（假设为30000美元）
btc_quantity = initial_investment / btc_initial_price  # 初始持有的BTC数量

# 减仓设置
sell_intervals = 20  # 分成5次减仓
price_increase_rate = 0.1  # 每次减仓价格上涨10%
sell_ratio = 1 / sell_intervals  # 每次减仓的比例

# 减仓过程记录
btc_remaining = btc_quantity  # 初始持仓
total_btc_sold = 0  # 累计卖出的BTC数量
total_usd_earned = 0  # 累计卖出的美元收益

# 模拟减仓过程
print("减仓过程模拟：\n")
for i in range(sell_intervals):
    target_price = btc_initial_price * (1 + price_increase_rate * (i + 1))  # 当前目标价格
    btc_to_sell = btc_remaining * sell_ratio  # 当前减仓的BTC数量
    usd_earned = btc_to_sell * target_price  # 当前减仓获得的美元

    # 更新累计数据
    btc_remaining -= btc_to_sell
    total_btc_sold += btc_to_sell
    total_usd_earned += usd_earned

    print(f"第 {i + 1} 次减仓：")
    print(f"  目标价格: {target_price:.2f} 美元")
    print(f"  卖出BTC数量: {btc_to_sell:.6f} BTC")
    print(f"  获得美元: {usd_earned:.2f} 美元")
    print(f"  剩余BTC数量: {btc_remaining:.6f} BTC\n")

# 剩余BTC的价值
final_price = btc_initial_price * (1 + price_increase_rate * sell_intervals)  # 最后目标价格
remaining_value = btc_remaining * final_price

# 总结
print("总结：")
print(f"初始持有BTC数量: {btc_quantity:.6f} BTC")
print(f"减仓后总卖出BTC数量: {total_btc_sold:.6f} BTC")
print(f"减仓后总美元收益: {total_usd_earned:.2f} 美元")
print(f"减仓后剩余BTC数量: {btc_remaining:.6f} BTC")
print(f"减仓后剩余BTC的价值: {remaining_value:.2f} 美元")