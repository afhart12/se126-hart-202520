# Alexandra Hart
# SE126.04
# Lab 1
# 1/9/2025

# Program Prompt: a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

# Variable dictionary:

answer = "y"
maxCapacity = 0
pplAttending = 0

# Functions ---------
def difference():
    dif = maxCapacity - pplAttending
    if dif < 0:
        remove = dif * -1
    elif dif > 0:
        print(f"You can still add {dif} people to the room and meet fire regulations!")
    elif dif == 0:
        print("You have met the fire regulations, but you cannot add any additional people to the room.")
#--------------------

while answer == "y":
    float(input(print("Enter the amount of people attending the meeting: ")))
    float(input(print("Enter the maximum capacity of people in the room as per fire regulations: ")))
    