# Alexandra Hart
# SE 126.04
# Lab 2
# 1/13/2025

# Program Prompt: Create a program that processes the given file, displays the data correctly, and gives a final count of how many computers were listed in the file

# Variable Dictionary:
# (I know this is for variables but this beginning part is for me so I can reference what each record in the data is)
# record[0] is type. record[1] is brand. record[2] is CPU. record[3] is RAM.
# record[4] is 1st disk, record[5] is no HDD, record[6] is either 2nd disk or OS, record[7] is either OS or YR
# record[8] is YR(if it exists)
# totalRecords = a counter for how many computers are listed in the file
# num = the number associated with record 5, indicating if there is 1 or 2 hard drives
# disk2 = record 6 if applicable
# os = operating system, record 6 or 7
# yr = year, record 7 or 8

import csv

with open("week 2/lab 2/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)
    totalRecords = 0

    print(f"{'Type':7} {'Brand':7} {'CPU':3} {'RAM':3} {'1st Disk':6} {'No HDD':4} {'2nd Disk':10} {'OS':4} {'YR':3}")
    for record in file:
        totalRecords += 1
        if record[0] == "D":
            record[0] = "Desktop"
        elif record[0] == "L": record[0] == "Laptop"
        num = int(record[5])
        os = record[6]
        yr = record[7]
        if num == 2:
            disk2 = record[6]
            os = record[7]
            yr = record[8]
        else: disk2 = "n/a"
        if record[1] == "DL":
            record[1] = "Dell"
        elif record[1] == "GW":
            record[1] = "Gateway"
        print(f"{record[0]:7} {record[1]:7} {record[2]:3} {record[3]:3} {record[4]:10} {record[5]:7} {disk2:6} {os:4} {yr:3}")

    print(f"TOTAL COMPUTERS: {totalRecords}")
    
    
