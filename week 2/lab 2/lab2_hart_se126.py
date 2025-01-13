# Alexandra Hart
# SE 126.04
# Lab 2
# 1/13/2025

# Program Prompt: 

# Variable Dictionary:
# (I know this is for variables but this beginning part is for me so I can reference what each record in the data is)
# record[0] is type. record[1] is brand. record[2] is CPU. record[3] is RAM.
# record[4] is 1st disk, record[5] is no HDD, record[6] is either 2nd disk or OS, record[7] is either OS or YR
# record[8] is YR(if it exists)

import csv

with open("week 2/lab 2/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    print("{'Type':7} {'Brand':7} {'CPU':3} {'RAM':3} {'1st Disk':6} {'No HDD':2} {'2nd Disk':6} {'OS':4} {'YR':3}")
    for record in file:
        if record[0] == "D":
            record[0] = "Desktop"
        else: record[0] == "Laptop"
        float(record[5])
        if record[5] == 1:
            os = record[6]
        else: os = record[7]
        if record[1] == "DL":
            record[1] = "Dell"
        elif record[1] == "GW":
            record[1] = "Gateway"
    
