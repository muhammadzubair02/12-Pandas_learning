import pandas as pd
data_frame = pd.read_csv('HousePricePrediction.csv',
                         parse_dates=['Date'])

header = data_frame.head()
#print(header)
data_sorted = data_frame.sort_values(by=['SalePrice'], ascending=[True])
print(data_sorted)