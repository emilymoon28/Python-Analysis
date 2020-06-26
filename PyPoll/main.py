import os
import csv

csvpath=os.path.join("Resources","election_data.csv")

#extract all the votes and put them into a list
votes=[]
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        votes.append(row[2])

# the total number of votes cast of the whole doc
total_votes=len(votes)
print("Election Result")
print("------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------------------------------")

#get the unique name of the candidates
unique=[]
def get_names(list):
    for i in list:
        if i not in unique:
            unique.append(i)
#call the function to add the unique names into the list
get_names(votes)
#print(unique)

#use function to 'sum up' the votes of each candidate
def count_votes(list,name):
    count=0
    for item in list:
        if name==item:
            count+=1
    return count

#count the votes of each candidate
summary={}
for x in unique:
    summary[x]=count_votes(votes,x)

#print(summary)

max_vote=0
for key,value in summary.items():
    print(f'{key}: {round((value/total_votes)*100,4)}% ({value})')
    if value>max_vote:
        max_vote=value
print("------------------------------------------------------")

#store the largest number of votes
max_votes=max(summary.values())

#use a simple function to get the key based on value
def find_key(val):
    for key,value in summary.items():
        if val==value:
            return key

print("Winner: " + find_key(max_votes))
print("------------------------------------------------------")

output_path=os.path.join("Analysis","output.txt")

with open(output_path,'w') as output_file:
    output_file.write("Election Result\n")
    output_file.write("------------------------------------------------------\n")
    output_file.write(f'Total Votes: {total_votes}\n')
    output_file.write("------------------------------------------------------\n")
    max_vote=0
    for key,value in summary.items():
        output_file.write(f'{key}: {round((value/total_votes)*100,4)}% ({value})\n')
        if value>max_vote:
            max_vote=value
    output_file.write("------------------------------------------------------\n")
    output_file.write("Winner: " + find_key(max_votes)+"\n")
    output_file.write("------------------------------------------------------\n")


