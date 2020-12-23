import tkinter
from tkinter import *


def createWindow():
    global window
    window = Tk()
    window.geometry("800x500")

def doMain():
    global inputbox
    global inputtext
    inputbox = Entry(window, bd = 5)
    inputbox.pack(side = LEFT)
    inputbox.place(x=20, y=30)
    inputtext = inputbox.get()

def mainLoop():
    window.mainloop()

if __name__ == "__main__":
    createWindow()
    doMain()
    mainLoop()
    