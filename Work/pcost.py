# pcost.py
#
# Exercise 1.27

import sys


def portfolio_cost(filename):
    total_cost = 0
    try:
        with open(filename, 'rt') as f:

            next(f)  # Skipping the headers
            for line in f:
                row = line.split(',')
                total_cost += int(row[1]) * float(row[2].strip())

    except FileNotFoundError:
        print("File not found. Ensure that you have correct file name.")
    except ValueError:
        print("Unable to convert a value to int.")

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
