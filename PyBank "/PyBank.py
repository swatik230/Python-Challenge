import os
import csv  # Module for reading CSV files

# Open the path with csv library
csvpath = os.path.join('D:/MSU DATA/Module3_Challenge/Starter_Code/Starter_Code/PyBank/Resources', 'budget_data.csv')

count = 0
net_total = 0
increase = 0
decrease = 0
initial = 1
final_val = 0

# Read the file, row by row
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        net_total = net_total + int(row[1])
        count += 1
        initial_val = int(row[1])

       # Checks the max increase and the min decrease.

        if (increase > (final_val - initial_val)):
            increase = final_val - initial_val
            mincrease = row[0]
        if (decrease < (final_val - initial_val)):
            decrease = final_val - initial_val
            mdecrease = row[0]
        final_val = initial_val

        if initial == 1:
            valorinitial = int(row[1])
            initial = 0
        if count == 86:
            valorfinal = int(row[1])

    average = (valorfinal - valorinitial) / (count - 1)

    file1 = open('D:/MSU DATA/Module3_Challenge/Starter_Code/Starter_Code/PyBank/Resources/budget_data.csv', 'w+')
    file1.write("\t \t Financial Analysis\n")
    file1.write("---------------------------------------------------")
    file1.write("\nTotal of number of months analyzed: %s" % (count))
    file1.write("\nNet total amount: %1.1f" % (net_total))
    file1.write("\nAverage: %1.2f" % (average))
    file1.write("\nGreatest increase in profits: %1.1f, from the month of %s" % (-increase, mincrease))
    file1.write("\nGreatest decrease in losses: %1.1f, from the month of %s\n" % (-decrease, mdecrease))
    file1.write("---------------------------------------------------")
    file1.close() 

    print("\t \t Financial Analysis")
    print("-------------------------------------------------")
    print("Total of number of months analyzed: %s" % (count))
    print("Net total amount: %1.1f" % (net_total))
    print("Average: %1.2f" % (average))
    print("Greatest increase in profits: %1.1f, from the month of %s" % (increase, mincrease))
    print("Greatest decrease in losses: %1.1f, from the month of %s" % (decrease, mdecrease))
    print("--------------------------------------------------")
