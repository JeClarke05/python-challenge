#Title: Py Poll Challenge 
#By: Jennifer Clarke
#Purpose: analyze voting records, provide outcome calculations, and print the outcome to txt file

#import the os and CSV Python modules
import os
import csv

#create os path to csv resource file
csvpath = os.path.join("", "Resources", "election_data.csv")

#Create variables to track changes
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

can1Percent = (float(can1Count) / float(num_of_votes)) * 100
can2Percent = (float(can2Count) / float(num_of_votes)) * 100
can3Percent = (float(can3Count) / float(num_of_votes)) * 100
can4Percent = (float(can4Count) / float(num_of_votes)) * 100

#Print Summary Table

print("Election Results")
print("-----------------------")
print("Total Votes: " + str(num_of_votes))
print("-----------------------")
print(can1 + ":" + str(round(can1Percent, 3 )) + "% " + "("+ str(can1Count) + ")")
print(can2 + ":" + str(round(can2Percent, 3)) + "% " + "("+ str(can2Count) + ")")
print(can3 + ":" + str(round(can3Percent, 3)) + "% " + "("+ str(can3Count) + ")")
print(can4 + ":" + str(round(can4Percent, 3)) + "% " + "("+ str(can4Count) + ")")
print("-----------------------")

print("-----------------------")
