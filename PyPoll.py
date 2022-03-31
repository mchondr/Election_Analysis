import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("/Users/mchondr/Desktop/Data Analysis/Election_Analysis/Resourses/election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # Print the file object.
     print(election_data)

# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/mchondr/Desktop/Data Analysis/Election_Analysis/analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)