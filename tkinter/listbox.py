# using tkinter listbox
from tkinter import *
m = Tk()
m.title("Listbox")
lst = Listbox(m)
lst.insert(1,"Python")
lst.insert(2,"Java")
lst.insert(3,"R")
lst.insert(4,"git")
lst.pack()
m.mainloop()