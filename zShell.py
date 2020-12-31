import tkinter
from tkinter import *
import os
#os.chdir(os.path.abspath(os.path.expanduser('~')))
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
def createWindow():
    global window
    window = Tk()
    window.title("zShell")
    window['bg'] = 'black'
    window.geometry("800x500")
def doInput():
    global inputbox
    global inputtext
    inputbox = Entry(window, bd = 4)
    inputbox.pack(side = LEFT)
    inputbox.place(x=20, y=30, height = 30, width = 400)
    inputbox.bind('<Return>', doButton)
def doButton():
    global button1
    button1 = Button(window, text = "Execute", 
                         command = combine_funcs(doCommand, doText))
    button1.place(x = 430, y = 30)
def doCommand():
    global output
    inputtext = inputbox.get()
    stream = os.popen(inputtext)
    output = stream.read()
    print(output)
def doText():
    global textbox
    textbox = Text(window)
    textbox.place(x = 30, y = 70)
    textbox.config(fg="green", bg="black")
    textbox.insert(INSERT, output)
def pressEnter(event):
    doCommand()
    doText()
def mainLoop():
    window.mainloop()
if __name__ == "__main__":
    createWindow()
    doInput()
    window.bind('<Return>', pressEnter)
    doButton()
    mainLoop()