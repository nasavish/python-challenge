# Import libaries
import pandas as pd

# Print what I'm doing
print('Election Results')
print('--------------------')

# Read data
data = 'election_data_1.csv'
data_df = pd.read_csv(data)

data_df.head()

# Print total votes
total_votes = data_df['Voter ID'].count()

print('Total Votes: ' + str(total_votes))
print('--------------------')

# Votes/ candidate
candidates = data_df.groupby('Candidate')
candidates

candidate_votes = candidates['Voter ID'].count()
candidate_votes

# Percent votes/ candidate
percent_votes = round((candidate_votes/ total_votes)*100,1)
percent_votes

# New results data frame
results_df = pd.concat([candidate_votes, percent_votes], axis=1)
results_df.columns = ['Votes', 'Percent']
print(results_df[['Percent', 'Votes']])

# Print winner
print('--------------------')
winner = results_df['Percent'].sort_values(ascending=False)
print('Winner: {}'.format(winner.index[0]))
print('--------------------')

# Export results into .txt
# 'main.py' > 'main.txt'
f= open("main.txt","w")
f.write('Election Results\n')
f.write('--------------------\n')
f.write('Total Votes: ' + str(total_votes))
f.write('\n--------------------\n')
f.write('     '+str(results_df[['Percent', 'Votes']]))
f.write('\n--------------------')
f.write('\nWinner: {}'.format(winner.index[0]))
f.write('\n--------------------') 
f.close() 


