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
# name = list to hold all of the names found in rec[0] of the csv file
# num = list to hold all of the id numbers found in rec[1]
# type = list to hold all of the character types found in rec[2]
# status = list to hold all of the character status values, all found in rec[3]
# menu = a y or n value used to run the main menu loop
# displayLabels = see notes next to the function
# optionChoice = see notes next to the function
# opt = menu option, the value contains user input of which menu choice they select
# found =  a list that holds values that match search criteria
# search = a value that holds the search criteria entered by the user
# ready = a y or n value that is determined by user input, used to determine whether or not to proceed to the text adventure game or return to the menu
# start = if ready == "y", start = "y", and when start == "y" the battle loop begins and the text adventure will start
# when start == "n", the battle loop ends
# userName = user input of the users name, displayed in the text adventure
# q1, q2, q3, q4, q5 = the values that hold the users choice based on what they enter after they read the question. Based on what these values are, the game will decide whether to continue or loop back to the start/menu


# variables and lists ----------------------
name = []
num = []
type = []
status = []
menu = "y"
# function(s) ----------------------------------------
def displayLabels(): #prints labels for any instance in which the program will have to display data, used in menu options 1, 2, 3, and 4
    print(f"{'NAME':22} {'ID NUM':7} {'TYPE':10} {'STATUS':15}")
    print("-" * 50)

def optionChoice(question): # the paramater value is the question input value where the user will enter an option from the ones provided
    if question != "1" or "2": #if the user enters anything other than a "1" or "2"
        print("You have been DEFEATED! Better luck next time!") # the user will lose the game!
        #(this was my best idea, there would be way too many loops if I did the other option I thought of)
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
        print("One option will be labeled as 1, and the other one will be labeled as 2. Please only enter 1 or 2, or you will LOSE THE BATTLE!")
        ready = input("Ready to get started? (Y/N): ")
        start = ""
        if ready.lower() == "y":
            start = "y"
        else: 
            print("Looks like you aren't ready to battle yet. Come back when you're ready!")
        while start == "y":
            print("Let's get started.")
            userName = input("Please enter YOUR name: ")
            print(f"Welcome, {userName}! Today, you will embark on an adventure with Finn and Jake, two of Ooo's greatest warriors!")
            print("You get a call from Princess Bubblegum. She seems worried.")
            print("Do you respond to the call for adventure?")
            print("1: Yes, rush to the Candy Kingdom!")
            print("2: No, stay at home and make bacon pancakes!")
            q1 = input("Your choice(1/2): ") # for reference, a GOOD CHOICE will result in the game continuing, and a BAD CHOICE will end the game and return to the menu
            optionChoice(q1) #using my handmade function to check the validity of the user input, see the function section above for details
            if q1 == "1": #good choice - question 1
                print("Good choice! You rush to the castle to find that one of Princess Bubblegum's experiments has gone wrong!")
                print("There are a bunch of infected candy people, wandering around, searching to infect more citizens!")
                print("What do you do?")
                print("1: Immediately charge at the infected citizens and try to wipe them out before they infect more citizens!")
                print("2: Go see Princess Bubblegum and ask for her advice.")
                q2 = input("Your choice(1/2): ")
                optionChoice(q2)
                if q2 == "1": #bad choice - question 2
                    print(f"Finn, Jake, and {userName} charge at the infected candy people! Jake gets bitten and infected, Finn gets overpowered by the infected, and you face an angry Princess.")
                    print("She yells from her window and informs you that SHE HAD THE ANTIDOTE! She needed YOU to claim it and use it on the people!")
                    print("YOU LOSE!")
                    start = "n"
                elif q2 == "2": #good choice - question 2
                    print("The three of you run to Princess Bubblegum's quarters in the castle. She is there, worried, but brewing up a solution.")
                    print("You spot a glowing bucket on her desk. She hands the bucket containing the ANTIDOTE to you and tells you to use it on the people.")
                    print("You rush back outside. ")
                    q3 = input("Your choice(1/2): ")
                    optionChoice(q3)
                    if q3 == "1": #good choice - question 3
                        print("")
                        q4 = input("Your choice(1/2): ")
                        optionChoice(q4)
                        if q4 == "1": #bad choice - question 4
                            print("")
                            start = "n"
                        elif q4 == "2": #good choice - question 4
                            print("")
                            q5 = input("Your choice(1/2): ")
                            optionChoice(q5)
                            if q5 == "1": #user wins the game
                                print("")
                                start = "n" # this value HAS to become "n" in order to end the game, regardless of what choice the user picks for q5!!
                            elif q5 == "2": # user loses, bad choice - question 5
                                print("")
                                start = "n"
                    elif q3 == "2": #bad choice - question 3
                        print("")
                        start = "n"
            elif q1 == "2": #bad choice - question 1
                print("You have chose to stay at home with Jake and make bacon pancakes.")
                print("Finn responds to the call and gets defeated in battle! Princess Bubblegum is VERY angry!!")
                print("You LOSE!")
                start = "n"
            

