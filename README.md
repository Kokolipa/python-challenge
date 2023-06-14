# Python Challenge
### Project description:
This project inlcludes python scripts to analyse two different datasets (PyBank & PyPoll) and provide a text file output containing the results. The first dataset,  budget_data.csv, contains financial records of a company in two columns: "Date" and "Profit/Losses". The python script analyses the dataset and provides the follwoing output:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

The second dataset, election_data.csv, contains three columns of poll data for a small rural U.S. town: "Voter ID", "County", and "Candidate". The python script analyses the data and provides the following output:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote


#### Folder structure
``` yml
.
├── PyBank
│   ├── analysis               # This folder contains the txt file (summary of the results)
│   │   ├── analysis_results.txt    
│   └── ..                  
|   ├── Resources              # This folder contains the csv file
│   |   ├── budget_data.csv                            
│   └── ..
|   ├── main.py                # This is the python script 
├── PyPoll
│   ├── analysis               # This folder contains the txt file (summary of the results)
│   │   ├── analysis_results2.txt   
│   └── ..                  
|   ├── Resources               # This folder contains the csv file
│   |   ├── election_data.csv                            
│   └── ..      
|   ├── main.py                 # This is the python script              
|              
|___README.md
``` 
