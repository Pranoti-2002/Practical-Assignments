import pandas as pd  
import numpy as np
from sklearn import preprocessing

df = pd.read_csv(r'C:\DSBDA\employees.csv') 
print(df) 
print(df.dtypes)

print(df.head())  #df=np.array([2 , 3 , 4, 5 , 6 , 7] )

normalized_arr = preprocessing.normalize([df['Salary']]) 
print(normalized_arr) 


print(df.head()) 

print(df) 

#checking missing values in dataset 
print(df['Team'].isnull()) 

#describe function 

print(df.describe()) 

print(df['Team'].isnull().sum())  

