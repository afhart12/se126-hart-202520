#Alexandra Hart
# Lab 5
# SE126.04
# February 14, 2025

# Prompt:

# library menu:
# 1 - all data, print statement
# 2 - title keyword, sequential search
# 3 - author, sequential
# 4 - genre, sequential
# 5 - one specific library number item, binary search
# 6 - sequential, status of avaliable
# 7 - status of on loan, sequential
# 8 - exit the loop

# variable dictionary

libnum = []
title = []
author = []
genre = []
pgcount = []
status = []

menu = "y" # this is to start the main while loop
# functions -----
def display(x, records):
    print(f"{'NUMBER':7}  {'TITLE':32}  {'AUTHOR':25}  {'GENRE':15} {'PG COUNT':4} {'STATUS':9}")
    print("----------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{libnum[x]:7}  {title[x]:32}  {author[x]:25}  {genre[x]:15} {pgcount[x]:4} {status[x]:9}")

    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{libnum[x]:7}  {title[x]:32}  {author[x]:25}  {genre[x]:15} {pgcount[x]:4} {status[x]:9}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{libnum[x]:7}  {title[x]:32}  {author[x]:25}  {genre[x]:15} {pgcount[x]:4} {status[x]:9}")

    print("----------------------------------------------------------------\n")

#-------
import csv

with open("week 6/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        libnum.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        

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
    if opt == "1":
        display("x", len(libnum) - 1)
