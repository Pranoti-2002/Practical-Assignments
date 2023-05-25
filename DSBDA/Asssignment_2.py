import pandas as pd 
import numpy as np 

df=pd.read_csv(r'C:\CSV_file\Academic-Performance-Dataset.csv') 
df.head()   

df['EM1_marks'].isnull().sum()  

df['math score'].describe()  

#replacing null values with mean of that column

mean_value=df['Total Marks'].mean()  
df['Total Marks'].fillna(mean_value , inplace=False)  
df['Total Marks'].head()   

#detecting outliers

def detect_outliers_iqr(column):
    # Calculate the first quartile (Q1) and third quartile (Q3)
    q1 = column.quantile(0.25)
    q3 = column.quantile(0.75)

    # Calculate the IQR (Interquartile Range)
    iqr = q3 - q1

    # Define the lower and upper bounds for outliers
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # Find the outliers
    outliers = column[(column < lower_bound) | (column > upper_bound)] 
    print(iqr) 
    print(lower_bound) 
    print(upper_bound)  
    return outliers

outliers = detect_outliers_iqr(df['Total Marks'])  
print("Outliers:", outliers)

# data transformation

transformed_data=np.log(df['Total Marks']) 
transformed_data
