from tkinter import *
import datetime

win = Tk()
win.title('Button Event')
win.geometry('200x200')

def ring(event):
    print('The doorbell was rung at ' + str(datetime.datetime.now()))

button1 = Button(win, text='Click for the time')
button1.pack()
button1.bind('<Button-1>', ring)

win.mainloop()