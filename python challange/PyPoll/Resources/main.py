import os
import csv

def election_results(filename, output_file):
    # Dictionary to store vote counts per candidate
    candidate_votes = {}
    total_votes = 0

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header

        for row in reader:
            candidate_name = row[2]  # Assuming candidate's name is in the third column
            candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1
            total_votes += 1

    with open(output_file, 'w') as f:
        # Write results to file
        f.write(f"Total votes: {total_votes}\n")
        f.write("-" * 30 + "\n")
        
        max_votes = 0
        winner = ""

        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100
            f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
            
            if votes > max_votes:
                max_votes = votes
                winner = candidate

        f.write("-" * 30 + "\n")
        f.write(f"Winner: {winner}\n")
        f.write("-" * 30 + "\n")

# Test the function
election_csv = os.path.join("..", "resources", "election_data.csv")
output_txt = os.path.join("..", "resources", "analysis.txt")
election_results(election_csv, output_txt)

   