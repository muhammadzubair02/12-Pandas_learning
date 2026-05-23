import pandas as pd

data_frame = pd.DataFrame({
    'Name' : ['Muhammad Zubair ', 'Muhammad Awais', 'MUHAMMAD ANAS', 'Arham_abdullah']
})
print(data_frame)

# As we clearly see in above data frame that there are extra spaces and uper and lower case latters are present. now 
# need to clean tha data.

data_frame['Name'] = data_frame['Name'].str.strip().str.lower() # This line of code made change in original column

# We also make a new column

data_frame['Clean_Name'] = data_frame['Name'].str.strip().str.lower()
#print(data_frame)

#With another function we can replace the letter os the str
data_frame['Clean_Name'] = data_frame['Clean_Name'].str.replace('_', ' ')
#print(data_frame)


#we use all the menthod in once to clean the string like 
data_frame['Clean_Name'] = data_frame['Name'].str.strip().str.lower().str.replace('_', ' ')
print(data_frame)