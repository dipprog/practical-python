# report.py
#
# Exercise 2.4

import csv

from prices import read_prices


def read_portfolio(filename):
    '''
    Open a stock portfolio file into a list of dictionaries with keys name, shares and price.
    '''
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio


def make_report(portfolio, prices):
    '''
    Return a list of tuple of stock portfolio report having keys name, shares, current_price, change_price
    '''
    portfolio_report = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        current_price = prices[stock['name']]
        change_price = current_price - stock['price']
        portfolio_report.append((name, shares, current_price, change_price))
    return portfolio_report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        price_f = '$' + f'{price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {price_f:>10s} {change:>10.2f}')


def print_loss_gain(portfolio, prices, pcost):
    current_value = 0.0
    for stock in portfolio:
        if stock['name'] in prices.keys():
            current_value += int(stock['shares']) * prices[stock['name']]

    print("Portfolio Total Cost:", pcost)
    print("Current Value:", current_value)
    print(f"Gain/Loss: {(current_value-pcost):0.2f}",)


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == "__main__":
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
