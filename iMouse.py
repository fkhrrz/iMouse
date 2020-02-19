from tkinter import *
from uuid import getnode as get_mac
from msvcrt import getch
import re
import time
import win32api, win32con

runFlag = False
hotkeyStart = 48
hotkeyStop = 49

# Begin Function Section
def iMouse():
    if Lb.size() > 0:
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
    win32api.MessageBox(0, "Made with ♥ and ☕ by fkhrrz@1rdaystudio.com", "About")

def hotkeyWindow():
    showHotkey = True

    hotkeyUI = Toplevel(app)
    hotkeyUI.resizable(0,0)
    hotkeyUI.title("Hotkey")

    Label(hotkeyUI, text="Start", width=15).grid(row=0, column=0, padx=1, pady=1)
    startSV = StringVar()
    startSV.trace("w", lambda name, index, mode, startSV=startSV: hotkeyEntry(1,'start',startSV))
    startEntry = Entry(hotkeyUI, width=15, textvariable=startSV).grid(row=0, column=1, padx=1, pady=1)

    Label(hotkeyUI, text="Stop", width=15).grid(row=0, column=0, padx=1, pady=1)
    stopSV = StringVar()
    stopSV.trace("w", lambda name, index, mode, stopSV=stopSV: hotkeyEntry(1,'stop',stopSV))
    stopEntry = Entry(hotkeyUI, width=15, textvariable=stopSV).grid(row=0, column=1, padx=1, pady=1)

    def closeHotkey():
        showHotkey = False
        hotkeyUI.destroy()

    while showHotkey:
        hotkeyUI.protocol("WM_DELETE_WINDOW", closeHotkey)
        hotkeyUI.update_idletasks()
        hotkeyUI.update()
        time.sleep(0.01)

def run():
    global runFlag
    if runFlag:
        runFlag = False
    else:
        runFlag = True
        
def hotkeyEntry(max,target,val):
    if re.search("[0-9]", val.get()):
        illegalChar = re.compile("[0-9]")
        illegalPos = int
        for m in illegalChar.finditer(val.get()):
            illegalPos = m.start()
        if len(val.get()) > max:
            target.delete(max, END)
        else:
            if target == 'start':
                hotkeyStart.delete(illegalPos, illegalPos+1)
            elif target == 'stop':
                hotkeyStop.delete(illegalPos, illegalPos+1)
# End Function Section

app = Tk()
app.resizable(0,0)

# App Title
app.title("iMouse")

# Toolbar
toolbar = Menu(app)
app.config(menu=toolbar)
toolbarFile = Menu(toolbar, tearoff=0)
toolbarFile.add_command(label="Import")
toolbarFile.add_command(label="Export")
toolbarFile.add_separator()
toolbarFile.add_command(label="Exit", command=app.destroy)
toolbar.add_cascade(label="File", menu=toolbarFile)
toolbar.add_cascade(label="Hotkey", command=hotkeyWindow)
toolbar.add_cascade(label="About", command=about)

# Command List
Lb = Listbox(app, width=30)
Lb.grid(row=0, column=0, rowspan=5)

# X Position
Label(app, text="X Pos", width=15).grid(row=0, column=1, pady=1)
xSV = StringVar()
xSV.trace("w", lambda name, index, mode, xSV=xSV: checkEntry('x',xSV))
xPos = Entry(app, width=15, textvariable=xSV).grid(row=1, column=1)
# Y Position
Label(app, text="Y Pos", width=15).grid(row=0, column=2, pady=1)
ySV = StringVar()
ySV.trace("w", lambda name, index, mode, ySV=ySV: checkEntry('y',ySV))
yPos = Entry(app, width=15, textvariable=ySV).grid(row=1, column=2)

# Button Add Click Command
btnAddPosition = Button(app, text="Add Position", width=30, command=addPosition).grid(row=2, column=1, columnspan=2, padx=5)
btnAddLeftClick = Button(app, text="Add Left Click", width=15, command=addLeftClick).grid(row=3, column=1, padx=5)
btnAddRightClick = Button(app, text="Add Right Click", width=15, command=addRightClick).grid(row=3, column=2, padx=5)
btnRemove = Button(app, text="Remove", width=30, command=removeItem).grid(row=4, column=1, columnspan=2, padx=5)
btnStart = Button(app, text="Start", width=30, command=run).grid(row=5, column=1, columnspan=2, padx=5, pady=5)

while True:
    if win32api.GetAsyncKeyState(ord('T')):
        getPosition()
    
    if win32api.GetAsyncKeyState(win32con.VK_F1):
        run()

    if runFlag:
        iMouse()

    app.update_idletasks()
    app.update()
    time.sleep(0.01)