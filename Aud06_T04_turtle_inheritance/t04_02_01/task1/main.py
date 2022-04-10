from Figures import *
from turtle import *
import random


if __name__ == "__main__":
    home()
    delay(1)
    speed(10)
    width(3)

    Figs = (Circle, Triangle, Trapezoid, Rectangle, Quadrate)
    for _ in range(100):
        Fig = random.choice(Figs)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        a = random.randint(30, 100)
        clr = "#{:0>2x}{:0>2x}{:0>2x}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        if Fig in (Trapezoid, Rectangle):
            b = random.randint(30, 50)
            fig = Fig(x, y, a, b, clr)
        else:
            fig = Fig(x, y, a, clr)

        fig.show()

    mainloop()
