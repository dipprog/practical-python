import csv


def read_prices(file):
    '''
    Read prices from a CSV file of name, price data
    '''
    rows = csv.reader(file)
    prices = {name: float(price) for name, price in rows}
    return prices
