#Import os & csv

import os
import csv



#Find the Total Profit/Loss
with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    total = 0
    for row in csv.reader(csvfile):
        total = sum(int(r[1]) for r in csv.reader(csvfile))
    print(total)

#Counting the Total Number Of Months

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    TotalMonths=len(list(reader))
    print(TotalMonths)
    
#Average change over entire period

import csv
import os

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        next(reader)
        change2=0
        
        for row in reader:
             
             print(row['Profit/Losses'])
             
        
        
#Subtracting every current row from previous row, taking sum of all rows then finding average.

        
        
#Finding greatest increase between months



#Finding greatest decrease between months
   
    
print('Finacial Analysis')
print('-----------------')
print('Total Months:', TotalMonths)
print('Total Profit/Losses:', total)


newdict = {'Date': 'Jun-2016', 'Profit/Losses': '712961'}
print(newdict['Profit/Losses'])

list2=[2,4,7,8]
list2.append(10)
for x in range(5):
    print(list2[x])

list3=[]
for x in range(5):
    list3.append(list2[x]-list2[x-1])
    
print(list3[1:4])

list5=[10,20,30,40]

list6=[]

for x in range(4):
    list6.append(list5[x]-list5[x-1])
print(list6)
    