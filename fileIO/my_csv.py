#!/usr/bin/python3

import csv

"""

The csv module uses csv.reader() to return a list

"""
with open('parse.csv', 'r') as csv_file:
    csv_data = csv.DictReader(csv_file) #lists will be returned
    for line in csv_data:
        print(line)
