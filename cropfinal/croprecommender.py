import tkinter as tk
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from tkinter import *
window=tk.Tk()
window.geometry('600x800')
window.title('Crop Recommender ')
window.configure(bg='green')
l1 = tk.Label(window,text='Crop Recommender',bg='white',fg='black',font=('Times New Roman',25))
l1.place(x=215,y=0)
l2 = tk.Label(window,text='Nitrogen',bg='green',fg='black',font=('Times New Roman',15))
l2.place(x=150,y=75)
txt1=tk.Entry(window)
txt1.place(x=300,y=75)
l3 = tk.Label(window,text='Phosphorus',bg='green',fg='black',font=('Times New Roman',15))
l3.place(x=150,y=150)
txt7 = tk.Entry(window)
txt7.place(x=300,y=150)
l4 = tk.Label(window,text='Potassium',bg='green',fg='black',font=('Times New Roman',15))
l4.place(x=150,y=225)
txt2=tk.Entry(window)
txt2.place(x=300,y=225)
l5 = tk.Label(window,text='Temperature',bg='green',fg='black',font=('Times New Roman',15))
l5.place(x=150,y=300)
txt3=tk.Entry(window)
txt3.place(x=300,y=300)
l6 = tk.Label(window,text='Humidity',bg='green',fg='black',font=('Times New Roman',15))
l6.place(x=150,y=375)
txt4=tk.Entry(window)
txt4.place(x=300,y=375)
l7 = tk.Label(window,text='pH Value',bg='green',fg='black',font=('Times New Roman',15))
l7.place(x=150,y=450)
txt5=tk.Entry(window)
txt5.place(x=300,y=450)
l8 = tk.Label(window,text='Rain Fall',bg='green',fg='black',font=('Times New Roman',15))
l8.place(x=150,y=525)
txt6=tk.Entry(window)
txt6.place(x=300,y=525)

def stroke():
    global l10
    a = float(txt1.get())
    b = float(txt7.get())
    c = float(txt2.get())
    d = float(txt3.get())
    e = float(txt4.get())
    f = float(txt5.get())
    g = float(txt6.get())
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt
    # load test
    dataset = pd.read_csv('Crop_recommendation.csv')
    income_set = set(dataset['label'])
    dataset['label'] = dataset['label'].map({'rice': 0, 'maize': 1, 'chickpea': 2, 'kidneybeans': 3,'pigeonpeas':4,'mothbeans':5,'mungbean':6,'blackgram':7,'lentil':8,'pomegranate':9,'banana':10,'mango':11,'grapes':12,'watermelon':13,'muskmelon':14,'apple':15,'orange':16,'papaya':17,'coconut':18,'cotton':19,'jute':20,'coffee':21}).astype(float)
    x = dataset['N'].median()
    dataset['N'].fillna(x, inplace=True)
    y = dataset['P'].median()
    dataset['P'].fillna(y, inplace=True)
    z = dataset['K'].median()
    dataset['K'].fillna(z, inplace=True)
    x1 = dataset['temperature'].median()
    dataset['temperature'].fillna(x1, inplace=True)
    y1 = dataset['humidity'].median()
    dataset['humidity'].fillna(y1, inplace=True)
    z1 = dataset['ph'].median()
    dataset['ph'].fillna(z1, inplace=True)
    zz = dataset['rainfall'].median()
    dataset['rainfall'].fillna(zz, inplace=True)

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
    model = DecisionTreeClassifier(criterion='entropy', max_depth=100, random_state=0)
    model.fit(X_train, y_train)
    newEmp = [[a,b,c,d,e,f,g]]
    result = model.predict(newEmp)
    print("Result ", result)

    if result == 0:
        l10 = tk.Label(window, text='Sutaible Crop Rice', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 1:
        l10 = tk.Label(window, text='Sutiable crop Maize', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 2:
        l10 = tk.Label(window, text='Sutiable crop Chickpea', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 3:
        l10 = tk.Label(window, text='Sutiable crop Kidney beans', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 4:
        l10 = tk.Label(window, text='Sutiable crop Pigeon Peas', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 5:
        l10 = tk.Label(window, text='Sutiable crop Moth Beans', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 6:
        l10 = tk.Label(window, text='Sutiable crop Mug Beans', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 7:
        l10 = tk.Label(window, text='Sutiable crop Blackgrams', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 8:
        l10 = tk.Label(window, text='Sutiable crop Lentil', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 9:
        l10 = tk.Label(window, text='Sutiable crop Pomegranate', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 10:
        l10 = tk.Label(window, text='Sutiable crop Banana', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 11:
        l10 = tk.Label(window, text='Sutiable crop Mango', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 12:
        l10 = tk.Label(window, text='Sutiable crop Grapes', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 13:
        l10 = tk.Label(window, text='Sutiable crop Watermelon', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 14:
        l10 = tk.Label(window, text='Sutiable crop Muskmelon', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 15:
        l10 = tk.Label(window, text='Sutiable crop Apple', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 16:
        l10 = tk.Label(window, text='Sutiable crop Orange', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 17:
        l10 = tk.Label(window, text='Sutiable crop Papaya', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 18:
        l10 = tk.Label(window, text='Sutiable crop Coconut', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 19:
        l10 = tk.Label(window, text='Sutiable crop Cotton', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 20:
        l10 = tk.Label(window, text='Sutiable crop Jute', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    elif result == 21:
        l10 = tk.Label(window, text='Sutiable crop Coffee', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=250, y=750)
    else:
        l10 = tk.Label(window, text='Not Enough Data', bg='light green', fg='black', font=('Times New Roman', 15))
        l10.place(x=150, y=750)
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