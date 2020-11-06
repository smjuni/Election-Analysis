#The data we need:
#Total votes case
#complete listof candidates
#total # of votes/candidate
#% of votes each candidate received
#the winner by most votes

# #import the datetime class from the datetime module
# import datetime as dt
# #use the now() attribute on the datetime class to get the present time
# now=dt.datetime.now()
# #print the present time
# print("The time right now is", now)

#add our dependencies
import csv
import os

#assign a variable forthe file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#add accumulater variable
total_votes=0

#candidate options
candidate_options = []

#create a dicionary
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage= 0

#open the election results and read the file.
with open(file_to_load) as election_data:

#Read the file object with the reader function.
    file_reader = csv.reader(election_data)

#print the header row
    headers = next(file_reader)
    # print(headers)
#print each row in the csv file.
    for row in file_reader:
        #add to the total count
        total_votes += 1

        #print the candidate's name from each row
        candidate_name = row[2]

        #add the candidates name to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #start counting the votes for that candidate
            candidate_votes[candidate_name] =0
            #add a vote to the votes for that candidate
        candidate_votes[candidate_name]+=1

#create a for loop to go thorugh candidate options list
for candidate_name in candidate_votes:
    
#use the for loop to retreive candidate votes from the candidate_votes dict
    votes = candidate_votes[candidate_name]
#calculate the percentage of candidate votes
    vote_percentage = float(votes)/float(total_votes) *100
#print each candidate and their percentage using an f string
    print(f"{candidate_name} received {vote_percentage:.1f}% ({votes}).\n")
#To do: print each candidates nuame , vote count, and percentage of voes to the terminal
# print(candidate_votes)
      
#print the total votes.
# print(total_votes)
# #print the file object.
#     print(election_data)

#Determine winning vote count and candidate
#determine if otes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage> winning_percentage):
    #if true set winning_count to votes and winning_percent to vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
    #set the winning candidate equal to candidates name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"----------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"----------------------------------------\n")
print(winning_candidate_summary)
# #using the open() function with the w mode we will write data to the file
# #open(file_to_save, "w")
# #using the with statement ope the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     #write some data to that file
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("---------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# # #close the file
# # outfile.close()

