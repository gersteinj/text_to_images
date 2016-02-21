import tkinter
import tkinter.colorchooser

root = tkinter.Tk(className="GuiTest")      # Creates root window
title = tkinter.Label(root, text="Text to Images", font=("Helvetica", 18))
title.pack()
dirs = tkinter.Message(root, text="Choose your settings, then choose your file. When you're ready, click the \"Process\" button.", width = 600)
dirs.pack()


def getColor():
    global textColor
    color = tkinter.colorchooser.askcolor()
    print(color)
    return color

tkinter.Button(text='Select Color', command=getColor).pack()
tkinter.mainloop()
