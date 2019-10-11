#!/usr/bin/env python3.7.2
from tkinter import *

win = Tk()
win.title('Calculator')
#//win.geometry('400x400')

# ---ELEMENTS---
click1 = Button(win, text='1', width=9, height=4, highlightbackground='orange')
click2 = Button(win, text='2', width=9, height=4, highlightbackground='orange')
click3 = Button(win, text='3', width=9, height=4, highlightbackground='orange')
click4 = Button(win, text='4', width=9, height=4, highlightbackground='orange')
click5 = Button(win, text='5', width=9, height=4, highlightbackground='orange')
click6 = Button(win, text='6', width=9, height=4, highlightbackground='orange')
click7 = Button(win, text='7', width=9, height=4, highlightbackground='orange')
click8 = Button(win, text='8', width=9, height=4, highlightbackground='orange')
click9 = Button(win, text='9', width=9, height=4, highlightbackground='orange')
click0 = Button(win, text='0', width=9, height=4, highlightbackground='orange')
lcd = Label(win, height=3, text='Numbers will apear here')

# ---POSTION---
lcd.grid(columnspan=3)
click1.grid(column=0,row=2)
click2.grid(column=1, row=2)
click3.grid(column=2, row=2)
click4.grid(column=0, row=3)
click5.grid(column=1, row=3)
click6.grid(column=2, row=3)
click7.grid(column=0, row=4)
click8.grid(column=1, row=4)
click9.grid(column=2, row=4)
click0.grid(column=1, row=5)


win.mainloop()