#Alexandra Hart
#2/3/2025
#Lab 4

# Program Prompt: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension. Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. 

# variable dictionary:
# fName - first name
# lName - last name
# age - age
# scName - screen name
# house - house name
# dept - department nanme
# ext - phone extension
# email - email
# extRD - phone extension counter for research and development dept.
# extM - phone extension counter for marketing dept.
# extHR - phone extension counter for human resources dept.
# extA - phone extension counter for accounting dept.
# extS - phone extension counter for sales dept.
# extAu - phone extension counter for auditing dept.
# empCount - employee counter
# rdCount - counter for employees in research dept
# mCount - counter for employees in marketing
# hrCount - counter for employees in human resources
# aCount - counter for employees in accounting
# sCount - counter for employees in sales
# auCount - counter for employees in auditing

import csv

fName = []
lName = []
age = []
scName = []
house = []
dept = []
ext = []
email = []
extRD = 100
extM = 200
extHR = 300
extA = 400
extS = 500
extAu = 600
empCount = 0
rdCount = 0
mCount = 0
hrCount = 0
aCount = 0
sCount = 0
auCount = 0


print(f"{'First':8} {'Last':10} {'Email':30} {'Department':23} {'Ext':3}")

with open("week4/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        scName.append(rec[3])
        house.append(rec[4])
        email.append(rec[3] + "@westeros.net")
        if rec[4] == "House Stark":
            dept.append("Research and Development")
            extRD += 1
            ext.append(extRD)
            rdCount += 1
        elif rec[4] == "House Targaryen":
            dept.append("Marketing")
            extM += 1
            mCount += 1
            ext.append(extM)
        elif rec[4] == "House Tully":
            dept.append("Human Resources")
            extHR += 1
            hrCount += 1
            ext.append(extHR)
        elif rec[4] == "House Lannister":
            dept.append("Accounting")
            extA += 1
            aCount += 1
            ext.append(extA)
        elif rec[4] == "House Baratheon":
            dept.append("Sales")
            extS += 1
            sCount += 1
            ext.append(extS)
        else: 
            dept.append("Auditing")
            extAu += 1
            auCount += 1
            ext.append(extAu)
        empCount += 1
        
    for i in range(0, len(fName)):
        print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {dept[i]:23} {ext[i]:3}")

file = open("westeros.csv", "w")

for i in range(0, len(fName)):
    file.write(f"{fName[i]},{lName[i]},{email[i]},{dept[i]},{ext[i]}\n")
file.close()

print("File has closed.")
print(f"There are {empCount} employees in the file.")
print(f"Research and Development: {rdCount}")
print(f"Marketing: {mCount}")
print(f"Human Resources: {hrCount}")
print(f"Accounting: {aCount}")
print(f"Sales: {sCount}")
print(f"Auditing: {auCount}")
