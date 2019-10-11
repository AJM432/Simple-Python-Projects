from tkinter import *

win = Tk()
win.title('TK_3')
win.geometry('400x400')

label1 = Label(win, text='one', bg='red', fg='black') # * 'bg' and 'fg' are backgroud and text color
label2 = Label(win, text='two', bg='green', fg='black')
label1.pack(fill=X) # * fill param allows label to grow in x or y
label2.pack(fill=Y)






win.mainloop()