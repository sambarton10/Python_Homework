#Import os & csv

import os
import csv


#Find the Total Profit/Loss
with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    total = 0
    for row in csv.reader(csvfile):
        total = sum(int(r[1]) for r in csv.reader(csvfile))

#Counting the Total Number Of Months

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    TotalMonths=len(list(reader))
    
#Subtracting every current row from previous row, taking sum of all rows then finding average.

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    
#Finding greatest increase between months




#Finding greatest decrease between months
   
    
    print('Finacial Analysis')
    print('-----------------')
    print('Total Months:', TotalMonths)
    print('Total Profit/Losses:', total)
    print('Average Change: $')
    print('Greatest Increase of Profits In Period:')
    print('Greatest Decrease of Profits In Period:')

budget_file = os.path.join("Python_Homework1", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {TotalMonths}\n")
    outfile.write(f"Total:  ${total}\n")
    outfile.write(f"Average Change:\n")
    outfile.write(f"Greatest Increase in Profits:")
    outfile.write(f"Greatest Decrease in Losses:")

