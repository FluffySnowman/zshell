import tkinter
from tkinter import *


def createWindow():
    global window
    window = Tk()
    window.geometry("800x500")

def mainLoop():
    window.mainloop()

if __name__ == "__main__":
    createWindow()
    mainLoop()
    