#W8D1 - Introduction to Dictionaries

#start by creating populated dictionary
myCar = {
    #'key' : 'value'
    "make" : "Ford",
    "model" : "Focus SE Hatchback",
    "year" : 2014,
    "name" : "Gwendoline",
    "color" : "black",
    "friends" : ["Tyler","Tony","Steve"]
    # key names CANNOT be repeated / no duplicates of keys!!!
}

#view the entire dictionary and its data
print(myCar)

#view a specific value from the dictionary --> name[key] --> value
print(f"My car is a {myCar["make"]} {myCar["model"]}. It is {myCar["color"]}.")

#add some data to a dictionary once created
myCar["plate"] = "12345"

#or use the .update() method
myCar.update({"wheels" : "4"})


yourCar = {
    #'key' : 'value'
    "make" : "Ford",
    "model" : "F-150",
    "year" : 2024,
    "name" : "Gandalf",
    "color" : "black"
}

for key in yourCar:
    #for every key stored to the yourCar dictionary
    print(f"{key.upper():10} {yourCar[key]}")