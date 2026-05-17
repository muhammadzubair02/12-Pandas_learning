import pandas as pd
# First we create a data
data = {
    'Name' : ['Arham','Hadi', 'Ayyan', 'Anas'],
    'Age' : [10, 6, 5, 2],
    'City' : ['Faisalabad', 'Islamabad', 'Lahore', 'Multan'],
    'Salary': [4000, 3000, 2000, 1000]
}

df = pd.DataFrame(data) #This line of code convert the data into dataframe

# Create a subset from df start from row 1 and go till row 3. and column is Only Name and Salary.{Use loc function}
sub_set_loc = df.loc[1:3, ['Name', 'Salary']]
print("This is the subset", sub_set_loc)

# Create a subset from df start from row 0 and go till row 3. and column from 1 to 3.{Use iloc function}
sub_set_iloc = df.iloc[0:3, 1:3]
print("This is the subset", sub_set_iloc)

#Difference between loc and loc
#loc: In loc we use numeric value as well as string to tell the range as you see sub_set_loc = df.loc[1:3, ['Name', 'Salary']].
#loc: In loc all the elements of range are print 

#iloc: In iloc we use numeric value only as you see sub_set_iloc = df.iloc[0:3, 1:3].
#loc: In iloc all elements less than our giving range are print for example when we give 0:3. this print the element form 0 to 2.