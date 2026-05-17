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

#now we ask pandas to read the file and upload the data fram
data_frame_file = pd.read_csv('HousePricePrediction.csv')
print(data_frame_file.info())


print("shap: ", data_frame_file.shape) #Print the shape of the data set
print("type: ", data_frame_file.dtypes) #Print the type of the data set

print("Statistical Explaination: ", data_frame_file.describe) #This function is give more detail of the data set.