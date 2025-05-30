import tkinter as tk
from tkinter import *
from tkinter import Checkbutton, Radiobutton

base=tk.Tk()
base.title("simple menu")
menu_bar=tk.Menu(base)
file_menu=tk.Menu(menu_bar)
file_menu.add_command(label="new")
file_menu.add_command(label="open")
file_menu.add_command(label="exit")
menu_bar.add_cascade(label="file",menu=file_menu)

base.config(menu=menu_bar)
#root.mainloop()

'''base.title("check box demo")

ch1=Checkbutton(base,text="pizza",width=15)
ch1.pack()

ch2=Checkbutton(base,text="burger",width=15)
ch2.pack()

ch3=Checkbutton(base,text="pestry",width=15)
ch3.pack()
group1=IntVar()
r1=Radiobutton(base,text="male")
r1.config(value=1,variable=group1)
r1.pack()

r2=Radiobutton(base,text="female")
r2.config(value=2,variable=group1)
r2.pack()'''
base.mainloop()