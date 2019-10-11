import tkinter as tk
import random

#  *---Main Window---*
win = tk.Tk()
win.title("Login System")
win.geometry("400x400") # window size

# *---Label---*
user = tk.Label(text="Enter your Username: ") # this is LABEL and can be used in any way
user.grid(column=0, row=0) # aranges elements into grid structure (column, row)
pword = tk.Label(text="Enter your Password: ")
pword.grid(column=0, row=1)

# *---Button---*
# ! 'bg' command does not work, use highlightbackgroudn to color an element
# ? command allows you to give the button access to the function "phrase"

button1 = tk.Button(text="Click this button", highlightbackground="grey", command=win)
button1.grid(column=1, row=2)


# *---Entry Field---*
entry1 = tk.Entry()
entry1.grid(column=1, row=1)
# Runs the window as loop
win.mainloop()
