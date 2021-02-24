

from turtle import *
from Triangle import Triangle
import random


MAX_X = 400
MAX_Y = 400

COLORS = ["black", "red", "blue", "#00FF00", "#667788"]


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:0>2X}{:0>2X}{:0>2X}".format(r, g, b)


if __name__ == '__main__':
    home()

    speed(10)
    delay(10)

    while Triangle.get_count() != 100:
        p1 = (random.randint(-MAX_X, MAX_X), random.randint(-MAX_Y, MAX_Y))
        p2 = (random.randint(-MAX_X, MAX_X), random.randint(-MAX_Y, MAX_Y))
        p3 = (random.randint(-MAX_X, MAX_X), random.randint(-MAX_Y, MAX_Y))
        t = Triangle(p1, p2, p3)

        t.set_thickness(random.randint(1, 10))
        t.set_fillcolor(get_random_color())
        t.set_outline(get_random_color())
        # t.set_fillcolor(random.choice(COLORS))
        # t.set_outline(random.choice(COLORS))

        t.draw()

    mainloop()
