import os
import csv

#Finding our csv file so we can find the data we want from it.
election_data = os.path.join("Resources", "election_data.csv")

# A list to capture the names of candidates running, the number each condidate got, 
# the perccentage of votes and setting the quantity of votes to 0
candidates = []
num_of_votes = []
percent_of_votes = []
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # As we loop through, we will add 1 vote towards the total votes
        total_votes += 1 

        # Will add new names in their respective rows as they are found within the Candidate Column
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_of_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_of_votes[index] += 1
    
    # To get a percentage, we need to calculate the total votes, multiply by 100, then configure the percentage
    # "%.3%%" = formatting the number we get from our previous calculation to show as a percentage
    # append to add this percentage to the right of the candidates
    for votes in num_of_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_of_votes.append(percentage)
    
    # Find the winning candidate through the max function
    winner = max(num_of_votes)
    index = num_of_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(num_of_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(num_of_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))