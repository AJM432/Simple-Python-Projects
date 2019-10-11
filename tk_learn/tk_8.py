from tkinter import *


class buttons:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text='print msg', command=self.print_msg)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text='QUIT', command=win.destroy)
        self.quit_button.pack(side=LEFT)


    def print_msg(self):
        print('Hello World')


win = Tk()

b = buttons(win)

win.mainloop()