
from tkinter import *

def log():
    user = Entry(win, text='User')
    password = Entry(win, text='Password')
    user.pack()
    password.pack()

def test(event):
    print('hi')

win = Tk()
win.title('Login')
win.geometry('400x400')


login = Button(win, text='Login', bg='lightgrey')
login.bind("<Button-1>", log)
login.grid(column=2, row=3)

win.mainloop()

'''
db = {
    'Alvin': 'Forget4',

    'Alan': 'test'
}

user = input('Enter Username: ')
password = input('Enter password: ')

if user in db:
    print('yes')
    if password in db:
        print('yes pass')

else:
    print('no')

'''