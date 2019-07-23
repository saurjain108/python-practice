import pandas as pd
import re
df = pd.read_csv('pokemon_data.csv')
print(df.head(3)) #printing top 3
print(df.tail(3)) # printing bottom 3
#df_excel = pd.read_excel('excel file') #inputing excel file
print(df.columns[1]) #first column
print(df['Name']) #input Name colume
print(df[['Name', 'HP']]) #input name and HP column
print("#######")
print(df.iloc[0])  #printing first row
print(df.iloc[2,1]) #printing a specific location
for i, j in df.iterrows():
    print(i,j)
print(df.loc[df['Type 1'] == "Fire"]) # output the data with ['Type 1'] == "Fire"
print(df.describe()) # high level stats
print(df.sort_values(['Type 1','HP'], ascending=[0,0])) # the [0,0] represent ascending for ['Type 1','HP']
df['Total'] = df.iloc[1:3, 4:10].sum(axis=1) # this will hive total of rows in between 1-3 and cols 4-10 and create new
#column at the end called Total
print(df.head(4))


#writting to a specific file
df.to_csv('modified.csv', index= False)
df.to_excel('modified.xlsx', index= False)


#filering data

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
new_df = new_df.reset_index() #resetting index
print(new_df)
new_df.to_csv('filter.csv') # added filtered data to new csv file

#filtering with regex
new_regex = df.loc[df['Type 1'].str.contains('fire|grass', flags= re.I, regex=True)]
print(new_regex)
new_regex2 =df.loc[df['Name'].str.contains('^pi[a-z]*', flags= re.I, regex=True)]
print(new_regex2)
