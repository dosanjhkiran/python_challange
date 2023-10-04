import os
import csv
#defining a fuction
def financial_analysis(filename):
    # Variables
    months = 0
    net_total = 0
    prev_value = None
    total_change = 0
    greatest_increase = float('-inf')
    greatest_decrease = float('inf')
    greatest_inc_month = ""
    greatest_dec_month = ""

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        
        for row in reader:
            months += 1
            net_total += int(row[1])
            
            if prev_value is not None:
                change = int(row[1]) - prev_value
                total_change += change
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_inc_month = row[0]
                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_dec_month = row[0]
            prev_value = int(row[1])
        
        avg_change = total_change / (months - 1)

    return (months, net_total, avg_change, greatest_inc_month, greatest_increase, greatest_dec_month, greatest_decrease)
#providing a file path
budget_csv = os.path.join("..", "resources", "budget_data.csv")
months, net_total, avg_change, greatest_inc_month, greatest_increase, greatest_dec_month, greatest_decrease = financial_analysis(budget_csv)
#save output in the text file
output_path = os.path.join("..", "resources", "analysis.txt")
#it will print the output in the text file
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------\n")
    txtfile.write(f"Total Months: {months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${avg_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_decrease})\n")

#printing the oiutput
print(f"Total Months: {months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_decrease})")
