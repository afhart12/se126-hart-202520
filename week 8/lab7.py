# Alexandra Hart
# SE126.04
# Lab 7
# 2/25/2025

#Program Prompt: 

# variable dictionary:

dictionary = {}
menu = "y"
import csv

with open("week 8/words.csv") as csvfile: # file open
    file = csv.reader(csvfile)
    for rec in file:
        dictionary.update({rec[0] : rec[1]})

while menu == "y":
    print("My Programming Dictionary Menu: ")
    print("1. Show all words(including definitions)")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. EXIT")
    opt = input("Your selection(1/2/3/4): ")
    if opt == "1":
        print(f"{'WORD':15} {'DEFINITION':158}")
        for key in dictionary:
            print(f"{key:15} {dictionary[key]:158}")

    elif opt == "2":
        found = []
        search = input("What are you searching for? ")

        for key in dictionary:
            if search.lower() == dictionary[key].lower():
                found.append(key)
        
        if found != 0:
            print(f"We found your search for {search}, details below: ")
            print("-" * 50)
            for i in range(0, len(found)):
                print(f"{found[i].upper():4} {dictionary[found[i]]}")
            print("-" * 50)
        else: 
            print(f"We could not find your search for {search}.")

