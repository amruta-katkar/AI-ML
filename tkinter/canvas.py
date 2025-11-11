# using tkinter create canvas
from tkinter import *
import tkinter as tk
master = tk.Tk()
w = Canvas(master,width = 40,height = 60)
w.pack()
cn_height = 20
cn_width = 200
w.create_line(0,cn_height,cn_width,cn_height)
mainloop()