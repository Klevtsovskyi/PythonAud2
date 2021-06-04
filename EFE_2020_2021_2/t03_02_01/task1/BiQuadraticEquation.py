

from QuaraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):
    """ a x^4 + b x^2 + c = 0"""

    def __str__(self):
        return "{} x^4 + {} x^2 + {} = 0".format(self._a, self._b, self._c)

    def solve(self):
        # y = x^2
        # a y^2 + b y + c = 0 -> y1, y2
        # x^2 = y1, x^2 = y2
        sols = super().solve()
        if sols == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        elif len(sols) == 0:
            return set()
        elif len(sols) == 1:
            y1 = sols.pop()
            eq = QuadraticEquation(1, 0, -y1)
            return eq.solve()
        else:
            y1 = sols.pop()
            eq = QuadraticEquation(1, 0, -y1)
            result = eq.solve()
            y2 = sols.pop()
            eq = QuadraticEquation(1, 0, -y2)
            for x in eq.solve():
                result.add(x)
            return result


if __name__ == '__main__':
    eq1 = BiQuadraticEquation(0, 1, 1)
    eq1.show()
    print(eq1.solve())

    eq2 = BiQuadraticEquation(0, 1, 0)
    eq2.show()
    print(eq2.solve())

    eq3 = BiQuadraticEquation(0, 0, 0)
    eq3.show()
    print(eq3.solve())

    eq4 = BiQuadraticEquation(0, 0, 1)
    eq4.show()
    print(eq4.solve())

    eq5 = BiQuadraticEquation(1, 1, 1)
    eq5.show()
    print(eq5.solve())

    eq6 = BiQuadraticEquation(1, -2, 1)
    eq6.show()
    print(eq6.solve())

    eq7 = BiQuadraticEquation(1, -4, 2)
    eq7.show()
    print(eq7.solve())
