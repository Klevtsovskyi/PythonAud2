# a * x^2 + b * x + c = 0


class QuadraticEquation:

    INF = "inf"

    def __init__(self, a, b=0, c=0):
        if isinstance(a, QuadraticEquation):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = b
            self.c = c

    def show(self):
        print("{} * x^2 + {} * x + {} = 0"
              .format(self.a, self.b, self.c))

    def get_dis(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    # 0 = 0
                    return QuadraticEquation.INF
                else:
                    # c = 0
                    return ()
            else:
                # b * x + c = 0
                return (-self.c / self.b, )
        else:
            # a * x^2 + b * x + c = 0
            d = self.get_dis()
            if d < 0:
                return ()
            elif d == 0:
                x1 = -self.b / (2 * self.a)
                return (x1, )
            else:
                x1 = (-self.b - d ** 0.5) / (2 * self.a)
                x2 = (-self.b + d ** 0.5) / (2 * self.a)
            return (x1, x2)


if __name__ == '__main__':
    eq = QuadraticEquation(2, 3, 4)
    eq1 = QuadraticEquation(eq)
    eq.show()
    eq1.show()
