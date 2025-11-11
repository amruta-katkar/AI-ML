# using tkinter create checkbox
from tkinter import *
m = Tk()
a = IntVar()
b = IntVar()

Checkbutton(m ,text = "Check1", variable = a).grid(row = 0,sticky = W)
Checkbutton(m ,text = "Check2", variable = b).grid(row = 1,sticky = W)

mainloop()