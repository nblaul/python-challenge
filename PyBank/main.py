import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_months = []
    total = []
    change = []

    for row in csvreader:
        # list of all months
        total_months.append(row[0])
        # create list of profit/loss
        total.append(row[1])

    
    # sum profit/loss
    total = list(map(int, total))

    for i in range(len(total)-1):
        #create list with all changes
        monthly_change = change.append(total[i+1]-total[i])
        

average_change = sum(change)/len(change)
average_change = round(average_change, 2)
max_increase = max(change)
max_decrease = min(change)   

max_increase_month = change.index(max_increase) +1
max_increase_month = total_months[max_increase_month]

max_decrease_month = change.index(max_decrease) +1
max_decrease_month = total_months[max_decrease_month]

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

output_path = os.path.join("Analysis", "analysis.txt")

lines = ["Financial Analysis", "--------------------------", f"Total Months: {len(total_months)}",
f"Total: ${sum(total)}",f"Average Change: ${average_change}",
f"Greatest Increase in Profits: {max_increase_month} (${max_increase})", f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"]

with open(output_path, 'w') as txtfile:
    for line in lines:
        txtfile.write(line)
        txtfile.write('\n')