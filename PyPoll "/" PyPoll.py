
import os
import csv

#Set the path for the CSV file in PyPollcsv

PyPollcsv = os.path.join("D:/MSU DATA/Module3_Challenge/Starter_Code/Starter_Code/PyPoll/Resources", "election_data.csv")

# Create the lists to store data. Initialize 

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y / count) * 100
        vote_percent.append(z)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

# Print to terminal

print("Election Results")
print("-------------------------")
print("Total Votes :" + str(count))
print("-------------------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(round(vote_percent[i],3) )+ "% (" + str(vote_count[i]) + ")")
print("-------------------------")
print("Winner :" + winner)
print("-------------------------")

# Print to a text file: election_results.txt


with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(round(vote_percent[i],3)) + "% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("---------------------------------------\n")
