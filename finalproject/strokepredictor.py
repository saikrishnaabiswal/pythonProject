import tkinter as tk
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from tkinter import *
window=tk.Tk()
window.geometry('600x800')
window.title('Stroke Predictor ')
window.configure(bg='light blue')
l1 = tk.Label(window,text='Stroke Predictor',bg='white',fg='black',font=('Times New Roman',25))
l1.place(x=215,y=0)
l2 = tk.Label(window,text='Gender',bg='light blue',fg='black',font=('Times New Roman',15))
l2.place(x=150,y=75)
click = StringVar()
click.set("--Select--")
drop = OptionMenu(window, click,"Male","Female")
drop.place(x=300,y=75)
l3 = tk.Label(window,text='Age',bg='light blue',fg='black',font=('Times New Roman',15))
l3.place(x=150,y=150)
txt1=tk.Entry(window)
txt1.place(x=300,y=150)
l4 = tk.Label(window,text='Hyper Tension',bg='light blue',fg='black',font=('Times New Roman',15))
l4.place(x=150,y=225)
click1 = StringVar()
click1.set("--Select--")
drop1 = OptionMenu(window, click1,"Yes","No")
drop1.place(x=300,y=225)
l5 = tk.Label(window,text='Heart Disease',bg='light blue',fg='black',font=('Times New Roman',15))
l5.place(x=150,y=300)
click2 = StringVar()
click2.set("--Select--")
drop2 = OptionMenu(window, click2,"Yes","No")
drop2.place(x=300,y=300)
l6 = tk.Label(window,text='Married',bg='light blue',fg='black',font=('Times New Roman',15))
l6.place(x=150,y=375)
click3 = StringVar()
click3.set("--Select--")
drop3 = OptionMenu(window, click3,"Yes","No")
drop3.place(x=300,y=375)
l7 = tk.Label(window,text='Work Type',bg='light blue',fg='black',font=('Times New Roman',15))
l7.place(x=150,y=450)
click4 = StringVar()
click4.set("--Select--")
drop4 = OptionMenu(window, click4,"Private","Self Employed","Government Job","Children")
drop4.place(x=300,y=450)
l8 = tk.Label(window,text='Residence',bg='light blue',fg='black',font=('Times New Roman',15))
l8.place(x=150,y=525)
click5 = StringVar()
click5.set("--Select--")
drop5 = OptionMenu(window, click5,"Urban","Rural")
drop5.place(x=300,y=525)
l9 = tk.Label(window,text='Smokes',bg='light blue',fg='black',font=('Times New Roman',15))
l9.place(x=150,y=600)
click6 = StringVar()
click6.set("--Select--")
drop6 = OptionMenu(window, click6,"Never Smokes","Smokes","Formaly Smokes")
drop6.place(x=300,y=600)
def stroke():
    global l10
    a=click.get()
    if a == 'Male':
        a1 = 1
    else:
        a1 = 0
    b = click1.get()
    if a == 'Yes':
        b1 = 1
    else:
        b1 = 0
    c = click2.get()
    if c == 'Yes':
        c1 = 1
    else:
        c1 = 0
    d = click3.get()
    if d == 'Yes':
        d1 = 1
    else:
        d1 = 0
    e = click4.get()
    if e == 'Private':
        e1 = 0
    elif e == 'Self Employed':
        e1 = 1
    elif e == 'Children':
        e1 = 3
    elif e == 'Government Job':
        e1 = 2
    else:
        e1 =4
    f = click5.get()
    if f == 'Urban':
        f1 = 1
    else:
        f1 = 0
    g = click6.get()
    if g == 'Never Smokes':
        g1 = 0
    elif g == 'Smokes':
        g1 = 1
    else:
        g1 = 2
    h = int(txt1.get())
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt
    # load test
    dataset = pd.read_csv('stroke.csv')
    income_set = set(dataset['stroke'])
    dataset['gender'] = dataset['gender'].map({'Female': 0, 'Male': 1}).astype(float)
    dataset['ever_married'] = dataset['ever_married'].map({'No': 0, 'Yes': 1}).astype(float)
    dataset['work_type'] = dataset['work_type'].map({'Private': 0, 'Self-employed': 1,'Govt_job':  2,'children': 3}).astype(float)
    dataset['Residence_type'] = dataset['Residence_type'].map({'Urban': 1, 'Rural': 0}).astype(float)
    dataset['smoking_status'] = dataset['smoking_status'].map({'formerly smoked': 0, 'never smoked': 1, 'smokes': 2,'Unknown': 3}).astype(float)
    x = dataset['gender'].median()
    dataset['gender'].fillna(x, inplace=True)
    y = dataset['ever_married'].median()
    dataset['ever_married'].fillna(y, inplace=True)
    z = dataset['work_type'].median()
    dataset['work_type'].fillna(z, inplace=True)
    x1 = dataset['Residence_type'].median()
    dataset['Residence_type'].fillna(x1, inplace=True)
    y1 = dataset['smoking_status'].median()
    dataset['smoking_status'].fillna(y1, inplace=True)

    print(dataset.head)
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, -1].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
    accuracy = []
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    import matplotlib.pyplot as plt
    for i in range(1, 10):
        model = DecisionTreeClassifier(max_depth=i, random_state=0)
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        score = accuracy_score(y_test, pred)
        accuracy.append(score)
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(criterion='entropy', max_depth=10000, random_state=0)
    model.fit(X_train, y_train)
    newEmp = [[a1,h,b1,c1,d1,e1,f1,g1]]
    result = model.predict(newEmp)
    print("Result ", result)
    if result == 1:
        l10 = tk.Label(window, text='Will  get stroke', bg='red', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 0:
        l10 = tk.Label(window, text='Will not get stroke', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    else:
        l10 = tk.Label(window, text='Not Enough Data', bg='yellow', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    from sklearn.metrics import confusion_matrix, accuracy_score
    cm = confusion_matrix(y_test, pred)
    print("Confusion Matrix: ")
    print(cm)
    print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, pred) * 100))
b1 = tk.Button(window,text='predict',command=stroke)
b1.place(x=200,y=675)

def clear():
    l10.destroy()
b6 = tk.Button(window,text='clear',command=clear)
b6.place(x=400,y=675)





window.mainloop()