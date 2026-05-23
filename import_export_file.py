import pandas as pd
import openpyxl #we install the library openpyxl for handle the excel file

df = pd.read_csv("HousePricePrediction.csv",
                 parse_dates=['Id'],
                 dtype={'LotArea': 'float64',
                        'SalePrice': 'float64' })

# print(df.columns)
print(df.info())