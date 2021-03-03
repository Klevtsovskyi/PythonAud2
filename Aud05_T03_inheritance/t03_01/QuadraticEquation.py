

from Equation import Equation


class QuadraticEquation(Equation):
    """ a x^2 + b x + c = 0"""

    def __init__(self, a, b, c):
        super().__init__(b, c)
        self._a = a

    def solve(self):
        if self._a == 0:
            return super().solve()
        else:
            d = self.get_dis()
            if d < 0:
                return set()
            elif d == 0:
                return {-self._b / (2 * self._a)}
            else:
                d2 = d**0.5
                x1 = (-self._b - d2) / (2 * self._a)
                x2 = (-self._b + d2) / (2 * self._a)
                return {x1, x2}

    def get_dis(self):
        return self._b**2 - 4 * self._a * self._c

    def __str__(self):
        return "{} x^2 + ".format(self._a) + super().__str__()


if __name__ == '__main__':
    eq = QuadraticEquation(1, -8, -9)
    eq.show()
    print(eq.solve())

    eq = QuadraticEquation(1, 1, 1)
    eq.show()
    print(eq.solve())

    eq = QuadraticEquation(1, -2, 1)
    eq.show()
    print(eq.solve())

    eq = QuadraticEquation(0, 1, 2)
    eq.show()
    print(eq.solve())

    eq = QuadraticEquation(0, 0, 2)
    eq.show()
    print(eq.solve())

    eq = QuadraticEquation(0, 0, 0)
    eq.show()
    print(eq.solve())
