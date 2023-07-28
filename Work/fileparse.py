# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # if csv file has headers, do headers processing
        if has_headers:
            # Read the file headers
            headers = next(rows)

            # If select is not set, select all the column name
            if not select:
                select = headers

            indices = [headers.index(colname) for colname in select]

        records = []
        for row in rows:
            if not row:      # Skip row with no data
                continue

            # If types is set, do type conversion
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                # Make a dictionary
                record = {colname: row[index]
                          for colname, index in zip(select, indices)}
            else:
                record = tuple(row)
            records.append(record)

    return records
