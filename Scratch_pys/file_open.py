# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

total_votes = 0
candidate_options = []
candidate_votes = {}
#csvpath = os.path.join('/Users/curtissmith/Data_Class/election_analysis/Resources/', 'election_results.csv')

with open('/Users/curtissmith/Data_Class/election_analysis/Resources/election_results.csv') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)