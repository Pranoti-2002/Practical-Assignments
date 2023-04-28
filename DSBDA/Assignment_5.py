import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay,classification_report,accuracy_score, precision_score, recall_score, f1_score

#Loading dataset
data =  pd.read_csv(r'C:\DSBDA\Social_Network_Ads.csv')
print(data.head())
#print(data.info())

#Checking null values
print(data.isnull().sum())

#Loading 'Age', 'Estimated_salary' as the features in 'x'  and 'Purchased' as the target variable in 'y'
x = data.iloc[:,2:4]
y = data.iloc[:,4]   

#Spliting data into 75% training and 25% testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

#scaling the dataset for equal contribution in training and testing 
scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.transform(x_test)

#Preparing and Training our Logistic Regression model with the training and testing data
lr = LogisticRegression(random_state = 0,solver = 'lbfgs')
lr.fit(x_train,y_train)
pred = lr.predict(x_test)
       
print(x_test[:10]) 
print('-'*15)
print(pred[:10])

print('Expected Output:',pred[:15]) 
print('-'*15)
print('Predicted Output:\n',y_test[:15])

#confusion matrix
matrix = confusion_matrix(y_test,pred,labels = lr.classes_)
print(matrix)

tp, fn, fp, tn = confusion_matrix(y_test,pred,labels=[1,0]).reshape(-1)
conf_matrix = ConfusionMatrixDisplay(confusion_matrix=matrix,display_labels=lr.classes_)
conf_matrix.plot(cmap=plt.cm.Reds)
plt.show()

#Determining the Accuracy,Error Rate,Recall,Precision of the model 
print('\nAccuracy: {:.2f}'.format(accuracy_score(y_test,pred)))
print('Error Rate: ',(fp+fn)/(tp+tn+fn+fp))
print('Sensitivity (Recall or True positive rate) :',tp/(tp+fn))
print('Specificity (True negative rate) :',tn/(fp+tn))
print('Precision (Positive predictive value) :',tp/(tp+fp))
print('False Positive Rate :',fp/(tn+fp))

