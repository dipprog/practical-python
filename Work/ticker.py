# ticker.py

from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def print_ticker(rows, formatter):
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        rowdata = [row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"]
        formatter.row(rowdata)

def ticker(portfile, logfile, fmt):
    import report
    import tableformat

    portfolio = report.read_portfolio(portfile)
    logs = follow(logfile)
    rows = parse_stock_data(logs)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    print_ticker(rows, formatter)

if __name__ == "__main__":
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
