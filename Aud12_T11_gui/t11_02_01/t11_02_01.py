

from tkinter import *
root = Tk()


def is_palindrome(string):
    return string == string[::-1]


entry = Entry(root, font="Arial 14")
entry.pack()


label = Label(root, text="Введіть рядок", font="Arial 14")
label.pack()


def check():
    string = entry.get()
    if is_palindrome(string):
        label["text"] = string + " - це паліндром"
    else:
        label["text"] = string + " - це не паліндром"


btn = Button(root, text="Перевірити",
             width=30, height=5,
             bg="white", fg="black", font="Arial 14",
             command=check)
btn.pack()

root.mainloop()
