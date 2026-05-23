import pandas as pd
import openpyxl #we install the library openpyxl for handle the excel file

# df = pd.read_csv("HousePricePrediction.csv",
#                  parse_dates=['Id'],
#                  dtype={'LotArea': 'float64',
#                         'SalePrice': 'float64' })

# print(df.columns)
#print(df.info())  #Show the info of data frame with a bove values
df = pd.read_csv("HousePricePrediction.csv")
clean_df = df[df['SalePrice'] <150000] #clean the data hows saleprice is less then 150k
#print(clean_df.info())

sub_set = clean_df[['Id', 'LotArea', 'TotalBsmtSF', 'SalePrice']] # Create a subset with the following columns
#print(sub_set)

sub_set.to_excel("subset house price.xlsx") #Expoert the subset in excel format

print("File exported")
sub_set.info()
