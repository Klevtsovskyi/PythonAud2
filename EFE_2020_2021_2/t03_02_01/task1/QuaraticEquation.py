

from Equation import Equation


class QuadraticEquation(Equation):
    """ a x^2 + b x + c = 0"""

    def __init__(self, a, b, c):
        super().__init__(b, c)
        self._a = a

    def __str__(self):
        return "{} x^2 + ".format(self._a) + super().__str__()

    def dis(self):
        return self._b ** 2 - 4 * self._a * self._c

    def solve(self):
        # 0 x^2 + b x + c = 0
        if self._a == 0:
            return super().solve()
        # a x^2 + b x + c = 0
        else:
            d = self.dis()
            if d < 0:
                return set()
            else:
                x1 = (-self._b - d ** 0.5) / (2 * self._a)
                x2 = (-self._b + d ** 0.5) / (2 * self._a)
                return {x1, x2}


if __name__ == '__main__':
    eq1 = QuadraticEquation(0, 1, 1)
    eq1.show()
    print(eq1.solve())

    eq2 = QuadraticEquation(0, 1, 0)
    eq2.show()
    print(eq2.solve())

    eq3 = QuadraticEquation(0, 0, 0)
    eq3.show()
    print(eq3.solve())

    eq4 = QuadraticEquation(0, 0, 1)
    eq4.show()
    print(eq4.solve())

    eq5 = QuadraticEquation(1, 1, 1)
    eq5.show()
    print(eq5.solve())

    eq6 = QuadraticEquation(1, -2, 1)
    eq6.show()
    print(eq6.solve())

    eq7 = QuadraticEquation(1, -4, 2)
    eq7.show()
    print(eq7.solve())
