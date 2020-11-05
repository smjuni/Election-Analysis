#The data we need
#Total votes case
#complete listof candidates
#total # of votes/candidate
#% of votes each candidate received
#the winner by most votes

#import the datetime class from the datetime module
import datetime as dt
#use the now() attribute on the datetime class to get the present time
now=dt.datetime.now()
#print the present time
print("The time right now is", now)

import csv
import os

#assign a variable forthe file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file.
with open(file_to_load) as election_data:

#Read the file object with the reader function.
    file_reader = csv.reader(election_data)

#print the header row
headers = next(file_reader)
print(headers)
# #print each row in the csv file.
#     for row in file_reader:

#         print(row)

# #print the file object.
#     print(election_data)



#using the open() function with the w mode we will write data to the file
#open(file_to_save, "w")
#using the with statement ope the file as a text file.
with open(file_to_save, "w") as txt_file:
    #write some data to that file
    txt_file.write("Counties in the Election\n")
    txt_file.write("---------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# #close the file
# outfile.close()

