from tkinter import *

app = Tk()
app.title("iMouse")

# Command List
Lb = Listbox(app)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.grid(row=0, column=0, rowspan=3)

# Position
Label(app, text='X Pos', width=10).grid(row=0, column=1, pady=1)
Label(app, text='Y Pos', width=10).grid(row=0, column=2, pady=1)
e1 = Entry(app, width=10)
e2 = Entry(app, width=10)
e1.grid(row=1, column=1)
e2.grid(row=1, column=2)

# Button Add Click Command
btnClick = Button(app, text='Add Click', width=20, command=app.destroy).grid(row=2, column=1, columnspan=2, padx=5)

app.mainloop()