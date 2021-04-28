

from tkinter import *

top = Tk()

canvas = Canvas(top, width=400, height=400, bg="white")
canvas.pack()

oval = canvas.create_oval(100, 100, 150, 150)


def move_up(ev): canvas.move(oval, 0, -5)
def move_down(ev): canvas.move(oval, 0, 5)
def move_left(ev): canvas.move(oval, -5, 0)
def move_right(ev): canvas.move(oval, 5, 0)


canvas.bind("<Up>", move_up)
canvas.bind("<Down>", move_down)
canvas.bind("<Left>", move_left)
canvas.bind("<Right>", move_right)

canvas.focus_set()
mainloop()
