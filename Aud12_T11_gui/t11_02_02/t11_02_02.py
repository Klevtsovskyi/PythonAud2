

from tkinter import *


class DifferentWords:

    def __init__(self):
        self.top = Tk()
        self.string = StringVar()
        self._make_widgets()

    def _make_widgets(self):
        Label(
            self.top, text="Введіть рядок", width=40, height=4,
            font="Arial 14"
        ).pack()
        entry = Entry(self.top, font="Arial 14", textvariable=self.string)
        entry.pack(fill=X)
        entry.bind("<Return>", self.on_button_press)
        entry.focus_set()
        Button(
            self.top, text="Вивести різні слова", font="Arial 14",
            command=self.on_button_press
        ).pack()
        self.listbox = Listbox(self.top, font="Arial 14")
        self.listbox.pack(fill=X)

    def on_button_press(self, ev=None):
        self.listbox.delete(0, END)
        string = self.string.get()
        words = set(string.split())
        for word in words:
            self.listbox.insert(END, word)
        self.string.set("")


if __name__ == '__main__':
    dw = DifferentWords()
    mainloop()
