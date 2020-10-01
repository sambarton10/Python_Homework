'Import os & csv

import os
import csv

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

