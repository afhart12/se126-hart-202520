# Alexandra Hart
# SE126.04
# Lab 1
# 1/9/2025

# Program Prompt: a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

# Variable dictionary:
# answer = value that runs the main loop, determines if the user will enter more data or not
# maxCapacity = the maximum capacity of the meeting room entered by the user
# pplAttending = the amount of people attending the meeting entered by the user
# dif = the value that holds the difference of maxCapacity - pplAttending to determine the amount of people over/under capacity



answer = "y"
maxCapacity = 0
pplAttending = 0
dif = 0
# Functions ---------
def difference():
    dif = maxCapacity - pplAttending
    if dif < 0:
       dif = dif * -1
       print(f"You must remove {dif} people from the room to have the meeting.")
    elif dif == 0:
        print("You have perfectly met the requirements and you are clear to have the meeting in this room.")
    elif dif > 0:
       print(f"You can add {dif} people to the room and still meet the requirements.")

def decision():
    answer = input("Would you like to check another room?: (y/n) ").lower()
    if answer != "y" and answer != "n":
        answer = input("Invalid entry, please try again. Would you like to check another room? (y/n): ")
    return answer
#--------------------

while answer == "y":
    meetingName = input("Enter the name of the meeting: ")
    pplAttending = float(input("Enter the amount of people attending the meeting: "))
    maxCapacity = float(input("Enter the maximum capacity of people in the room as per fire regulations: "))
    difference()
    answer = decision()
print("Goodbye.")


    