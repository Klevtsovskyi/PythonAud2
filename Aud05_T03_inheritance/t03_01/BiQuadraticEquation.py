

from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):
    """ a x^4 + b x^2 + c = 0"""

    def solve(self):
        # y = x^2 -> a y^2 + b y + c = 0 -> y1, y2
        # x^2 - y1 = 0, x^2 - y2 = 0
        solutions_y = super().solve()
        if solutions_y == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        else:
            result = set()
            for y in solutions_y:
                eq = QuadraticEquation(1, 0, -y)
                solutions_x = eq.solve()
                for x in solutions_x:
                    result.add(x)
            return result

    def __str__(self):
        return "{} x^4 + {} x^2 + {} = 0".format(self._a, self._b, self._c)


if __name__ == '__main__':
    eq = BiQuadraticEquation(1, -3, 2)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(1, -3, 0)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(1, 0, 0)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(1, -8, -9)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(1, 1, 1)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(1, -2, 1)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(0, 1, 2)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(0, 0, 2)
    eq.show()
    print(eq.solve())

    eq = BiQuadraticEquation(0, 0, 0)
    eq.show()
    print(eq.solve())
