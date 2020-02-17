from tkinter import *
from uuid import getnode as get_mac
import re
import time
import pywin32_system32, win32api, win32con

runFlag = False

# Begin Function Section
def iMouse():
    for x in Lb.get(0, END):
        if x == "Left Click":
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,xPos,yPos,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,xPos,yPos,0,0)
        elif x == "Right Click":
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,xPos,yPos,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,xPos,yPos,0,0)
        else :
            xPos = int(x.split(",")[0])
            yPos = int(x.split(",")[1])
            win32api.SetCursorPos((xPos,yPos))
        time.sleep(0.2)

def checkEntry(target,val):
    if re.search("[^0-9]", val.get()):
        illegalChar = re.compile("[^0-9]")
        illegalPos = int
        for m in illegalChar.finditer(val.get()):
            illegalPos = m.start()
        if target == 'x':
            xPos.delete(illegalPos, illegalPos+1)
        elif target == 'y':
            yPos.delete(illegalPos, illegalPos+1)

def addPosition():
    if len(xPos.get()) > 0 and len(yPos.get()) > 0:
        Lb.insert((Lb.size() + 1), xPos.get()+","+yPos.get())
    elif len(xPos.get()) == 0 :
        win32api.MessageBox(0, "Fill X Position", "Alert")
    elif len(yPos.get()) == 0:
        win32api.MessageBox(0, "Fill Y Position", "Alert")

def addLeftClick():
    Lb.insert((Lb.size() + 1), "Left Click")
    
def addRightClick():
    Lb.insert((Lb.size() + 1), "Right Click")

def removeItem():
    Lb.delete(Lb.curselection())

def getPosition():
    xPos.delete(0,END)
    xPos.insert(0,win32api.GetCursorPos()[0])
    yPos.delete(0,END)
    yPos.insert(0,win32api.GetCursorPos()[1])

def about():
    win32api.MessageBox(0, 'Made with ♥ and ☕ by fkhrrz@1rdaystudio.com', 'About')

def hotkeyWindow():
    win32api.MessageBox(0, 'Made with ♥ and ☕ by fkhrrz@1rdaystudio.com', 'About')

def run():
    global runFlag
    if runFlag:
        runFlag = False
    else:
        runFlag = True
# End Function Section

app = Tk()
app.resizable(0,0)

# App Title
app.title("iMouse")

# Toolbar
toolbar = Menu(app)
app.config(menu=toolbar)
toolbarFile = Menu(toolbar, tearoff=0)
toolbarFile.add_command(label='Import')
toolbarFile.add_command(label='Export')
toolbarFile.add_separator()
toolbarFile.add_command(label='Exit', command=app.destroy)
toolbar.add_cascade(label='File', menu=toolbarFile)
toolbar.add_cascade(label='Hotkey', command=hotkeyWindow)
toolbar.add_cascade(label='About', command=about)

# Command List
Lb = Listbox(app, width=30)
Lb.grid(row=0, column=0, rowspan=5)

# X Position
Label(app, text='X Pos', width=15).grid(row=0, column=1, pady=1)
xSV = StringVar()
xSV.trace("w", lambda name, index, mode, xSV=xSV: checkEntry('x',xSV))
xPos = Entry(app, width=15, textvariable=xSV)
xPos.grid(row=1, column=1)
# Y Position
Label(app, text='Y Pos', width=15).grid(row=0, column=2, pady=1)
yPos = Entry(app, width=15)
yPos.grid(row=1, column=2)

# Button Add Click Command
btnAddPosition = Button(app, text='Add Position', width=30, command=addPosition).grid(row=2, column=1, columnspan=2, padx=5)
btnAddLeftClick = Button(app, text='Add Left Click', width=15, command=addLeftClick).grid(row=3, column=1, padx=5)
btnAddRightClick = Button(app, text='Add Right Click', width=15, command=addRightClick).grid(row=3, column=2, padx=5)
btnRemove = Button(app, text='Remove', width=30, command=removeItem).grid(row=4, column=1, columnspan=2, padx=5)
btnStart = Button(app, text='Start', width=30, command=run).grid(row=5, column=1, columnspan=2, padx=5, pady=5)

def isKeyPressed(key):
    return (win32api.GetKeyState(key) & (1 << 7)) != 0

wasKeyPressedTheLastTimeWeChecked = False
while True:
    keyT = isKeyPressed(ord('T'))
    if keyT and not isKeyT:
        getPosition()
    isKeyT = keyT
    
    keyQ = isKeyPressed(ord('Q'))
    if keyQ and not isKeyQ:
        run()
    isKeyQ = keyQ

    if runFlag:
        iMouse()

    app.update_idletasks()
    app.update()
    time.sleep(0.01)