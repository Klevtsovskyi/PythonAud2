

from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation


if __name__ == '__main__':
    file = "input03.txt"
    with open(file) as f:
        equations = {0: [], 1: [], 2: [], 3: [], 4: [],
                     Equation.INF: []}

        for line in f:
            try:
                coefs = list(map(int, line.split()))
                if len(coefs) == 2:
                    eq = Equation(coefs[0], coefs[1])
                elif len(coefs) == 3:
                    eq = QuadraticEquation(coefs[0], coefs[1], coefs[2])
                elif len(coefs) == 5:
                    eq = BiQuadraticEquation(coefs[0], coefs[2], coefs[4])
                solutions = eq.solve()
                if solutions == Equation.INF:
                    count = Equation.INF
                else:
                    count = len(solutions)
                equations[count].append(eq)
            except ValueError:
                pass

        print("Solutions 0:")
        for equation in equations[0]:
            equation.show()
        print("=====")
        print("Solutions 1:")
        for equation in equations[1]:
            equation.show()
        print("=====")
        print("Solutions 2:")
        for equation in equations[2]:
            equation.show()
        print("=====")
        print("Solutions 3:")
        for equation in equations[3]:
            equation.show()
        print("=====")
        print("Solutions 4:")
        for equation in equations[4]:
            equation.show()
        print("=====")
        print("Solutions inf:")
        for equation in equations[Equation.INF]:
            equation.show()

        if equations[1]:
            minsol = float("inf")
            min_eq = None
            maxsol = float("-inf")
            max_eq = None
            for equation in equations[1]:
                solution = equation.solve().pop()
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