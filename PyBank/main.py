#Title: Py Bank Challenge 
#By: Jennifer Clarke
#Purpose: analyze PyBank records and provide summary calculations as well as export a txt file.

#import the os and CSV Python modules
import os
import csv

#create os path to csv resource file
csvpath = os.path.join("", "Resources", "budget_data.csv")

#Create variables to track changes
monthYear = []
totalNet = 0
rNum = 0
rev = []
momDifList = []

#Open csv file to read data
with open(csvpath, 'r', newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    
    #Skip header of CSV file
    csv_header = next(csvreader)
    #Loop through csv data
    for row in csvreader:
        #add date to list and count number of items in list to get number of months
        monthYear.append(row[0])
        num_months = len(monthYear)
        rev.append(row[1])
        #calculate total net 
        totalNet = totalNet + int(row[1])
    

for x in range(1, len(rev)):
        diff = (int(rev[x])) - int(rev[x-1])
        momDifList.append(diff)
        
Gincrease = max(momDifList)
Gdecrease = min(momDifList)

indexGincrease = momDifList.index(Gincrease)
indexGdecrease = momDifList.index(Gdecrease)

GincreaseMon = monthYear[indexGincrease + 1]
GdecreaseMon = monthYear[indexGdecrease + 1]

aveChange = sum(momDifList) / len(momDifList)   

#Print Financial Analysis Header 
print("Financial Analysis")
print("------------------------------") 
#Print total months to the summary output 
print("Total Months: " + str(num_months))
print("Total: $" + str(totalNet))
print("Average Change: " + str(round(aveChange, 2)))
print("Greatest Increase in Profits: " + GincreaseMon + "(" + str(Gincrease) + ")")
print("Greatest Decrease in Profits: " + GdecreaseMon + "(" + str(Gdecrease) + ")")