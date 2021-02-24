

from turtle import *


class Triangle:

    _count = 0

    @staticmethod
    def get_count():
        return Triangle._count

    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

        self._outline = "black"
        self._fillcolor = None
        self._thickness = 1

        Triangle._count += 1

    def set_outline(self, color):
        self._outline = color

    def set_fillcolor(self, color):
        self._fillcolor = color

    def set_thickness(self, thickness):
        self._thickness = thickness

    def draw(self):
        oldcolor = pencolor()
        oldfillcolor = fillcolor()
        oldsize = pensize()

        pencolor(self._outline)
        if self._fillcolor:
            fillcolor(self._fillcolor)
        pensize(self._thickness)

        up()
        goto(self._p1)
        down()
        if self._fillcolor:
            begin_fill()
        goto(self._p2)
        goto(self._p3)
        goto(self._p1)
        if self._fillcolor:
            end_fill()
        up()

        pencolor(oldcolor)
        fillcolor(oldfillcolor)
        pensize(oldsize)


if __name__ == '__main__':
    home()

    p1 = (200, 0)
    p2 = (0, 100)
    p3 = (100, 100)
    t = Triangle(p1, p2, p3)

    t.set_outline("red")
    t.set_thickness(5)
    t.set_fillcolor("green")

    t.draw()

    mainloop()
