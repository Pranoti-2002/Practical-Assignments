import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('iris') 

print(dataset.head()) 

sns.histplot(dataset['sepal_length'], kde=True , linewidth=0) 

sns.jointplot(x='sepal_length', y='petal_length', data=dataset) 
plt.show()   