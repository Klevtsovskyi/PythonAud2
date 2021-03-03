

class Equation:
    """ b x + c = 0"""

    INF = "inf"

    def __init__(self, b, c):
        self._b = b
        self._c = c

    def solve(self):
        if self._b == 0:
            # 0 = 0
            if self._c == 0:
                return Equation.INF
            # c = 0
            else:
                return set()
        # b x + c = 0
        else:
            return {-self._c / self._b}

    def show(self):
        print(self)

    def __str__(self):
        return "{} x + {} = 0".format(self._b, self._c)


if __name__ == '__main__':
    eq = Equation(1, 2)
    eq.show()
    print(eq.solve())

    eq = Equation(0, 2)
    eq.show()
    print(eq.solve())

    eq = Equation(0, 0)
    eq.show()
    print(eq.solve())
