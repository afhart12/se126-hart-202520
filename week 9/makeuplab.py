#Alexandra Hart
#SE126.04
#Make-up Lab
#3/6/2025

#Program prompt: build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file: students.txt

#variable dictionary:
#id = list of student id numbers from the txt file
#last = list of student last names from the txt file
# first = list of student first names from the txt file
# class1 = list of the students FIRST class from the txt file
# class2 = list of the students SECOND class from the txt file
# class3 = list of the students THIRD class from the txt file
# menu = a function used to display the menu options, returns the users choice
# choice = the users choice of menu options from the menu function
# menuLoop = a value that only changes if the user selects the EXIT option(aka "5")
# menuChoice = a value that holds the return value of "choice" variable
# found = list to hold all indexes with data that relates to 'search'
# search = a value that holds the users search query
# min = the minimum value in the binary search method, aka first searchable index
# max = the maximum value in the binary search mehtod, aka the last searchable index
# mid = the middle value in binary search that we use to compare the search entry to

id = []
last = []
first = []
class1 = []
class2 = []
class3 = []
menuLoop = "y"

import csv

#functions

def menu():
    print("--- MENU ---")
    print("1. See all student reports.")
    print("2. Search for student by ID")
    print("3. Search for a student by last name")
    print("4. View a class roster")
    print("5. EXIT")
    choice = input("Please select an option(1/2/3/4/5): ")

    return choice

with open("week 9/students.txt") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        id.append(rec[0])
        last.append(rec[1])
        first.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])


while menuLoop == "y":
    menuChoice = menu()
    if menuChoice == "1":
        print(f"{'ID':4} {'LAST NAME':10} {'FIRST NAME':10} {'CLASS 1':5} {'CLASS 2':5} {'CLASS 3'}")
        for i in range(0, len(id)):
            print(f"{id[i]:4} {last[i]:10} {first[i]:10} {class1[i]:7} {class2[i]:7} {class3[i]}")
    
    elif menuChoice == "2":
        #binary search
        search = input("Enter the student ID NUMBER for the student you are looking for: ")

        min = 0
        max = len(id) - 1
        mid = int((min + max) / 2)

        while min < max and search != id[mid]:
            if search < id[mid]:
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)
        
        if search == id[mid]:
            print(f"We found your search for {search}, details below: ")
            print(f"{id[mid]:4} {last[mid]:10} {first[mid]:10} {class1[mid]:7} {class2[mid]:7} {class3[mid]}")

        else:
            print(f"Sorry, we did not find your search for {search} :[")
    
    elif menuChoice == "3":
        #binary search
        search = input("Enter the LAST NAME of the student you are searching for: ")

        min = 0
        max = len(id) - 1
        mid = int((min + max) / 2)

        while min < max and search.lower() != last[mid].lower():
            if search.lower() < last[mid].lower():
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)
        if search.lower() == last[mid].lower():
            print(f"We found your search for {search}, details below: ")
            print(f"{id[mid]:4} {last[mid]:10} {first[mid]:10} {class1[mid]:7} {class2[mid]:7} {class3[mid]}")

        else:
            print(f"Sorry, we did not find your search for {search} :[")

    elif menuChoice == "4":
        #sequential search
        found = []

        search = input("Enter the CLASS you want to view the roster for: ")

        for i in range(0, len(class1)):
            if search.upper() == class1[i] or search.upper() == class2[i] or search.upper() == class3[i]:
                found.append(i)

        if not found: 
            print(f"Sorry, there are no students enrolled in {search.upper()}.")

        else: 
            print(f"Here is a list of students enrolled in {search.upper()}: ")
            print(f"{'ID':4} {'LAST NAME':10} {'FIRST NAME':10}")
            for i in range(0, len(found)):
                print(f"{id[i]:4} {last[i]:10} {first[i]:10}")
    elif menuChoice == "5":
        menuLoop = "n"

    else: 
        print("------ INVALID ENTRY!!! -------")

print("Goodbye.")


