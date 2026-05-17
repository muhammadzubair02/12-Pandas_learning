#First we install the python pandas library by using the pip install pandas

#we import pandas as pd. pd is a industrial standard 
import pandas as pd


#We create a series 
s = pd.Series([10,20,20,30,40], index = ['a','b','c','d','e'])
print(s)

#This function is use to print the only values of the series
print("Values: ", s.values) #1st Method to print the value of the series
values = s.values #1st Method to print the value of the series
print("Values are: ", values)

#This function is use to print the only index of the series
print("Indexs: ", s.index) #1st Method to print the indexes of the series

print("Type: ", s.dtype) #Print the type of the series
print("Header: ", s.head) #Print the head of the series
print("Tail: ", s.tail) #Print the tail of the series