# W2D1 - Text File Handling Demo

# Step 1: import the csv library
import csv

totalRecords = 0 # holds total # of records in the file
# step 2: connect to file

# connected to file ------------------------------------

# include relative file path in open() - flip backslash to forward slash or line will generate an error
with open("week 2/simple.csv") as csvfile:
    # make sure to indent inside of code block

    # allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2d list / matrix / table]
    file = csv.reader(csvfile)
    # print for headers
    print("{'NAME':10} {'NUM':3} {'COLOR'}")
    
    # Step 3: process through every record or row in the file
    for record in file:
        # add +1 to totalRecords to keep accurate count of recs
        totalRecords += 1

        name = record[0]
        number = record[1]
        color = record [2]


# disconnected from file -------------------------------

print(f"\nTotal Records: {totalRecords}\n")
