# Election-Analysis #
# Part 1 - Module 3 - Python #

## Project Overview ##
Following a local congressional election an Elections employee, Tom has asked that we analyze the elections data to find out the following:
  
  1. Calculate the total number of votes cast.
  2. Compile a list of Candidates who received votes.
  3. Calculate the total number of votes each Candidate received.
  4. Calculate the percentage of votes each Candidate won.
  5. Determine the winner of the election based on popular vote.

## Resources ##
Data Source: election_results.csv
Software: Python 3.7.6, Visual Studio Code, 1.50.1

## Summary ##
The analysis of the election shows that:
  - There were 369,711 votes cast
  - The Candidates were:
    - Charles Casper Stockham
    - Diana Degette
    - Raymon Anthony Doane
   - The Candidate results were:  
    - Charles Casper Stockham received 23.0% (85213).
    - Diana DeGette received 73.8% (272892).
    - Raymon Anthony Doane received 3.1% (11606).
  - The winner of the election was Diana DeGette with 73.8% and 272892 votes.


# Part 2 - Challenge #
## Overview of the Election Audit ##

The purpose of this audit was to help our Colorado Elections Officer, Tom to supply the election commission with some further details to the election analysis above. The additional data requested is:
  - The voter turnout for each county.
  - The percentage of votes each county received out of the total votes.
  - The county that had the highest voter turnout.

## Election Audit Results ##
The audit of the election (referenced in election_analysis.txt) shows that:
  - The total votes cast: 369,711
  - The votes by county:
    - Jefferson: 38,855
    - Denver: 306,055
    - Arapahoe: 24,801
  - The percentage of votes each county received out of the total votes cast:
    - Jefferson: 10.5% 
    - Denver: 82.8%
    - Arapahoe: 6.7% 
  - The County with the highest voter turnout was Denver with 306,055 voters and 82.8% of the turnout.
  - The Candidates were:
    - Charles Casper Stockham
    - Diana Degette
    - Raymon Anthony Doane
  - The Candidate results were:  
    - Charles Casper Stockham received 23.0% (85213).
    - Diana DeGette received 73.8% (272892).
    - Raymon Anthony Doane received 3.1% (11606).
  - The winner of the election was Diana DeGette with 73.8% and 272892 votes.

## Election Audit Summary ##
This script could be easily modified to perform analysis of any election. The script is versatile if the data is provided in a similar format and the outcomes of the election are following the same formulas.

In order to utilize this script for a different data set, you would need to ensure that the os.path.join command is linked to the correct resource and then that the 
below code references the correct input for candidate name and county(or other area) name.

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row [1]
You will also need to review the script to ensure that the output matches and is relevant to the text.

If there are more categories or factors to the election that need to be considered (For example: if different counties have different mathematical weight to their votes), then the script would need to be modified to add in a calculation to ensure that the end votes were tallied correctly.
