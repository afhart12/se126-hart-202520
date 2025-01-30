# W4D2 Sequential Search Review and Creating and writing to text files

# program prompt: in the w4d2 demo, we will review utilizing sequential search for simple singular and multi returns. we will then create and write data to a text file using Python.

# --- IMPORTS ---------------------------------------
import csv

# --- FUNCTIONS -------------------------------------

# --- MAIN EXECUTING CODE ---------------------------

# create an empty list for every potential field in the file
dragons = [] # field0 - dragon names
riders = []  # field1 - rider names
counts = []  # field2 - 1 or 2, count of colors
color1 = []  # field3 - first primary color
color2 = []  # field4 - second color,  only if color is 2

with open("week4/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        dragons.append(record[0])
        riders.append(record[1])
        counts.append(int(record[2]))
        color1.append(record[3])
        if record[2] == 2:
            color2.append(record[4])
        elif record[2] == 1: 
            color2.append("---")
        
# disconnected from file, no more working with records!! working with lists now

# process lists to display data to the console

print(f"{'DRAGONS':15} {'RIDERS':30} {'#':3} {'COLOR1':8} {'COLOR2':8}")

for index in range(0, len(dragons)):
    print(f"{dragons[index]:15} {riders[index]:30} {counts[index]:3} {color1[index]:8} {color2[index]:8}")
print("----------------------------------------------------")

# SEARCH for a specific dragon

#step 1 - setup and gain of search

found = "x"
search = input("Which dragon are you looking for: ")

# step 2 - perform search: for loop with if statement

for index in range(0, len(dragons)):
    if search.lower() in dragons[index].lower():
        #hold onto found location(index) of our searched-for value
        found = index

# step 3 - filter and display results
if found != "x":
    print(f"Your search for {search} has been FOUND: ")
    print(f"{dragons[found]:15} {riders[found]:30} {counts[found]:3} {color1[found]:8} {color2[found]:8}")
else: 
    print(f"Your search for {search} was NOT FOUND :(")

# search for a color set

found = []
search = input("Enter the color you are looking for: ")

for index in range(0, len(color1)):
    if search.lower() in color1[index] or search.lower() in color2[index]:
        found.append(index)

# check if found is empty
if not found: 
    print("Your search for {search} was NOT FOUND :(")
else: 
    for index in range(0, len(found)):
        print(f"{dragons[found[index]]:15} {riders[found[index]]:30} {counts[found[index]]:3} {color1[found[index]]:8} {color2[found[index]]:8}")


# WRITE some data to a file and creating said file
# create and write dragons and riders of the data to a new text file

file = open("targs.csv", "w")

for index in range(0, len(dragons)):
    file.write(f"{dragons[index]},{riders[index]}\n")
file.close()
