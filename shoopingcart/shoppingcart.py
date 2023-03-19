import tkinter as tk
from tkinter import*
from tkinter import messagebox
BGC="white"
FGC="black"
root = tk.Tk()
root.geometry("600x600")
root.title("Shopping Cart")
root.resizable(False,False)
root.configure(bg=BGC)
l1= tk.Label(root , text='Welcome to shopping Cart')
l1.place(x= 250, y= 50)
l2= tk.Label(root , text='Electronics')
l2.place(x= 130, y= 350)
l4= tk.Label(root , text='Furniture')
l4.place(x= 290, y= 350)
l3= tk.Label(root , text='Diary Products')
l3.place(x= 430, y= 350)
def b1ele():
    if  messagebox.showinfo("Buy",f"Add"):
        root.destroy()
b1=tk.Button(root, text='Buy', command=b1ele)
b1.place(x=150, y= 400)
b2=tk.Button(root, text='Buy')
b2.place(x=300, y= 400)
b3=tk.Button(root, text='Buy')
b3.place(x=450, y= 400)
b4=tk.Button(root, text='Bill')
b4.place(x=300, y= 500)
root.mainloop()