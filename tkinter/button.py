# tkinter button
import tkinter as tk
m = tk.Tk()
m.title("My First GUI")
button = tk.Button(m, text="Click me", command=lambda: print("Button clicked"))
button.pack()
m.mainloop()