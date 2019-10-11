from tkinter import *

# ---RUN---
win = Tk()
win.title('Tk_4')

# ---ELEMENTS---
label1 = Label(win, text='Name')
label2 = Label(win, text='Password')

entry1 = Entry(win)
entry2 = Entry(win)

check1 = Checkbutton(win, text='Keep me logged in') # * 'Checkbutton' creates a checkbox

# ---POSITION---
label1.grid(row=0, sticky='E') # * 'sticky' lets you choose the direction [N, S, E, W]
label2.grid(row=1, sticky='E')

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

check1.grid(columnspan=2) # * 'columnspan' lets the element take up 2 column spaces


win.mainloop()