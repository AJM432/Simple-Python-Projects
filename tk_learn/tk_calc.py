from tkinter import *

win = Tk()
win.title('Calculator')

label_1 = Button(win, text='1', bg='lightgrey', width='10', height='5')
label_2 = Button(win, text='2', bg='lightgrey', width='10', height='5')
label_3 = Button(win, text='3', bg='lightgrey', width='10', height='5')
label_4 = Button(win, text='4', bg='lightgrey', width='10', height='5')
label_5 = Button(win, text='5', bg='lightgrey', width='10', height='5')
label_6 = Button(win, text='6', bg='lightgrey', width='10', height='5')
label_7 = Button(win, text='7', bg='lightgrey', width='10', height='5')
label_8 = Button(win, text='8', bg='lightgrey', width='10', height='5')
label_9 = Button(win, text='9', bg='lightgrey', width='10', height='5')
label_0 = Button(win, text='0', bg='lightgrey', width='10', height='5')

label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()
label_6.pack()
label_7.pack()
label_8.pack()
label_9.pack()
label_0.pack()

win.mainloop()
