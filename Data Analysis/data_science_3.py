import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 How many apps in the 'BUSINESS' 'Category' are there?
print(df['Category'].value_counts()) 
#246

# 2 What is the ratio of apps for teenagers ('Teen') to those for children over 10 years old ('Everyone 10+')?
# Round the answer to the nearest hundredth.
print(df['Content Rating'].value_counts())
print(868/318)
#2.73

# 3.1 What is the average 'Rating' of 'Paid' apps? 
# Round the answer to the nearest hundredth.
print(df.groupby(by = 'Type')['Rating'].mean())
#4.25

# 3.2 How much lower is the average 'Rating' of 'Free' apps than the average rating of 'Paid' apps?
# Round the answer to the nearest hundredth.
print(4.247957 - 4.171955)
#0.08

# 4 What are the minimum and maximum app 'Size' in the 'COMICS' 'Category'?
# Round the answer to the nearest hundredth.
print(df.groupby(by = 'Category')['Size'].min())
print(df.groupby(by = 'Category')['Size'].max())
#0.43 and 40.0

# Bonus 1. How many apps have a 'Rating' of strictly greater than 4.5 in the 'FINANCE' 'Category'?
print(df[df['Rating'] > 4.5]['Category'].value_counts())
#64

# Bonus 2. What is the ratio of 'Free' to 'Paid' games with a 'Rating' greater than 4.9?
print(df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts())
print(8/4)
#2
