import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('iris') 
sns.boxplot(x='sepal_length' , y='petal_length' ) 

plt.show() 