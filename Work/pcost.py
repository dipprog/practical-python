# pcost.py
#
# Exercise 1.27

import sys
import csv


def portfolio_cost(filename):
    ''' Computes the total cost (shares * price) of a portfolio file'''
    with open(filename, 'rt') as f:
        total_cost = 0
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')
    return total_cost


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total Cost:', cost)
