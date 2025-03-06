#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)       #entire list
print(names_list[0])    #first value  
print(names_list[len(names_list) - 1])       #last value

#creation & population of dictionaries
people_dictionary ={
    #"key" : value
}
#create an empty list for each potential field
#these MUST remain the same length in order to parallel
names = []
riders = []
nums = []
color1 = []
color2 = []

#gaining data from a text file 
with open("week 9/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #adding data to a list 
        names.append(rec[0])
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
        else:
            color2.append("N/A")


        #adding data to a dictionary



#processing data from collections
# lists --> standard for i in range():
print(f"{'NAMES':12} {'RIDERS':30} {'NUM':3} {'COLOR 1':8} {'COLOR 2'}")
for i in range(0, len(names)): 
    
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")
print("-" * 75)

#searching & sorting
#BINARY SEARCH --> requires a set of ordered and unique data, no duplicates!!
#in this case, only the name list can be name searched
#ALWAYS SORT YOUR DATA FIRST!

for i in range(0, len(names) - 1):
    for j in range(0, len(names) - 1):
        if names[j] > names[j + 1]:
            #swap places
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)

# binary --> bi means 2 --> we create a high and low half of the list
search = input("Please enter the dragon name you are searching for: ")
min = 0
max = len(names) - 1
mid = int((min + max) / 2)

while min < max and search.lower() != names[mid].lower():
    if search.lower() < names[mid].lower():
        max = mid - 1
    else: 
        min = mid + 1
    mid = int((min + max) / 2)

if search.lower() == names[mid].lower():
    print(f"We found your search for {search} in record {mid}, details below: ")
    print(f"{names[mid]:12} {riders[mid]:30} {nums[mid]:3} {color1[mid]:8} {color2[mid]}")

else:
    print(f"Sorry, we did not find your search for {search} :[")


#2D lists - lists of lists!