import pandas as pd
# First we create a data
data = {
    'Name' : ['Arham','Hadi', 'Ayyan', 'Anas'],
    'Age' : [10, 6, 5, 2],
    'City' : ['Faisalabad', 'Islamabad', 'Lahore', 'Multan'],
    'Salary': [4000, 3000, 2000, 1000]
}

df = pd.DataFrame(data) #This line of code convert the data into dataframe

# Create a subset from df start from row 1 and go till row 3. and column is Only Name and Salary.
sub_set = df.loc[1:3, ['Name', 'Salary']]
print("This is the subset", sub_set)