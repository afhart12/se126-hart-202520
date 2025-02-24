# Alexandra Hart
# SE126.04
# Lab 6 
# 02/24/2025

#Program prompt(and additional personal notes): Print an airplane seating chart, allow user to enter which seat they want and update the chart until either every seat is full or the user wants to stop.
# ask user for row number, ask for seat letter, check for validity, place x at that coordinate
# if seat == x, they cant sit there, else, change value to x
# if user wants to sit in row 1, 1st position, index 0, subtract 1 from user row entry
# row - 1 = index
# do not need index to hold rows, a list, b list, c list, d list 

aSeats = ["A","A","A","A","A","A","A"]
bSeats = ["B","B","B","B","B","B","B"]
cSeats = ["C","C","C","C","C","C","C"]
dSeats = ["D","D","D","D","D","D","D"]
answer = "y"

def display(): # I am aware that I could've done this differently and there was a WAY easier way with a for loop but I already typed it all out so its kinda pointless now...
    print(f"Row 1: {aSeats[0]:2} {bSeats[0]:4} {cSeats[0]:2} {dSeats[0]:2}")
    print(f"    2: {aSeats[1]:2} {bSeats[1]:4} {cSeats[1]:2} {dSeats[1]:2}")
    print(f"    3: {aSeats[2]:2} {bSeats[2]:4} {cSeats[2]:2} {dSeats[2]:2}")
    print(f"    4: {aSeats[3]:2} {bSeats[3]:4} {cSeats[3]:2} {dSeats[3]:2}")
    print(f"    5: {aSeats[4]:2} {bSeats[4]:4} {cSeats[4]:2} {dSeats[4]:2}")
    print(f"    6: {aSeats[5]:2} {bSeats[5]:4} {cSeats[5]:2} {dSeats[5]:2}")
    print(f"    7: {aSeats[6]:2} {bSeats[6]:4} {cSeats[6]:2} {dSeats[6]:2}")

while answer == "y":
    answer = input("Would you like to reserve an airplane seat?: (y/n) ").lower()
    display()
    row = input("Please select a row number: ")
    seat = input("Please select a seat letter: (A/B/C/D) ").upper()
    index = int(row) - 1
    if seat == "A":
        if aSeats[index] == "X":
            print("This seat is taken. Please try again.")
        else:
            aSeats[index] = "X"
    elif seat == "B":
        if bSeats[index] == "X":
            print("This seat is taken. Please try again.")
        else:
            bSeats[index] = "X"
    elif seat == "C":
        if cSeats[index] == "X":
            print("This seat is taken. Please try again.")
        else:
            cSeats[index] = "X"
    elif seat == "D":
        if dSeats[index] == "X":
            print("This seat is taken. Please try again.")
        else:
            dSeats[index] = "X"
    else:
        print("INVALID ENTRY, PLEASE TRY AGAIN.")
    display()


print("Goodbye.")
