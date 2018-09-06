#Title: Py Poll Challenge 
#By: Jennifer Clarke
#Purpose: analyze voting records, provide outcome calculations, and print the outcome to txt file

#import the os and CSV Python modules
import os
import csv

#create os path to csv resource file
csvpath = os.path.join("", "Resources", "election_data.csv")

#Create lists to hold csv data 
candidate = []
uniqueCandidate = []
can1List = []
can2List = []
can3List = []
can4List = []
#Open csv file to read data
with open(csvpath, 'r', newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header information 
    csv_header = next(csvreader)
    #loop throuhg CSV file to append candidate names to a list 
    for row in csvreader:
        candidate.append(row[2])
        num_of_votes = len(candidate)

#Creae unique canidate list
for x in candidate:
    if x not in uniqueCandidate:
        uniqueCandidate.append(x)

#Break out unuque candidates         
can1 = uniqueCandidate[0]
can2 = uniqueCandidate[1]
can3 = uniqueCandidate[2]
can4 = uniqueCandidate[3]

#Crate list for each canidate 
for can in candidate:
    if can == can1:
        can1List.append(can1)
    elif can == can2:
        can2List.append(can2)
    elif can == can3:
        can3List.append(can3)
    elif can == can4:
        can4List.append(can4)

#count the numner of times each canidate appears        
can1Count = len(can1List)
can2Count = len(can2List)
can3Count = len(can3List)
can4Count = len(can4List)

#calculate Percentage of votes for each canidate
can1Percent = (float(can1Count) / float(num_of_votes))
can2Percent = (float(can2Count) / float(num_of_votes))
can3Percent = (float(can3Count) / float(num_of_votes))
can4Percent = (float(can4Count) / float(num_of_votes))

#Calculate Winner based on popular vote
winner = 0
if can1Count >= winner:
    winner = can1
elif can2Count >= winner:
    winner = can2
elif can3Count >= winner:
    winner = can3
elif can4Count >= winner:
    winner = can4


#Print Summary Table
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(num_of_votes))
print("-----------------------")
print(can1 + ":" + str("{:.3%}".format(can1Percent)) + "("+ str(can1Count) + ")")
print(can2 + ":" + str("{:.3%}".format(can2Percent)) + "("+ str(can2Count) + ")")
print(can3 + ":" + str("{:.3%}".format(can3Percent)) + "("+ str(can3Count) + ")")
print(can4 + ":" + str("{:.3%}".format(can4Percent)) + "("+ str(can4Count) + ")")
print("-----------------------")
print("WInner: " + winner)
print("-----------------------")
