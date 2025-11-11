# # text using tkinter
from tkinter import *
m = Tk()

txt = Text(m,height=3,width=40)
txt.pack()
txt.insert(END,"python is key learning for data science")
m.mainloop()