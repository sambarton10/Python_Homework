
'Import os & csv

import os
import csv

with open('/Users/sambarton/Python_Homework1/PyPoll/Resources/election_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

'Total Number of Months



'Total Number of "Profit/Losses" Over The Period

'Average Of Changes "Profit/Losses" Over The Period

'Greatest Increase In Profits

'Greatest Decrease In Losses

