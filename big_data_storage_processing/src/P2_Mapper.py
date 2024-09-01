#!/usr/bin/python3

# Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# Find the Sales breakdown by product category across all of our stores in the purchases.txt dataset.

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
    	# These are names of the columns/ attributes given to the data file
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(item, cost))
