# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os
# Assign a variable for the file to load the path
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# Declare candidate options list and candidate votes dictionary
candidate_options = []
candidate_votes = {}
# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the csv file
    for row in file_reader:
        #  Add to the toal vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If candidate does not match existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote
            candidate_votes[candidate_name] = 0
        # Add vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results in txt file
with open(file_to_save,"w") as txt_file:
# Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    # Retrieve votes for each candidate and get % of votes
    # Use a for loop to iterate through candidate options list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the vote percentage 
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")        
        # Print out each candidate's name, vote count and percentage of votes to terminal
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)
        # Determine the percentage of votes for each candidate by looping through the counts
        # Iterate through the candidate list
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning candidate = candidate's name
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate"s results to the text file
    txt_file.write(winning_candidate_summary)

