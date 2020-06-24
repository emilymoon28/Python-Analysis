import os
import csv

csvpath=os.path.join("Resources","budget_data.csv")
output_path=os.path.join("Analysis","output_bank.txt")

date=[]
profit_losses=[]


#read the csv and actions
with open(csvpath) as datafile:
    csvreader=csv.reader(datafile,delimiter=",")
    #skip headers
    next(csvreader,None)
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
        
#print out results
print("Financial Analysis")
print("--------------------------------------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(profit_losses)}')
print(f'Average Change: ${sum(profit_losses)/len(profit_losses)}')

#use the index of max increase/decrease profit/losses to find the corresponding dates in the date list
max_increase_index=profit_losses.index(max(profit_losses))
max_decrease_index=profit_losses.index(min(profit_losses))

print(f'Greatest Increase in Profits: {date[max_increase_index]} (${max(profit_losses)})')
print(f'Greatest Decrease in Profits: {date[max_decrease_index]} (${min(profit_losses)})')

        

#out put the result in a text file
with open(output_path,'w') as outputfile:
    outputfile.write("Financial Analysis \n-------------------------------------------------------- \n")
    outputfile.write(f'Total Months: {len(date)} \nTotal: ${sum(profit_losses)} \nAverage Change: ${sum(profit_losses)/len(profit_losses)} \n')
    outputfile.write(f'Greatest Increase in Profits: {date[max_increase_index]} (${max(profit_losses)})\nGreatest Decrease in Profits: {date[max_decrease_index]} (${min(profit_losses)}) \n')