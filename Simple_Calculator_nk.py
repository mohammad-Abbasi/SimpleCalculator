from tkinter import *


def insert(character):
    def g():
        display.insert(END, character)

    return g


def calc():
    res = eval(display.get())
    display.delete(0, END)
    display.insert(0, res)


root = Tk()

layout = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '+']
]

config = {'width': 5, 'height': 2, 'bd': 0}
display = Entry()
display.grid(row=0, column=0, columnspan=4, sticky=W + E)
for i, row in enumerate(layout):
    for j, item in enumerate(row):
        Button(text=item, command=insert(item) if item != '=' else calc, **config).grid(row=i + 1, column=j)

root.mainloop()
