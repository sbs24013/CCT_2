#!/usr/bin/env python3

# sales breakdown by all stores.

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
# Find the breaking the sales down by store
import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		# These are names of the columns/ attributes given to the data file
		date, time, store, item, cost, payment = data
		print("{0}\t{1}".format(store, cost))
