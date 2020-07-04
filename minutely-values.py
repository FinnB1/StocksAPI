import csv
from datetime import date
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicHermiteSpline
import math
import time
import json

minute_list = []

for x in range(510):
    minute_list.append(x)

current_day = date.today()
date_start = date(2020, 7, 4)

day = (current_day - date_start).days

current_day_prices = []
next_day_prices = []

with open('./data/daily-stock-prices.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for stock in csv_reader:
        start_price = stock[day]
        end_price = stock[day+1]
        current_day_prices.append(float(start_price))
        next_day_prices.append(float(end_price))

current_minute = 0


def generate_minutely_values(stockID):
    minutely_values = []
    start_val = current_day_prices[stockID]
    end_val = next_day_prices[stockID]
    x_to_fit = []
    y_to_fit = []
    num_points = random.randint(7, 13)
    x_to_fit.append(0)
    y_to_fit.append(start_val)
    x_to_fit.append(509)
    y_to_fit.append(end_val)
    for i in range(num_points - 2):
        x_to_fit.append(random.uniform(1, 508))
        y_to_fit.append(random.uniform(start_val + (start_val - end_val), end_val - (start_val - end_val)))
    zipped = zip(x_to_fit, y_to_fit)
    zipped = sorted(zipped)
    x_to_fit, y_to_fit = zip(*zipped)
    fit = CubicHermiteSpline(x=x_to_fit, y=y_to_fit, dydx=np.zeros(num_points))
    minutely_values = fit(minute_list)
    for i in range(minutely_values.size):
        minutely_values[i] = round(minutely_values[i] * random.gauss(1, 0.0002), 2)
    return np.ndarray.tolist(minutely_values)


all_minutely_values_for_day = []

for stockID in range(50):
    all_minutely_values_for_day.append(generate_minutely_values(stockID))

live_stock_prices = []


def update_live_prices():
    live_stock_prices = []
    change_in_prices = []
    for stockID in range(50):
        live_stock_prices.append(all_minutely_values_for_day[stockID][current_minute])
        change_in_prices.append(round(all_minutely_values_for_day[stockID][current_minute] - current_day_prices[stockID], 2))

    print('minute ' + str(current_minute), live_stock_prices)
    print(change_in_prices)

    file = open('./data/stocks.json', 'r')
    data = json.load(file)
    file.close()
    for stock in range(50):
        data[stock]['value'] = live_stock_prices[stock]
        data[stock]['change'] = change_in_prices[stock]

    file = open('./data/stocks.json', 'w')
    json.dump(data, file)
    file.close()


while True:
    update_live_prices()
    time.sleep(3)
    current_minute += 1
