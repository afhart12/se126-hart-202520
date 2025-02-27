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


