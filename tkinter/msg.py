# message using tkinter
from tkinter import *
m = Tk()
msg = "This is GUI using Tkinter"
msgmain = Message(m,text=msg)
msgmain.config(bg="green")
msgmain.pack()
m.mainloop()