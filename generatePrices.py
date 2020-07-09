import csv
import random
import numpy as np





def generate(days):
    avg_daily_return = random.uniform(-0.002, 0.005)
    daily_vol = random.uniform(0.010, 0.02)
    dailyValues = []
    current_price = round(random.uniform(20, 250), 2)
    dailyValues.append(current_price)
    for day in range(days - 1):
        price = round(dailyValues[day] * (1 + np.random.normal(avg_daily_return, daily_vol)), 2)
        dailyValues.append(price)

    return dailyValues

def generateStockPrices(stocks):
    stock_price_list = []
    for stock in range(50):
        stock_price_list.append(generate(1000))
    return stock_price_list

list = generateStockPrices(50)




list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(list[3:5])