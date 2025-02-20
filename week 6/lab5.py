#Alexandra Hart
# Lab 5
# SE126.04
# February 14, 2025

# Prompt: with the book list csv file, provide the following menu and options to the user and perform the task when it is chosen:

# library menu:
# 1 - all data, print statement
# 2 - title keyword, sequential search
# 3 - author, sequential
# 4 - genre, sequential
# 5 - one specific library number item, binary search
# 6 - status of avaliable, sequential
# 7 - status of on loan, sequential
# 8 - exit the loop

# variable dictionary
import csv
libnum = []
title = []
author = []
genre = []
pgcount = []
status = []
found = []
menu = "y" # this is to start the main while loop
def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

print("----------------------------------------------------------------\n")

#-------

with open("week 6/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        libnum.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pgcount.append(rec[4])
        status.append(rec[5])


while menu == "y":
    print("Welcome to the library menu!")
    print("1. Show All Titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show All Avaliable Books")
    print("7. Show all On Loan Books")
    print("8. EXIT")
    opt = input("Select a number(1/2/3/4/5/6/7/8): ")

    if opt not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("INVALID ENTRY!!! Please try again.")

    elif opt == "1":
        for i in range(0, len(libnum)):
            print(f"{libnum[i]:7}  {title[i]:32}  {author[i]:25}  {genre[i]:15} {pgcount[i]:4} {status[i]:9}")

    elif opt == "2":
        found = []
        search = input("What title are you searching for?: ").lower()

        for i in range(0, len(title)):
            if search in title[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry, your search for {search} was not found :[")
        
        else:
            print(f"Your search for {search} has been found!")
            for i in range(0, len(found)):
                print(f"{libnum[found[i]]:7}  {title[found[i]]:32}  {author[found[i]]:25}  {genre[found[i]]:15} {pgcount[found[i]]:4} {status[found[i]]:9}")
    
    elif opt == "3":
        found = []

        search = input("Which author are you searching for?: ")

        for i in range(0, len(author)):
            if search.lower() == author[i].lower():
                found.append(i)
            
        if not found:
            print(f"Sorry, your search for {search} was not found.")

        else:
            print(f"Your search for {search} has been found!")
            for i in range(0, len(found)):
                print(f"{libnum[found[i]]:7}  {title[found[i]]:32}  {author[found[i]]:25}  {genre[found[i]]:15} {pgcount[found[i]]:4} {status[found[i]]:9}")

    elif opt == "4":
        found = []

        search = input("What genre are you searching for?: ")

        for i in range(0, len(genre)):
            if search.lower() == genre[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry, your search for {search} was not found :[")
        
        else: 
            print(f"Your search for {search} has been found!")
            for i in range(0, len(found)):
                print(f"{libnum[found[i]]:7}  {title[found[i]]:32}  {author[found[i]]:25}  {genre[found[i]]:15} {pgcount[found[i]]:4} {status[found[i]]:9}")

    elif opt == "5":

# performing swap here
        for i in range(0, len(libnum) - 1):
            for j in range(0, len(libnum) -1): 
                if libnum[j] > libnum[j + 1]:
                    #they must swap places because the higher value must come afterwards
                    temp = libnum[j] # temporary variable
                    libnum[j] = libnum[j + 1]
                    libnum[j + 1] = temp

                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pgcount)
                    swap(j, status)

        min = 0
        max = len(libnum)
        mid = int((min + max) / 2)

        while min < max and search.lower() != libnum[mid].lower():
            if search.lower() < libnum[mid].lower():
                max = mid - 1
            else:
                #search > name[mid]
                min = mid + 1

            mid = int((min + max) / 2)

        if search.lower() == libnum[mid].lower():
            print(f"Your search for {search} has been found!")
            print(f"{libnum[mid]:7}  {title[mid]:32}  {author[mid]:25}  {genre[mid]:15} {pgcount[mid]:4} {status[mid]:9}")

        else:
            print(f"Your search for {search} was not found :[")


    elif opt == "6":

        found = []

        search = "Avaliable"
        for i in range(0, len(status))
            if search == status[i]:
                found.append(i)
            
        print(f"{libnum[found[i]]:7}  {title[found[i]]:32}  {author[found[i]]:25}  {genre[found[i]]:15} {pgcount[found[i]]:4} {status[found[i]]:9}")

    elif opt == "7":

        found = []

        search = "On Loan"
        for i in range(0, len(status))
            if search == status[i]:
                found.append(i)
            
        print(f"{libnum[found[i]]:7}  {title[found[i]]:32}  {author[found[i]]:25}  {genre[found[i]]:15} {pgcount[found[i]]:4} {status[found[i]]:9}")

    elif opt == "8":
        menu == "n"


print("Goodbye.")

        
            


