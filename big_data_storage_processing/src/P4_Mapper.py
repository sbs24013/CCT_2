#!/usr/bin/env python3

# Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        # These are names of the columns/ attributes given to the data file
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(1, cost))
