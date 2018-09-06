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
    #Loop through csv data to pull info from CSV file and organize in to variables and lists
    for row in csvreader:
        monthYear.append(row[0])
        num_months = len(monthYear)
        rev.append(row[1])
        #calculate total net by adding the contents of the profit/losses column
        totalNet = totalNet + int(row[1])
    
#loop though the revenue list to calculate the Month over Month change and append to new list
for x in range(1, len(rev)):
        diff = (int(rev[x])) - int(rev[x-1])
        momDifList.append(diff)

#find max value in the month over month differences for the greatest increase in prophet      
Gincrease = max(momDifList)
Gdecrease = min(momDifList)

#use the index of the greatest increase and decrease value to find the coresponding month
indexGincrease = momDifList.index(Gincrease)
indexGdecrease = momDifList.index(Gdecrease)

GincreaseMon = monthYear[indexGincrease + 1]
GdecreaseMon = monthYear[indexGdecrease + 1]

#This is my solution to reformat the date to MMM-YYYY. Could not get the date formatter to work but this was a fun alternative :)
splitI = GincreaseMon.split("-")
splitIM = splitI[1]
splitIY = splitI[0]

splitD = GdecreaseMon.split("-")
splitDM = splitD[1]
splitDY = splitD[0]

#use the total of the difference list divided by the length of the difference list to get the average change
aveChange = sum(momDifList) / len(momDifList)   

#Print Financial Analysis Header 
print("Financial Analysis")
print("------------------------------") 
#Print summary output 
print("Total Months: " + str(num_months))
print("Total: $" + str(totalNet))
print("Average Change: $" + str(round(aveChange, 2)))
print("Greatest Increase in Profits: " + splitIM + "-20" + splitIY + " ($" + str(Gincrease) + ")")
print("Greatest Decrease in Profits: " + splitDM + "-20" + splitDY + " ($" + str(Gdecrease) + ")")

#output summary to txt file 
text_file = open("Output.txt", "w")
text_file.write(f'Financial Analysis\n')
text_file.write(f'------------------------------\n')
text_file.write(f'Total Months: {str(num_months)}\n')
text_file.write(f'Total: ${str(totalNet)}\n')
text_file.write(f'Average Change: ${str(round(aveChange, 2))}\n')
text_file.write(f'Greatest Increase in Profits: {splitIM}-20{splitIY} (${str(Gincrease)})\n')
text_file.write(f'Greatest Decrease in Profits: {splitDM}-20{splitDY} (${str(Gdecrease)})\n')
text_file.close()
