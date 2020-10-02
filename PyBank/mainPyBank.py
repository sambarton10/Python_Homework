'Import os & csv

import os
import csv

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
        
    total = 0
    for row in csv.reader(csvfile):
        total = sum(int(r[1]) for r in csv.reader(csvfile))
    print(total)

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    TotalMonths=len(list(reader))
    print(TotalMonths)
    
    
    

