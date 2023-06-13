import csv as cv

# OUTLINING MY COMMENTS
# --------------------------------------------------------------------------------------------------------------------------------
#Hello - This will be the main header - section of comments - HEADING comments 
# * Theses type of comments will be commented out to outline my thoughts - WALKTHROUGH comments
# ? Theses type of comments will be commented out to clarify complex code - CLARIFICATION comments
# ! This type of comments will be used to update/fix my code/improve it for next time - ACTION/IMPROVEMENT comments
# todo - These type of comments will be used to outline new trick/function process- FLOW/HOW? comments
    # todo --> Example: Creating a pivot table with pandas -- Include the following arguments: [index = , columns = , values = ,aggfunc = , margins = ]
# --------------------------------------------------------------------------------------------------------------------------------

# Storing our dataset in the dataset variable
# *------------------------------------------------------------------------------------------------------------------------
dataset = []
with open("/Users/galbeeir/Desktop/git/python-challenge/PyBank/Resources/budget_data.csv", "r") as file:
    # create a csv reader object
    data = cv.reader(file)

    # * iterate through each row within the csv file 
    for row in data:
        print(row)
        dataset.append(row)

# SEPERATE OUR TWO COLUMNS
dates = []
profit_losses = []
for i in dataset: 
    dates.append(i[0])
    profit_losses.append(i[1])

# Excludin the first row within the date column
dates = dates[1:]
dates[:5]

# Excludin the first row within the profit_losses column
profit_losses = profit_losses[1:]

# Transforming the dtype of the profit losses column
# *------------------------------------------------------------------------------------------------------------------------
pl_column = []
for i in profit_losses:
    pl_column.append(int(i))

pl_column[:10]


# total # of months in our PyBank dataset
total_months = len(dates)

total = sum(pl_column)

# CALCULATING THE CHANGE OVER TIME
# *------------------------------------------------------------------------------------------------------------------------
previous_value = pl_column[0]
total_change = 0 

# * Excluding the first avlue form pl_column
for value in pl_column[1:]:
    change = value - previous_value
    total_change += change
    previous_value = value

# CALCULATING THE AVERAGE CHANGE BASED ON THE TOTAL CHANGE
# *------------------------------------------------------------------------------------------------------------------------
# * The change relative to the our pl_column is always n-1, we have to disclude one number
average_change = round(total_change / (len(pl_column)-1), 2) 
average_change


# Calculating the greatest increase in profits (date and amount) over the entire period
# *------------------------------------------------------------------------------------------------------------------------
max_increase = 0 
max_increase_index = 0

for i in range(1, len(pl_column)):
    
    # * substracting the following value from the previous one
    increase = pl_column[i] - pl_column[i-1] 
    if increase > max_increase:
        # ? In each iteration of the for loop, we are saving the most up to date "max_increase"
        max_increase = increase 

        # * To extract the most relevent of max_increase we use the following
        max_increase_index = i 
print(f"Greatest Increase in profits: {dates[max_increase_index]}, ${max_increase}")


# Calculating the greatest decrease in profits (date and amount) over the entire period
# *------------------------------------------------------------------------------------------------------------------------

# * We will use the same method to calculate this
min_decrease = 0 
min_decrease_index = 0 

for i in range(1, len(pl_column)):
    decrease = pl_column[i] - pl_column[i-1]
    # ? This time we want to check the greatest decrease, so we have to use the less then operator to retrive the smallest amount
    if decrease < min_decrease:
        min_decrease = decrease
        min_decrease_index = i
print(f"Greatest Decrease in profits: {dates[min_decrease_index]}, {dates[min_decrease_index]}, ${min_decrease}")

# PRITING ANALAYSIS RESULTS
results = f"""
Final Analysis
----------------------------------------------------------------
Total Months: {total_months}
Total: ${total}
Average Change: ${average_change}
Greatest Increase in Profits:{dates[max_increase_index]}, ${max_increase}
Greatest Decrease in Profits:{dates[min_decrease_index]}, ${min_decrease}
 """

# Pussing the results to terminal
print(results)

# Exporting the results to txt file format
with open("analysis_results.txt", "w") as file:
    file.write(results)