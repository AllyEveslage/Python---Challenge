import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("Resources", "budget_data.csv")

#Create our variables
months = 0
total_profit_loose = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    # Reading the header/different variables within the datat set
    first_row = next(csvreader)
    months += 1
    total_profit_loose += int(first_row[1])
    value = int(first_row[1])
    
    # This allows us to ignore the header and run through the information
    for row in csvreader:
        dates.append(row[0])
        
        # Calculating the change
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months +1 so it continues to move to the next month
        months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_profit_loose = total_profit_loose + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average within "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Printing all the information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(months)}")
print(f"Total: ${str(total_profit_loose)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Showing the code where to write the results of this code
output = open("output.csv", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(months)}")
line4 = str(f"Total: ${str(total_profit_loose)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))