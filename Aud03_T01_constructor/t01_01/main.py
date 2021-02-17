

from quadratic_equation import QuadraticEquation


if __name__ == '__main__':
    file = "input03.txt"
    with open(file) as f:
        eqs_0 = []
        eqs_1 = []
        eqs_2 = []
        eqs_inf = []

        for line in f:
            try:
                a, b, c = map(int, line.split())
                eq = QuadraticEquation(a, b, c)
                solutions = eq.solve()
                if solutions == QuadraticEquation.INF:
                    eqs_inf.append(eq)
                elif len(solutions) == 0:
                    eqs_0.append(eq)
                elif len(solutions) == 1:
                    eqs_1.append(eq)
                else:
                    eqs_2.append(eq)
            except ValueError:
                pass

        print("Solutions 0:")
        for equation in eqs_0:
            equation.show()
        print("=====")
        print("Solutions 1:")
        for equation in eqs_1:
            equation.show()
        print("=====")
        print("Solutions 2:")
        for equation in eqs_2:
            equation.show()
        print("=====")
        print("Solutions inf:")
        for equation in eqs_inf:
            equation.show()

        if eqs_1:
            minsol = float("inf")
            min_eq = None
            maxsol = float("-inf")
            max_eq = None
            for equation in eqs_1:
                solution = equation.solve()[0]
                if solution < minsol:
                    minsol = solution
                    min_eq = equation
                if solution > maxsol:
                    maxsol = solution
                    max_eq = equation

            print("Рівняння з найменшим розв'язком: ")
            min_eq.show()
            print(minsol)
            print("Рівняння з найбільшим розв'язком: ")
            max_eq.show()
            print(maxsol)
        else:
            print("Немає рівнянь з одним розв'язком")
