import matplotlib.pyplot as plt
import seaborn as sns 
dataset = sns.load_dataset('iris') 
print(dataset.head()) 

# features - sepal_length , sepal_width , petal_width , petal_length which are numeric in type 
# species feature is categorical in type 

fig, axes = plt.subplots( 2 , 2) 
 
sns.histplot(dataset['sepal_length'] , ax=axes[0 , 0])   
sns.histplot(dataset['sepal_width'] , ax=axes[0 , 1])  
sns.histplot(dataset['petal_length'] , ax=axes[1 , 0])  
sns.histplot(dataset['petal_width'] , ax=axes[1 , 1])   
plt.show() 

fig, axes = plt.subplots( 2 , 2) 

sns.boxplot(y='petal_length' , x='species' , data=dataset , ax=axes[0 , 0])  
sns.boxplot(y='sepal_length' , x='species' , data=dataset , ax=axes[0 , 1]) 
sns.boxplot(y='sepal_length' , x='species' , data=dataset , ax=axes[1 , 0]) 
sns.boxplot(y='sepal_length' , x='species' , data=dataset , ax=axes[1 , 1]) 

plt.show()   



