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

  
#Subtracting every current row from previous row, taking sum of all rows then finding average.
import csv
import os

with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader)
    change2=[]
    change3=[]
    
    for row in reader:
        
        change2.append(row ['Profit/Losses'])
        
        
with open('/Users/sambarton/Python_Homework1/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        change3.append(row ['Profit/Losses'])
        
        
#Finding greatest increase between months



#Finding greatest decrease between months
   
    
print('Finacial Analysis')
print('-----------------')
print('Total Months:', TotalMonths)
print('Total Profit/Losses:', total)
print('Average Change: $')
print('Greatest Increase of Profits In Period:')
print('Greatest Decrease of Profits In Period:')


newdict = {'Date': 'Jun-2016', 'Profit/Losses': '712961'}
print(newdict['Profit/Losses'])

list2=[3,4,6,60]
sumlist2=sum(list2)
list2.append(10)
for x in range(5):
    print(list2[x])

list3=[]
for x in range(5):
    list3.append(list2[x]-list2[x-1])
    
print(list3[1:4])

list5=[10,20,30,40]
sumlist5=sum(list5)
print(sumlist5)
list6=[]

for x in range(4):
    list6.append(list5[x]-list5[x-1])
print(list6[1:])
    
list10=[]
list10=(list5[x]-list2[x])

print(list10)

