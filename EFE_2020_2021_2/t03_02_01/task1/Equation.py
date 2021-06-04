

class Equation:
    """ b x + c = 0"""

    INF = "inf"

    def __init__(self, b, c):
        self._b = b
        self._c = c

    def __str__(self):
        return "{} x + {}".format(self._b, self._c)

    def show(self):
        print(self)

    def solve(self):
        # 0 x + c = 0
        if self._b == 0:
            # 0 x + 0 = 0
            if self._c == 0:
                return Equation.INF
            # 0 x + c = 0
            else:
                return set()
        # b x + c = 0
        else:
            return {-self._c / self._b}


if __name__ == '__main__':
    eq1 = Equation(1, 1)
    eq1.show()
    print(eq1.solve())

    eq2 = Equation(1, 0)
    eq2.show()
    print(eq2.solve())

    eq3 = Equation(0, 0)
    eq3.show()
    print(eq3.solve())

    eq4 = Equation(0, 1)
    eq4.show()
    print(eq4.solve())
