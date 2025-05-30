import tkinter as tk
from tkinter import *
base=tk.Tk();
base.title("login form")
l1=Label(base,text="user name")
l2=Label(base,text="passward")
t1=Entry(base,width=13)
t2=Entry(base,width=13,show="*")
b1=Button(base,text="sign in")

l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
t1.grid(row=2,column=0)
t2.grid(row=2,column=1)
b1.grid(row=3,column=1)

base.mainloop()

