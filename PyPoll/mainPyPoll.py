
#Import os & csv

import os
import csv

with open('/Users/sambarton/Python_Homework1/PyPoll/Resources/election_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    TotalVotes = 0
    for row in reader:
        TotalVotes += 1   

            
    
    print('Election Results')
    print('-------------------------')
    print('Total Votes:', TotalVotes)
    print('-------------------------')
    print('Khan:')
    print('Correy:')
    print('Li:')
    print('OTooley:')
    print('-------------------------')
    print('Winner:') 
    print('-------------------------')
