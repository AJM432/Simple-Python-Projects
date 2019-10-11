from tkinter import *

win = Tk()
win.geometry('300x300')

# ---FUNCTIONS---
def printname(event):
    print('Hello, Alvin')


# ! do not add brackets to call a function when using 'command' parameter
button1 = Button(win, text='print') # * 'command' gives the element access to a function
button1.pack()

# ! Put event '<Button-1>' in between greater and less than signs
button1.bind('<Button-1>', printname) # * 'Button-1 is the code name for a left mouse click'

win.mainloop()