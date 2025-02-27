# Alexandra Hart
# SE126.04
# Final Project
# 2/26/2025

# Program Description: This program provides the user with a menu of 5 options(search by name, type, or status, battle, exit program).
# Options 1, 2, and 3 allow the user to search for data based off of my premade characters.csv file. The data from the file is appended to lists to make it easy to access. The search method is sequential.
# Option 4 is a choose-your-path text game, where the program will provide a scenario and the user will select an option. This option will determine the outcome and the next scenario until the user reaches the end of the game.
# Option 5 will exit the program (and the main loop).

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

def searchFor(listName):
    for i in range(0, len(listName)): 
            if search.lower() == listName[i].lower():
                found.append([i])
        
    if not found: 
        print(f"Sorry, your search for {search} was not found :[")
    else:
        print("Your search has been found! Details below:")
        displayLabels()
        for i in range(0, len(found)):
            print(f"{name[found[i]]:22} {num[found[i]]:7} {type[found[i]]:10} {status[found[i]]:15}")
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
    print("4. Battle!")
    print("5. EXIT")
    opt = input("Select an option from the choices above(1/2/3/4/5): ")
    if opt == "1": #search by name
        found = []
        search = input("Enter the character NAME that you are searching for: ") # user enters character name
        searchFor(name)
    elif opt == "2":
        found = [] # reset found list to make it empty
        search = input("Enter the character TYPE that you are looking for: ")
        searchFor(type)
    elif opt == "3":
        found = []
        search = input("Enter the character STATUS you are searching for: ")
        searchFor(status)
    