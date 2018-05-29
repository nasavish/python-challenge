# Import libraries
import pandas as pd

# Print what I'm doing
print('Financial Analysis')
print('----------------------------')

# Read data
data = 'budget_data_1.csv'
data_df = pd.read_csv(data)

# Calculate total revenue
total_revenue = data_df['Revenue'].sum()

print('Total Revenue: ' + '$' + str(total_revenue))

# Calculate total months
total_months = data_df['Date'].count()

print('Total Months: ' + str(total_months)) 

# Create new column of monthly revenue delta
rev_difference = data_df['Revenue'].diff()

rev_difference

data_df['Monthly Revenue Delta'] = rev_difference
data_df.head()

# Calculate average revenue change
avg_monthly_delta = data_df['Monthly Revenue Delta'].mean()

print('Average Revenue Change: ' + '$' + str(round(avg_monthly_delta, 2)))

# Max revenue change
max_rev_change = data_df[['Date', 'Monthly Revenue Delta']][data_df['Monthly Revenue Delta'] == data_df['Monthly Revenue Delta'].max()]
max_rev_change_reset = max_rev_change.reset_index(drop=True)
max_date = max_rev_change_reset.loc[:,'Date'].values[0]
max_date

max_rev = max_rev_change_reset.loc[:,'Monthly Revenue Delta'].values[0]
max_rev

print('Greatest Increase in Revenue: {} ({})'.format(max_date, int(max_rev)))

# Min revenue change
min_rev_change = data_df[['Date', 'Monthly Revenue Delta']][data_df['Monthly Revenue Delta'] == data_df['Monthly Revenue Delta'].min()]
min_rev_change_reset = min_rev_change.reset_index(drop=True)
min_date = min_rev_change_reset.loc[:,'Date'].values[0]
min_date

min_rev = min_rev_change_reset.loc[:,'Monthly Revenue Delta'].values[0]
min_rev

print('Greatest Decrease in Revenue: {} ({})'.format(min_date, int(min_rev)))
