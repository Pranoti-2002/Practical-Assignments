import pandas as pd  
df = pd.read_csv(r'C:\DSBDA\HousingData.csv') 

print("percentile value in Salary is" ,df['Salary'].quantile(0.5)) 
gk = df.groupby('Salary') 
print(gk.first()) 

print(df) 

print("Mean of the salary column is" ,df['Salary'].mean())

print("Median of salary column is" ,df['Salary'].median()) 

print("Maximum value in Salary is" ,df['Salary'].max())  

print("Minimum value in Salary is" ,df['Salary'].min()) 

print("Standard deviation of Salary column is" ,df['Salary'].std()) 
