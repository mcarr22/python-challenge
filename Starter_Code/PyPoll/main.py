import os
import csv

#election csv path
ElectionCsv = os.path.join("c:/Users/makhi/OneDrive/Documents/github/python-challenge/Starter_Code/PyPoll/Resources/election_data.csv")
#output path
electionResults = os.path.join("c:/Users/makhi/OneDrive/Documents/github/python-challenge/Starter_Code/PyPoll/Resources/election_results.txt")

#variables
totalVotes = 0
print(os.getcwd())
print(ElectionCsv)
#create a dictionary of with key being candidates and how many votes they get
Candidates = {}
CandidateOptions = []
winningCount = 0
winner =""

with open(ElectionCsv) as csvfile:

    csvReader = csv.reader(csvfile, delimiter = ",")
    
    next(csvReader)

    for row in csvReader:

        candidateName = row[2]
        if candidateName not in CandidateOptions:
            CandidateOptions.append(candidateName)
            Candidates[candidateName] = 0

        Candidates[candidateName] +=1
    
        #count votes
        totalVotes+=1

with open(electionResults,'w') as txt:
    election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"-------------------------\n")
    txt.write(election_results)    

    for Candidate in Candidates:
    
        if winningCount < Candidates[Candidate]:
            winningCount = Candidates[Candidate]
            winner = Candidate

        votePercentage = Candidates[Candidate]/totalVotes*100
        print(str(round(votePercentage,2)) + "%")
        output = f"{Candidate} : {(round(votePercentage,3))}% ({Candidates[Candidate]})\n"
        txt.write(output)
        
    txt.write("The winner is: " + winner)
    
print(totalVotes)
print(CandidateOptions)
print(Candidates)
print(winningCount)
print(winner)
