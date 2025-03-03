# Alexandra Hart
# SE126.04
# Lab 7
# 2/25/2025

#Program Prompt: Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu: 1 = show all words, 2 = search for a word, 3 = add a word, 4 = exit

# variable dictionary:
#dictionary = my created dictionary that holds all of the words from the csv file and their definitions
# menu = a value to determine if the while loop keeps running
# opt = menu option that the user selects, either 1 2 3 or 4
# found = a list to hold the values found by my sequential search loop that relate to the users search
# search = a value holding the users search entry
# newWord = a value holding the users entry for a new word
# newdef = a value holding the users entry for a new definition relating to the word they put in
# flag = a variable that changes based on if the new word is the same as a word that already exists in the dictionary

dictionary = {

}
menu = "y"
import csv

with open("week 8/words.csv") as csvfile: # file open
    file = csv.reader(csvfile)
    for rec in file:
        dictionary.update({rec[0] : rec[1]})

while menu == "y": #this loop keeps the menu running until the user selects option 4
    print("My Programming Dictionary Menu: ")
    print("1. Show all words(including definitions)")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. EXIT")
    opt = input("Your selection(1/2/3/4): ")
    if opt == "1": #print all words from the dictionary
        print(f"{'WORD':15} {'DEFINITION':158}")
        for key in dictionary:
            print(f"{key:15} {dictionary[key]:158}")

    elif opt == "2":
        found = [] # value for keys in the dictionary that match the search query
        search = input("What are you searching for?: ")

        for key in dictionary:
            if search.lower() in key.lower():
                found.append(key)
            print(found)
        
        if not found: # no matching results, found list is empty
            print(f"We could not find your search for {search}.")
        else: # found list has one or more values
            print(f"We found your search for {search}, details below: ")
            print("-" * 50)
            for i in range(0, len(found)):
                print(f"{found[i]:4} {dictionary[found[i]]}")
            print("-" * 50)

    elif opt == "3":
        newWord = input("What word would you like to add?: ")
        newDef = input("What is this word's definition?: ")

        flag = "green"

        for key in dictionary:
            if newWord == key: #checks if the new word is the same as an existing key in the dictionary
                flag = "red"

        if flag != "red": #if the flag value does not become red, the program is clear to add the word to the dictionary
            dictionary.update({newWord : newDef}) 
        else: #the program cannot add the word because it already exists
            print(f"Sorry, this dictonary already contains the word {newWord}.")

    elif opt == "4":
        print("Goodbye.")
        menu = "n" #ends the loop

    else: 
        print("INVALID ENTRY!! Please try again.")

