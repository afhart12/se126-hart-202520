# Alexandra Hart
# SE126.04
# Final Project
# 2/26/2025

# Program Description: This program provides the user with a menu of 5 options(search by name, type, or status, battle, exit program).
# Options 1, 2, and 3 allow the user to search for data based off of my premade characters.csv file. The data from the file is appended to lists to make it easy to access. The search method is sequential.
# Option 4 is a choose-your-path text game, where the program will provide a scenario and the user will select an option. This option will determine the outcome and the next scenario until the user reaches the end of the game.
# Option 5 will display all of the data from the csv file in a neat format.
# Option 6 will exit the program (and the main loop).

# Variable Dictionary:

# variables and lists ----------------------
name = []
num = []
type = []
status = []
menu = "y"
# function(s) ----------------------------------------
def displayLabels():
    print(f"{'NAME':22} {'ID NUM':7} {'TYPE':10} {'STATUS':15}")
    print("-" * 50)

#connected to file -----------------------------
import csv
with open("final project/characters.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        name.append(rec[0])
        num.append(rec[1])
        type.append(rec[2])
        status.append(rec[3])

# disconnected from file ---------------------------

while menu == "y":
    print("--- IT'S ADVENTURE TIME! ---")
    print("1. Search by name")
    print("2. Search by character type")
    print("3. Search by character status")
    print("4. Show all characters and associated information")
    print("5. Battle!")
    print("6. EXIT")
    opt = input("Select an option from the choices above(1/2/3/4/5): ")
    if opt == "1": #search by name
        found = [] # list to store indices of potential results
        search = input("Enter the character NAME that you are searching for: ") # user enters character name
        for i in range(0, len(name)):
            if search.lower() in name[i].lower():
                found.append(i)
        
        if not found:
            print(f"Sorry, your search for {search} was NOT FOUND :[")
        else:
            print(f"Your search for {search} was found! Details below: ")
            displayLabels()
            for i in range(0, len(found)):
                print(f"{name[found[i]]:22} {num[found[i]]:7} {type[found[i]]:10} {status[found[i]]:15}")
    
    elif opt == "2":
        found = [] # reset found list to make it empty
        search = input("Enter the character TYPE that you are looking for: ")
        for i in range(0, len(type)):
            if search.lower() in type[i].lower():
                found.append(i)
        
        if not found:
            print(f"Sorry, your search for {search} was NOT FOUND :[")
        else:
            print(f"Your search for {search} was found! Details below: ")
            displayLabels()
            for i in range(0, len(found)):
                print(f"{name[found[i]]:22} {num[found[i]]:7} {type[found[i]]:10} {status[found[i]]:15}")
    
    elif opt == "3":
        found = []
        search = input("Enter the character STATUS you are searching for: ")
        for i in range(0, len(status)):
            if search.lower() in status[i].lower():
                found.append(i)
        
        if not found:
            print(f"Sorry, your search for {search} was NOT FOUND :[")
        else:
            print(f"Your search for {search} was found! Details below: ")
            displayLabels()
            for i in range(0, len(found)):
                print(f"{name[found[i]]:22} {num[found[i]]:7} {type[found[i]]:10} {status[found[i]]:15}")

    elif opt == "4":
        displayLabels()
        for i in range(0, len(name)):
            print(f"{name[i]:22} {num[i]:7} {type[i]:10} {status[i]:15}")
    
    elif opt == "5":
        print("Your journey begins! Here's a quick tutorial to get you started:")
        print("You will be given two options for each scenario.")
        print("One option will be labeled as A, and the other one will be labeled as B. Please only enter A or B.")
        ready = input("Ready to get started? (Y/N): ")
        if ready.lower() == "y":
            start = "y"
        else: 
            print("Looks like you aren't ready to battle yet. Come back when you're ready!")
        if start == "y":
            print("Perfect! Let's get started.")
            userName = input("Please enter YOUR name: ")
            print(f"Welcome, {userName}! Today, you will embark on an adventure with Finn and Jake, two of Ooo's greatest warriors!")
            print("You get a call from Princess Bubblegum. She seems worried.")
            print("Princess Bubblegum: Come quick!")
    