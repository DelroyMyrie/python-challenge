import csv
from collections import OrderedDict
from operator import itemgetter

# Mapping the CSV File
csvpath.join("Resources", "election_data.csv")

# Reading the CSV File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
print(csvreader)

# Variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

# Looping through data
for row in csvreader:

# Calculate Totals
    votes = votes + 1
    total_candidates = row["Candidate"]        

# Determine Candidate's with votes
    if row["Candidate"] not in candidate_options:
        candidate_options.append(row["Candidate"])
        candidate_votes[row["Candidate"]] = 1

    else:
        candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

# Determine the Winner
    if (votes > winner_votes):
        greatest_votes = votes + 1
        candidate_options = row["Candidate"]

print()
print()
print("Election Results")
print("-------------------------")
print("Total Votes " + str(votes))
print("-------------------------")

# Winner
for candidate in candidate_votes:
    print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes
winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("-------------------------")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("-------------------------")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("Total Votes " + str(votes))