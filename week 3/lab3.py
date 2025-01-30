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

num = []
age =[]
reg = []
votes = []

with open("week 3/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        num.append(record[0])
        age.append(int(record[1]))
        reg.append(record[2])
        votes.append(record[3])
        recordCount += 1

for index in range(0, len(age)):
    if age[index] < 18:
        notEligCount += 1
    elif age[index] >= 18 and reg[index] == "N":
        notRegCount += 1
    elif reg[index] == "Y" and votes[index] == "N":
        noVoteCount += 1
    elif votes[index] == "Y":
        votedCount += 1
print(f"Records Processed: {recordCount}")
print(f"Not Able to Register: {notEligCount}")
print(f"Old Enough to Vote, Not Registered: {notRegCount}")
print(f"Eligible, Didn't Vote: {noVoteCount}")
print(f"Voted: {votedCount}")