from tkinter import *

win = Tk()

def leftClick(event):
    print('Left')

def middleClick(event):
    print('Middle')

def rightClick(event):
    print('Right')


button = Button(win, text='Click the button', width=20, height=5)
button.pack()
button.bind('<Button-1>' ,leftClick)
button.bind('<Button-3>', middleClick)
button.bind('<Button-2>', rightClick)



win.mainloop()
