#W8D2 dictionary review and gaining data from text files

import csv

library = {
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}

with open("week 8/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in the file, do the following
        #file ---> 2d list, rec ---> 1 records data
        library.update({rec[0] : rec[1]})
        #library_num = rec[0]
        #title = rec[1]

# disconnected from file ---------------------------

for key in library:
    #for every key found in the library dictionary
    print(f"{key:4} : {library[key]}")
print("-" * 50)

# --- SEQUENTIAL SEARCH WITH DICTIONARIES --------------------

search = input("enter the TITLE you are searching for: ")

#all unique book titles, no need for found list
found = [] 

for key in library:
    if search.lower() in library[key].lower():
        found.append(key)
    
if found != 0:
    print(f"we found your search for {search}, details below: ")
    print("-" * 50)
    for i in range(0, len(found)):
        print(f"{found[i].upper():4} {library[found[i]]}")
    print("-" * 50)
else: 
    print(f"We could not find your search for {search}.")
