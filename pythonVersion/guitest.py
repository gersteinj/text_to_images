import tkinter
import tkinter.colorchooser
backColor = (255, 255, 255)
textColor = (0, 0, 0)

root = tkinter.Tk(className="GuiTest")      # Creates root window
title = tkinter.Label(root, text="Text to Images", font=("Helvetica", 18))
title.pack()


def setBackColor():
    global backColor
    backColor = tkinter.colorchooser.askcolor()
    print(backColor)


def setTextColor():
    global textColor
    textColor = tkinter.colorchooser.askcolor()
    print(textColor)

tkinter.Button(text='Background', command=setBackColor).pack()
tkinter.Button(text='Text Color', command=setTextColor).pack()
root.mainloop()
