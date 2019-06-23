import os
import csv

# Mapping the CSV File
csvpath.join("Resources", "budget_data.csv")

# Reading the CSV File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
print(csvreader)

# Variables
total_months = 0
total_profit/loss = 0
prev_profit/loss = 0
profit/loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]  
profit/loss_changes = []
  
# Looping through data
for row in csvreader:

# Calculate totals      
    total_months = total_months + 1
    total_profit/loss = total_profit/loss + int(row["profit/loss"])
    print(row)

# Keep track of changes
profit/loss_change = int(row["profit/loss"]) - prev_profit/loss
print(profit/loss_change)

# Reset the value of prev_profit/loss 
prev_profit/loss = int(row["profit/loss"])
print(prev_profit/loss)

 # Determine the greatest increase
if (profit/loss_change > greatest_increase[1]):
    greatest_increase[1] = profit/loss_change       
    greatest_increase[0] = row["Date"]

if (profit/loss_change < greatest_decrease[1]):
    greatest_decrease[1] = profit/loss_change
    greatest_decrease[0] = row["Date"]

 # Add to the profit/loss_changes list
profit/loss_changes.append(int(row["profit/loss"]))

# Set the profit/loss average
profit/loss_avg = sum(profit/loss_changes) / len(profit/loss_changes)

# Show Output
print()
print()
print()
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(total_months))
print("Total Profit/loss: " + "$" + str(total_profit/loss))
print("Average Change: " + "$" + str(round(profit/loss_changes) / (profit/loss_changes),2))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    
    
# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("Total profit/loss: " + "$" + str(total_profit/loss))
    txt_file.write("Average Change: " + "$" + str(round(profit/loss_changes) / (profit/loss_changes),2))
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")