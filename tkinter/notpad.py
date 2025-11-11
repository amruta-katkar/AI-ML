# create notpad menues using tkinter
from tkinter import *
m = Tk()
m.title("Untitled - Notepad")
menu = Menu(m)
m.config(menu = menu)
# create file menu
filemenu = Menu(menu)
menu.add_cascade(label ='file',menu = filemenu)
filemenu.add_command(label = 'New')
filemenu.add_command(label = "Open")
filemenu.add_cascade(label ='Save')
filemenu.add_cascade(label ='Save as')
filemenu.add_cascade(label ='New Window')

filemenu.add_separator()
filemenu.add_command(label = "Exit",command = m.quit())
# Edit menu
Editmenu = Menu(menu)
menu.add_cascade(label = "Edit",menu = Editmenu)
Editmenu.add_command(label = "Undo")
Editmenu.add_command(label = "Cut")
Editmenu.add_command(label = "Copy")
Editmenu.add_command(label = "Paste")
Editmenu.add_separator()
Editmenu.add_command(label = "Select All")
Editmenu.add_command(label = "Time/Date")



# formatmnu
formatmenu = Menu(menu)
menu.add_cascade(label = "Format",menu = formatmenu)
formatmenu.add_command(label = "Word Wrap")
formatmenu.add_command(label = "Font")



# View menu
viewmenu = Menu(menu)
menu.add_cascade(label = "View",menu = viewmenu)
viewmenu.add_command(label = "zoom")
viewmenu.add_command(label = "status bar")

# Help menu
helpmenu = Menu(menu)
menu.add_cascade(label = "Help",menu = helpmenu)
helpmenu.add_command(label = "View Help")
helpmenu.add_command(label ="Send feedback")
helpmenu.add_separator()
helpmenu.add_command(label = "About Notepad")

m.mainloop()