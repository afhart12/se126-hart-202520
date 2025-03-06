#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------



#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)       #entire list
print(names_list[0])    #first value  
print(names_list)       #last value

#creation & population of dictionaries
people_dictionary ={
    #"key" : value
}


#gaining data from a text file 
with open("week 9/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list 


        #adding data to a dictionary



#processing data from collections



#searching & sorting




#2D lists - lists of lists! 