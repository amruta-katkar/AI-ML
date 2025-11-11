# Radiobutton using tkinter
from tkinter import *
m = Tk()
a = IntVar()
Radiobutton(m,text="Male",variable=a,value=1).pack(anchor=W)
Radiobutton(m,text="Female",variable=a,value=2).pack(anchor=W)
m.mainloop()