import csv


def read_prices(filename: str) -> dict:
    '''
    Read prices from a CSV file of name, price data
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        prices = {name: float(price) for name, price in rows}
    return prices
