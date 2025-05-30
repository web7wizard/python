from tkinter import *
import tkinter as tk

base=tk.Tk()
base.title("form")
l1=Label(base,text="name")
l2=Entry(base,width=20)
group1=IntVar();
l3=Radiobutton(base,text="female")
l3.config(value=1,variable=group1)
l4=Radiobutton(base,text="male")
l4.config(value=2,variable=group1)
l7=Label(base,text="select")
l5=Checkbutton(base,text="complete 10")
l6=Checkbutton(base,text="complete 12")
l8=Button(base,text="submit")
l1.pack()
l2.pack()
l3.pack()
l4.pack()
l7.pack()
l5.pack()
l6.pack()
base.mainloop()
