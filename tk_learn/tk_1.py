from tkinter import *

# ---Main Window---
win = Tk()
win.title('tkinter first step')
#//win.geometry('100x100') # * size of window

# ---Frame---
topFrame = Frame(win)
bottomFrame = Frame(win)
rightFrame = Frame(win)
leftFrame = Frame(win)
topFrame.pack(side=TOP) # * pack element puts stuff where there is room, side specifies where
bottomFrame.pack(side=BOTTOM)
rightFrame.pack(side=RIGHT)
leftFrame.pack(side=LEFT)

# ---Elements---
label1 = Label(master=topFrame, text='1', fg='red') # * master specifies location
button2 = Button(master=topFrame, text='2', fg='green')# * 'fg' specifies text color
entry1 = Entry(master=topFrame, text='3', fg='blue')
check1 = Checkbutton(master=leftFrame, text='checkbox', fg='purple')


# ---Add Elements To Display---
label1.pack(side=LEFT) # * pack() had param 'side', shows where to put element
button2.pack(side=LEFT)
entry1.pack(side=LEFT)
check1.pack()



# ---Run---
win.mainloop()