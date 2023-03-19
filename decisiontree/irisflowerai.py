import pandas as pd
import numpy  as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#load test
dataset = pd.read_csv('IRIS.csv')
print(dataset.columns[dataset.isna().any()])
income_set = set(dataset['species'])

dataset['species']= dataset['species'].map({'Iris-setosa': 0,'Iris-versicolor':1,'Iris-virginica':2}).astype(int)
#Load summarize
print(dataset.head)
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)
print(X_train.shape)
print(X_test.shape)
#Finding best max depth value
accuracy = []
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
for i in range (1, 10):
    model= DecisionTreeClassifier (max_depth = i, random_state = 0)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    score = accuracy_score(y_test, pred)
    accuracy.append(score)
plt.figure(figsize=(12, 6))
plt.plot(range (1, 10), accuracy, color='red', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)
plt.title('Finding best Max_Depth')
plt.xlabel('pred')
plt.ylabel('score')
plt.show()
#traning
from sklearn.tree import DecisionTreeClassifier
model= DecisionTreeClassifier (criterion = 'entropy', max_depth=3,random_state =0)
model.fit(X_train, y_train)
newEmp= [[6.9,3.1,5.4,2.1]]
result = model.predict(newEmp)
print("Result ", result)
if result==0:
    print("Leaf Species is Setosa")
elif result==1:
    print("Leaf Species is Versicolour")
else:
    print("Leaf Species is Virginica")
#Prediction
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, pred)
print("Confusion Matrix: ")
print (cm)
print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, pred)*100))