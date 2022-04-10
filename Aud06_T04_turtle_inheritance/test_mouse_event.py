

from t1 import *


def f(x, y):
    onscreenclick(None)
    c = Cross(x, y, 50, "red")
    c.show()
    onscreenclick(f)


if __name__ == '__main__':
    home()
    pensize(5)
    listen()

    onscreenclick(f)

    mainloop()