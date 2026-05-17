import pandas as pd
# We create a data set
data = {
    'Name' : ['Arham','Hadi', 'Ayyan', 'Anas'],
    'Age' : [10, 6, 5, 2],
    'City' : ['Faisalabad', 'Islamabad', 'Lahore', 'Multan']
}
# We convert this data into data frame
data_frame = pd.DataFrame(data)
print(data_frame)