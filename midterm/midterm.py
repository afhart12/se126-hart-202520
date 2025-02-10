#Alexandra Hart
#Midterm Prompt 1

# Program Prompt: Create a program that processes through the westeros.csv file, stores the data into 1D lists, and prints the data to the user. Create a unique office number for each employee starting at 100. Create a new csv file and write the data to the file. Then, create a sequential search system allowing the user to search by email or department. The user should not be able to exit the progrma unless they select the exit option in the search menu. 

# variable dictionary:
# fName = first name of employee
# lName = last name of employee
# email = email of employee
# dept = department of employee
# ext = phone extension of employee
# office = office number of employee
# num = a counter that I made to make unique office numbers starting at 100
# menu = holds a value of which selection the user makes for the search menu options, defaults at 1 so the while loop will run
# records = counter for total records processed
# found = a list that remains empty unless a search value is found, resets each time you choose a menu option
# search = an input value that the users search value is stored in

import csv

#------ creating empty lists for each field
fName = []
lName = []
email = []
dept = []
ext = []
office = [] # this one is for the office number that will be created
num = 100 # this one is going to be a counter to make unique office numbers starting at 100
menu = 1
records = 0

#---- file is open --------
with open("midterm/westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        fName.append(record[0])
        lName.append(record[1])
        email.append(record[2])
        dept.append(record[3])
        ext.append(record[4])
        num += 1
        office.append(num)
        records += 1

# ---- disconnected from file -------

print(f"{'FIRST':9} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'PHONE EXT.':7} {'OFFICE #':3}")
# process lists and print data to console
for i in range(0, len(fName)):
    print(f"{fName[i]:9} {lName[i]:10} {email[i]:30} {dept[i]:23} {ext[i]:8} {office[i]:4}")
print(f"Records processed: {records}")
print("--------------------------------------")

# creates new csv file and writes data to it
file = open("midterm_choice1.csv", "w")
for i in range(0, len(fName)):
    file.write(f"{fName[i]},{lName[i]},{email[i]},{dept[i]},{ext[i]},{office[i]}\n")
file.close()

# setup found variable, search menu, and search input for user
while menu != "3":
    found = []
    menu = input("1. Search by EMAIL  2. Search by DEPARTMENT 3. EXIT (1 / 2 / 3): ")
# perform search based on which option the user selects
    if menu == "1":
        search = input("Please enter a valid email for the employee: ")

        for i in range(0, len(email)):
            if search.lower() == email[i].lower():
                found.append(i)
        if not found: # if the found list is empty / no value stored to it
            print("Your search for {search} was NOT FOUND :(")
        else: 
            print(f"{'FIRST':9} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'PHONE EXT.':7} {'OFFICE #':3}")
            for i in range(0, len(found)): # prints data based on which index it was found in
                
                print(f"{fName[found[i]]:9} {lName[found[i]]:10} {email[found[i]]:30} {dept[found[i]]:23} {ext[found[i]]:8} {office[found[i]]:4} ")
    elif menu == "2":
        search = input("Please enter a department name to find employees: ")
        for i in range(0, len(dept)):
            if search.lower() == dept[i].lower():
                found.append(i)
        if not found: 
            print(f"Your search for {search} was NOT FOUND :(")
        else: 
            print(f"{'FIRST':9} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'PHONE EXT.':7} {'OFFICE #':3}")
            for i in range(0, len(found)):
                print(f"{fName[found[i]]:9} {lName[found[i]]:10} {email[found[i]]:30} {dept[found[i]]:23} {ext[found[i]]:8} {office[found[i]]:4} ")

print("Goodbye.")



