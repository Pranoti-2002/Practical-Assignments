import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
#detecting the outliers 
df = pd.read_csv(r'C:\DSBDA\employees.csv') 
fig, ax = plt.subplots(figsize = (18,10))
ax.scatter(df['Salary'], df['Bonus %']) 
 
# x-axis label
ax.set_xlabel('Salary')
 
# y-axis label
ax.set_ylabel('Bonus') 
plt.show()

# printing outliers 
df = pd.read_csv(r'C:\DSBDA\employees.csv') 
print(np.where((df['Salary']>100000) & (df['Bonus %']>11)))

fig, ax = plt.subplots(figsize = (18,10))
ax.scatter(df['Salary'], df['Bonus %']) 
 
# x-axis label
ax.set_xlabel('Salary')
 
# y-axis label
ax.set_ylabel('Bonus')
plt.show()

df['Team'].fillna(value='Engineer', inplace=True)

print(df['Team'])  

print(df['Team'].isnull()) 

print(df['Team'].isnull().sum()) 

mean_value=df['Salary'].mean()



