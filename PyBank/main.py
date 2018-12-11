import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'res', 'budget_data.csv')

with open("budget_data.csv", newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    count = 0
    total = 0
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        #total = total+row[count]
        total = total + int(row[1])
        count = count+1
        
    print(count)   
    print(total)