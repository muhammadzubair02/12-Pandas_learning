import pandas as pd
import openpyxl

data_frame = pd.read_csv('HousePricePrediction.csv',
                         parse_dates=['Date'],
                         )
print(data_frame.head()) #Print the header of the data frame

print(data_frame.isna().sum()) #print the number of missinf values in data fram