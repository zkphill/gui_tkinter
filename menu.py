from tkinter import *
from tkinter import messagebox

def app_about():
    messagebox.showinfo(title = 'About', message = 'This app is the best!!!!')
    return

def exit():
    exit = messagebox.askyesno(title = 'Close', message = 'Get on with it!')
    if exit == 1:
        app_gui.destroy()

    return

app_gui = Tk()

app_gui.geometry('800x400+300+400')
app_gui.title('My App')

app_menu = Menu(app_gui)

file_menu = Menu(app_menu, tearoff = 0)
file_menu.add_command(label = "About", command = app_about)
file_menu.add_command(label = 'Close', command = exit)

app_menu.add_cascade(label = 'File', menu = file_menu)

app_gui.config(menu = app_menu)

app_gui.mainloop()
