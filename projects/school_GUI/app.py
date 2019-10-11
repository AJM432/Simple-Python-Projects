import tkinter as tk

#---Window Config---
win = tk.Tk()
win.geometry('400x400')
win.title('test')


#---Labels---
sub1 = tk.Label(text="Subject 1: ", bg='grey')
sub1.grid(column=0, row=0)

sub2 = tk.Label(text="Subject 2: ", bg='grey')
sub2.grid(column=0, row=1)

sub3 = tk.Label(text="Subject 3: ", bg='grey')
sub3.grid(column=0, row=2)

sub4 = tk.Label(text="Subject 4: ", bg='grey')
sub4.grid(column=0, row=3)

#









#---Run App---
win.mainloop()