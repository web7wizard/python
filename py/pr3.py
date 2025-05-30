import tkinter as tk
from tkinter import *
base=tk.Tk();
base.title("mennu demo")
menu_bar=tk.Menu(base)

file_menu=tk.Menu(menu_bar)
edit_menu=tk.Menu(menu_bar)

file_menu.add_command(label="new")
file_menu.add_command(label="open")
file_menu.add_command(label="exit")
menu_bar.add_cascade(label="file",menu=file_menu)

edit_menu.add_command(label="undo")
edit_menu.add_command(label="redo")
menu_bar.add_cascade(label="edit",menu=edit_menu)
base.config(menu=menu_bar)
base.mainloop()
