import pandas as pd 
import seaborn as sns
df=sns.load_dataset('iris')  
df.head() 

summary_stats = df.groupby('species')['sepal_length'].describe() 
summary_stats 

iris_set = (df['species']== 'setosa') 
df[iris_set].describe() 

iris_set = (df['species']== 'versicolor')  
df[iris_set].describe() 

iris_set = (df['species']== 'virginica')  
df[iris_set].describe() 

