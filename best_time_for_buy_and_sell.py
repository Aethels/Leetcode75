import random

prices = random.sample(range(1, 100), 10)
print(prices)

min_price = prices[0]
max_profit = 0
buy_day = 0
sell_day = 0

for i, price in enumerate(prices):
    if price < min_price:
        min_price = price
        buy_day = i
    elif price - min_price > max_profit:
        max_profit = price - min_price
        sell_day = i


print(f"The maximum profit you can achieve is {max_profit}")
print(f"You should buy the stock on day {buy_day + 1} and sell it on day {sell_day + 1}")