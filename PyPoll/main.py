import csv as cv
from collections import Counter

# OUTLINING MY COMMENTS 
# ------------------------------------------------------------------------------
#Hello - This will be the main header - section of comments - HEADING comments 
# * Theses type of comments will be commented out to outline my thoughts - WALKTHROUGH comments
# ? Theses type of comments will be commented out to clarify complex code - CLARIFICATION comments
# ! This type of comments will be used to update/fix my code/improve it for next time - ACTION/IMPROVEMENT comments
# todo - These type of comments will be used to outline new trick/function process- FLOW/HOW? comments
    # todo --> Example: Creating a pivot table with pandas -- Include the following arguments: [index = , columns = , values = ,aggfunc = , margins = ]
# ------------------------------------------------------------------------------


dataset = []
with open("/Users/galbeeir/Desktop/Starter_Code/PyPoll/Resources/election_data.csv", "r") as file:
    
    # create a csv reader object
    data = cv.reader(file)
    
    # Append each row from data to dataset
    for row in data:
        print(row)
        dataset.append(row)

# DATASET HEAD
dataset[:5]

# Seperating each column within our dataset to a variable
id_col = []
country = []
candidate = []

for i in dataset: 
    id_col.append(i[0])
    country.append(i[1])
    candidate.append(i[2])


# REMOVING THE HEADERS FOR OUR COLUMNS
id_col = id_col[1:]
country = country[1:]
candidate = candidate[1:]

# RETRIEVE THE TOTLA AMOUNT OF VOTES
total_votes = len(id_col)

# CREATE A DICTIONARY USING COUNTER FUNCTION FROM COLLECTIONS
candidate_counts = Counter(candidate)

# Iterating through the candidate_count dictionary to retrieve the name, count, and votes percentage per candidate
votes_percentage = []
name = []
counts = []
for can, count in candidate_counts.items():
    print(round((candidate_counts[can]/len(candidate)) *100, 3))
    votes_percentage.append(round((candidate_counts[can]/len(candidate)) *100, 3))
    name.append(can)
    counts.append(count)

# DYNAMICALLY RETREVE THE MAX VALUE FROM THE COUNTS
# * We refer back to the max_count_index in our "result" variable to retrive dinamically the "name" that had most of the counts
max_counts = 0
max_counts_index = 0

# ? We use enumerate to iterate through both the index and the values of count, index (stored in max_count_index) and the max_counts, store the max value from the counts
for i, v in enumerate(counts):
    if v > max_counts:
        max_counts = v
        max_counts_index = i
max_counts

# SUMMURISING THE RESULTS OF OUR ANALYSIS AND WRITING THE RESULT TO TXT FORMAT
result = f"""
ELECTION RESULTS
----------------------------------------------------
Total Votes: {total_votes}
----------------------------------------------------
Candidates who received votes: {name}
----------------------------------------------------
{name[0]}: {votes_percentage[0]}% ({counts[0]})
{name[1]}: {votes_percentage[1]}% ({counts[1]})
{name[2]}: {votes_percentage[2]}% ({counts[2]})
----------------------------------------------------
Winnder: {name[max_counts_index]}
----------------------------------------------------
"""
print(result)
# Exporting the results to txt file format
with open("analysis_results2.txt", "w") as file:
    file.write(result)