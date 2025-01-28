# Alexandra Hart
# SE126.04
# 1/26/2025
# Lab 3

# Program Prompt: 

# Variable dictionary:

import csv

recordCount = 0
notEligCount = 0
notRegCount = 0
noVoteCount = 0
votedCount = 0

with open("week 3/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        num = record[0]
        age = int(record[1])
        reg = record[2]
        votes = record[3]
        recordCount += 1
        if age < 18:
            notEligCount += 1
        elif age >= 18 and reg == "N":
            notRegCount += 1
        elif reg == "Y" and votes == "N":
            noVoteCount += 1
        elif votes == "Y":
            votedCount += 1
    print(f"Records Processed: {recordCount}")
    print(f"Not Able to Register: {notEligCount}")
    print(f"Old Enough to Vote, Not Registered: {notRegCount}")
    print(f"Eligible, Didn't Vote: {noVoteCount}")
    print(f"Voted: {votedCount}")