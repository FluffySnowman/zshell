import tkinter
from tkinter import *
import os

####################
#IMPORTANT FUNCTIONS
####################
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def createWindow():
    global window
    window = Tk()
    window.geometry("800x500")

def doInput():
    global inputbox
    global inputtext
    inputbox = Entry(window, bd = 4)
    inputbox.pack(side = LEFT)
    inputbox.place(x=20, y=30)

def doButton():
    global button1
    button1 = Button(window, text = "Execute", 
                         command = combine_funcs(doCommand, doText))
    button1.place(x = 170, y = 30)

def doCommand():
    global output

    inputtext = inputbox.get()

    stream = os.popen(inputtext)
    output = stream.read()
    print(output)

def doText():
    print("text command has been commanded or whatever")

def mainLoop():
    window.mainloop()

if __name__ == "__main__":
    createWindow()
    doInput()
    doButton()
    doCommand()
    mainLoop()
    