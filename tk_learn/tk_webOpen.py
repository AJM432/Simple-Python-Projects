
from tkinter import *
import webbrowser as wb

win = Tk()
win.title('Bookmarks')

def reddit(event):
    wb.open('https://www.reddit.com')

def learn(event):
    wb.open('https://learn-anything.xyz/')

#//blank1 = Label(win, width=10, height=2)
clickR = Button(win, text='Reddit', fg='red')
clickL = Button(win, text='Learn', fg='blue', highlightbackground='black')
clickR.config(width=10, height=2)
clickL.config(width=10, height=2)

#//blank1.grid()
clickR.grid(row=1, column=1)
clickL.grid(row=1, column=2)

#//clickR.grid(column= 0, row = 0)
#//clickL.grid(column=0, row=1, sticky=E)

clickR.bind('<Button-1>', reddit)
clickL.bind('<Button-1>', learn)


win.mainloop()



