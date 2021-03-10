

from t1 import *
import random


MAX_X = 400
MAX_Y = 400


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:0>2X}{:0>2X}{:0>2X}".format(r, g, b)


if __name__ == '__main__':
    home()
    speed(10)
    delay(10)
    pensize(5)

    Figs = (Circle, Quadrate, Triangle, Trapezoid, Rectangle, Cross)
    for i in range(100):
        Fig = random.choice(Figs)
        x = random.randint(-MAX_X, MAX_X)
        y = random.randint(-MAX_Y, MAX_Y)
        a = random.randint(1, MAX_X // 4)
        color = get_random_color()
        if Fig in (Trapezoid, Rectangle):
            b = random.randint(1, MAX_X // 4)
            fig = Fig(x, y, a, b, color)
        else:
            fig = Fig(x, y, a, color)

        fig.show()



    mainloop()
