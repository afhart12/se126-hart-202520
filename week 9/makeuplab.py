#Alexandra Hart
#SE126.04
#Make-up Lab
#3/6/2025

#Program prompt: 

#variable dictionary:

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
            print(f"we found your search for {search}, details below: ")
            print(f"{id[mid]:4} {last[mid]:10} {first[mid]:10} {class1[mid]:7} {class2[mid]:7} {class3[mid]}")

        else:
            print(f"Sorry, we did not find your search for {search} :[")
    


