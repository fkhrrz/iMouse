from tkinter import *
from uuid import getnode as get_mac
import re
import time
import win32api, win32con

# Begin Function Section
def iMouse():
    for x in Lb.get(0, END):
        xPos = int(x.split(",")[0])
        yPos = int(x.split(",")[1])
        if x == "Click":
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,xPos,yPos,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,xPos,yPos,0,0)
        else :
            win32api.SetCursorPos((xPos,yPos))

def testing():
    if len(xPos.get()) > 0 and len(yPos.get()) > 0:
        if re.search("[^0-9]", xPos.get()):
            print("Wrong Format X Position")
        elif re.search("[^0-9]", yPos.get()):
            print("Wrong Format Y Position")
        else :
            Lb.insert((Lb.size() + 1),xPos.get()+","+yPos.get())
    else :
        if len(xPos.get()) == 0:
            print("Fill X Position")
        elif len(yPos.get()) == 0:
            print("Fill Y Position")

def getPosition():
    xPos.delete(0,END)
    xPos.insert(0,win32api.GetCursorPos()[0])
    yPos.delete(0,END)
    yPos.insert(0,win32api.GetCursorPos()[1])
# End Function Section

app = Tk()
app.title("iMouse")
app.iconbitmap(r"X:\www\Job Project\bankindex\i\Circle-red.ico")

# Command List
Lb = Listbox(app)
Lb.grid(row=0, column=0, rowspan=4)

# X Position
Label(app, text='X Pos', width=10).grid(row=0, column=1, pady=1)
xPos = Entry(app, width=10)
xPos.grid(row=1, column=1)
# Y Position
Label(app, text='Y Pos', width=10).grid(row=0, column=2, pady=1)
yPos = Entry(app, width=10)
yPos.grid(row=1, column=2)

# Button Add Click Command
btnClick = Button(app, text='Add Position', width=20, command=testing).grid(row=2, column=1, columnspan=2, padx=5)
btnStart = Button(app, text='Start', width=20, command=iMouse).grid(row=3, column=1, columnspan=2, padx=5)

def isKeyPressed(key):
    return (win32api.GetKeyState(key) & (1 << 7)) != 0

wasKeyPressedTheLastTimeWeChecked = False
while True:
    keyIsPressed = isKeyPressed(ord('T'))
    if keyIsPressed and not wasKeyPressedTheLastTimeWeChecked:
        getPosition()
    wasKeyPressedTheLastTimeWeChecked = keyIsPressed
    # app.mainloop()
    app.update_idletasks()
    app.update()
    time.sleep(0.01)