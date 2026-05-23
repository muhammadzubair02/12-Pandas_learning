import pandas as pd
import openpyxl

data_frame = pd.read_csv('HousePricePrediction.csv',
                         parse_dates=['Date'],
                         )
#print(data_frame.head()) #Print the header of the data frame

print(data_frame.isna().sum()) #print the number of missinf values in data fram


#First we fill the missing values of the SalePrice column
data_frame['SalePrice'] = data_frame['SalePrice'].fillna(data_frame['SalePrice'].mode()[0]) 
#print(data_frame.isna().sum())

#Now we fill the the missing values of the 'MSZoning' column
data_frame['MSZoning'] = data_frame['MSZoning'].fillna(data_frame['MSZoning']).mode()[0]

#Now we fill the the missing values of the 'Exterior1st', 'BsmtFinSF2'and 'TotalBsmtSF' column
data_frame['Exterior1st'] = data_frame['Exterior1st'].fillna(data_frame['Exterior1st'].mode()[0]) 
data_frame['BsmtFinSF2'] = data_frame['BsmtFinSF2'].fillna(data_frame['BsmtFinSF2'].mode()[0]) 
data_frame['TotalBsmtSF'] = data_frame['TotalBsmtSF'].fillna(data_frame['TotalBsmtSF'].mode()[0])

# Print the final result
print(data_frame.isna().sum())