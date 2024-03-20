from tkinter import *




def button_click(char):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(char))

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('//', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = Button(root, text=text, padx=40, pady=20,
                    command=lambda t=text: button_click(t))
    button.grid(row=row, column=column)

clear_button = Button(root, text='Clear', padx=77, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

equal_button = Button(root, text='Calculate', padx=68, pady=20, command=equal)
equal_button.grid(row=5, column=2, columnspan=2)

root.mainloop()