import tkinter
from tkinter import *


def createWindow():
    global window
    window = Tk()
    window.geometry("800x500")

def doInput():
    global inputbox
    global inputtext
    inputbox = Entry(window, bd = 5)
    inputbox.pack(side = LEFT)
    inputbox.place(x=20, y=30)
    inputtext = inputbox.get()

def doButton():
    global button1
    button1 = Button(window, text = "Execute", command = doCommand)

def mainLoop():
    window.mainloop()

if __name__ == "__main__":
    createWindow()
    doInput()
    doButton()
    
    mainLoop()
    