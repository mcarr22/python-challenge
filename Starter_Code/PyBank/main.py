import os
import csv
#bank csv path
bankCsv = os.path.join("c:/Users/makhi/OneDrive/Documents/github/python-challenge/Starter_Code/PyBank/Resources/budget_data.csv")
#output path
bankAnalysis = os.path.join("c:/Users/makhi/OneDrive/Documents/github/python-challenge/Starter_Code/PyBank/Resources/budgetAnalysis.csv")
#variables
totalMonths = 0
totalProfits = 0
greatestIncrease = 0
greatestDecrease = 0
prevProfit = None
#list of profits for average
monthlyChange = []
monthlyChanges = []
#dictionary of date and profit
date = {}
profit = []



#read

with open(bankCsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    next(csvreader)

    for row in csvreader:
        month = row[0]
        monthProfit = int(row[1])
        
        if prevProfit is not None:
            monthlyChange = monthProfit - prevProfit
            monthlyChanges.append(monthlyChange)
        prevProfit = monthProfit
        # print (f"Month: {month}")
        # print("month profit: $" + row[1])
        
        
        
        #count total months
        totalMonths+=1
        totalProfits +=int(monthProfit)
        
        #calculate the average change
totalChange = sum(monthlyChanges)
averageChange = totalChange / (totalMonths-1)
#find the greatest increase
greatestIncrease = max(monthlyChanges)
greatestIncreaseMonth = monthlyChanges.index(greatestIncrease) + 1  
#find the greatest decrease
greatestDecrease = min(monthlyChanges)
greatestDecreaseMonth = monthlyChanges.index(greatestDecrease) + 1

print(f"total months: {totalMonths}")
print(f"total profits: ${totalProfits}")
print(f"average change: ${averageChange:.2f}")
print(f"Greatest increase: ${greatestIncrease:.2f}  {greatestIncreaseMonth}")
print(f"Greatest decrease: ${greatestDecrease:.2f} {greatestDecreaseMonth}")

with open(bankAnalysis,'w') as txt:
    election_results = (
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"total months: {totalMonths}\n"
    f"total profits: ${totalProfits}\n"
    f"average change: ${averageChange:.2f}\n"
    f"Greatest increase: ${greatestIncrease:.2f}  {greatestIncreaseMonth}\n"
    f"Greatest decrease: ${greatestDecrease:.2f} {greatestDecreaseMonth}"
    )
    txt.write(election_results)   