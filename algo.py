import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicHermiteSpline
import math


def evalPolynomial(poly, x):
    poly = poly[::-1]
    y = 0
    for p in range(poly.size):
        y += poly[p] * (x ** p)
    return y


def apoly(lst, x):
    total = 0
    for a in (lst):
        total = total * x + a
    return total


class Stock:
    def __init__(self):
        self.name = "placeholder"
        self.ticker = "tkr"
        self.dailyValues = []
        self.minutelyValues = []

    def generateDailyValues(self, days):
        avg_daily_return = random.uniform(-0.002, 0.005)
        daily_vol = random.uniform(0.010, 0.02)
        self.dailyValues = []
        current_price = round(random.uniform(20, 250), 2)
        self.dailyValues.append(current_price)
        for day in range(days - 1):
            price = round(self.dailyValues[day] * (1 + np.random.normal(avg_daily_return, daily_vol)), 2)
            self.dailyValues.append(price)

    def getDailyValues(self):
        return self.dailyValues

    def OLDgenerateMinutelyValuesFor(self, day):
        startVal = self.dailyValues[day]
        endVal = self.dailyValues[day + 1]
        self.minutelyValues.append(startVal)
        for minute in range(1, 509):
            targetPrice = startVal + ((endVal - startVal) * minute) / (509)
            self.minutelyValues.append(targetPrice * random.gauss(1, 0.0001))
        self.minutelyValues.append(endVal)

    def generateMinutelyValuesFor(self, day):
        startVal = self.dailyValues[day]
        endVal = self.dailyValues[day + 1]
        xToFit = []
        yToFit = []
        numPoints = random.randint(7, 13)
        xToFit.append(0)
        yToFit.append(startVal)
        xToFit.append(509)
        yToFit.append(endVal)
        for i in range(numPoints - 2):
            xToFit.append(random.uniform(1, 508))
            yToFit.append(random.uniform(startVal + (startVal - endVal), endVal - (startVal - endVal)))
        zipped = zip(xToFit, yToFit)
        zipped = sorted(zipped)
        xToFit, yToFit = zip(*zipped)
        fit = CubicHermiteSpline(x=xToFit, y=yToFit, dydx=np.zeros(numPoints))
        self.minutelyValues = fit(minute_list)
        for i in range(self.minutelyValues.size):
            self.minutelyValues[i] = self.minutelyValues[i] * random.gauss(1, 0.0002)

    def getMinutelyValues(self):
        return self.minutelyValues


no_stocks = 5
days = 365
day_list = []
minute_list = []
all_stocks = []

for x in range(days):
    day_list.append(x)

for x in range(510):
    minute_list.append(x)

for stock in range(no_stocks):
    all_stocks.append(Stock())
    all_stocks[stock].generateDailyValues(days)

# for stock in all_stocks:
#     plt.plot(day_list, stock.getDailyValues())

all_stocks[0].generateMinutelyValuesFor(100)
plt.plot(minute_list, all_stocks[0].getMinutelyValues())

plt.show()