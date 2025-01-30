# Alexandra Hart
# SE126.04
# 1/26/2025
# Lab 3

# Program Prompt: Construct a program that will analyze potential voters. The program should generate the following totals:

#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.
 

# Variable dictionary: 
# recordCount - amount of records in the csv file
# notEligCount - people not able to register to vote
# notRegCount - people not registered to vote
# noVoteCount - people who did not vote
# votedCount - people who voted
# num - list to store voter id numbers
# age - list to store voter ages
# reg = list to store registration status
# votes  = list to store voting status

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