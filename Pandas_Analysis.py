import pandas as pd 

# 1 Load the CSV file into a DataFrame.

df = pd.read_csv('people_dataset_75.csv')
#  print(df)

# 2 Display the first 10 rows

# print(df.head(10))

# Display the last 5 rows.

# print(df.tail(5))

#  4 Find the total number of records.

# print(df['Person_ID'].value_counts())

#  5  Find the data type of each column

# print(df['Person_ID'].dtype)
# print(df['Name'].dtype)
# print(df['Age'].dtype)
# print(df['Gender'].dtype)
# print(df['Height_cm'].dtype)
# print(df['Weight_kg'].dtype)
# print(df['City'].dtype)
# print(df['Activity_Level'].dtype)



# 6 Display all column names.

# print(df.columns)

# 7 = Find the average age of all participants

# print(df['Age'].mean())

# 8 = Find the maximum and minimum height.

# print(df['Height_cm'].min() , df['Height_cm'].max())


# 9 = Count the number of males and females
male = df['Gender'].value_counts()
# print(male)

# 10 Find the number of participants from each city.


participant = df.groupby('City')['Person_ID'].count()
# print(participant)

# 11 Find all participants older than 40 years.

forty = df[df['Age']>40]['Name']
# print(forty)

# 12 Find all participants whose weight is greater than 80 kg.

weight = df[df['Weight_kg']>80]['Name']
# print(weight)

# 13 Find all participants whose height is between 160 cm and 180 cm.

height = df[df['Height_cm'].between(160 , 180)]['Name']
# print(height)

# 14 Find participants who belong to Mumbai and have High activity level.

belong = df[(df['City']=='Mumbai') & (df['Activity_Level']=='High')]['Name']
# print(belong)

# 15 Find the average weight for each city.

avrg = df.groupby('City')['Weight_kg'].mean()
# print(avrg)

# 16 Find the average height for each gender 

agr = df.groupby('Gender')['Height_cm'].mean()
# print(agr)

# 17 = Count participants in each activity level

level = df.groupby('Activity_Level')['Person_ID'].count()
# print(level)

# 18 Find the city with the highest average age.

high = df.groupby('City')['Age'].mean().sort_values().tail(1)

# print(high)



# 19 List the top 10 oldest participants.

oldest = df.sort_values(by='Age',ascending=False ).head(10)['Person_ID']
# print(oldest)

# 20 Find all participants whose weight is above the overall average weight.
over = df['Weight_kg'].mean()
hgh = df[df['Weight_kg']>over]['Person_ID']
# print(hgh)

# 21 Create a pivot table showing average weight by city and gender

piv = df.pivot_table(values="Weight_kg" , index = 'Gender' , columns='City' , aggfunc='mean')
# print(piv)

# 22 Create a pivot table showing participant counts by city and activity level.
pt = df.pivot_table(values='Person_ID',index='Activity_Level' , columns='City' , aggfunc='count')
# print(pt)


# 23 Rank all participants based on weight from highest to lowest.
df['Rank'] = df['Weight_kg'].rank(ascending=False)
# print(df['Rank'])

# 24 = Find the top 5 tallest people in each city.

tall = df.sort_values(['Height_cm'],ascending=False).groupby('City').head(5)
# print(tall)

# 25 = For each city, calculate:
# Average Age
# Average Height
# Average Weight
# Participant Count
afg = df.groupby('City')[['Age','Height_cm','Weight_kg']].mean()

fg = df.groupby('City')['Person_ID'].size()
# print(afg)
# print(fg)


# 26 = Find the percentage of males and females in the dataset.

man = (df['Gender']=='Male').sum()
woman = (df['Gender']=='Female').sum()

total = len(df)
woman_per = (woman/total)*100

man_per =  (man/total)*100

# print(man_per,woman_per)

# 28 For each city, identify:
# Oldest participant
# Tallest participant
# Heaviest participa
oldest = df.sort_values('Age', ascending=False).groupby('City').head(1)

tallest = df.sort_values('Height_cm', ascending=False).groupby('City').head(1)

heaviest = df.sort_values('Weight_kg', ascending=False).groupby('City').head(1)












