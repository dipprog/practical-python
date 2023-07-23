# report.py
#
# Exercise 2.4

import csv

from prices import read_prices
from pcost import portfolio_cost


def read_portfolio(filename):
    '''Open a portfolio file and reads it into a list of tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            holding_dict = {
                'name': holding[0], 'shares': holding[1], 'price': holding[2]}
            portfolio.append(holding_dict)
    return portfolio


portfolio = read_portfolio('Data/portfolio.csv')
pcost = portfolio_cost('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

current_value = 0.0

for s in portfolio:
    if s['name'] in prices.keys():
        current_value += s['shares'] * prices[s['name']]

print("Portfolio Total Cost:", pcost)
print("Current Value:", current_value)
print(f"Gain/Loss: {(current_value-pcost):0.2f}",)
