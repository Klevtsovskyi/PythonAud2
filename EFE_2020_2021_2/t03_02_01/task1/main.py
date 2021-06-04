

from Equation import Equation
from QuaraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation


if __name__ == '__main__':
    filename = "input03.txt"
    equations = {0: [], 1: [], 2: [], 3: [], 4: [], Equation.INF: []}
    with open(filename) as f:
        for line in f:
            coefs = [int(n) for n in line.split()]
            if len(coefs) == 2:
                eq = Equation(coefs[0], coefs[1])
            elif len(coefs) == 3:
                eq = QuadraticEquation(coefs[0], coefs[1], coefs[2])
            else:
                eq = BiQuadraticEquation(coefs[0], coefs[2], coefs[4])
            sols = eq.solve()
            count = len(sols)
            equations[count].append(eq)
        for count in equations:
            print(count)
            print("=================")
            for eq in equations[count]:
                print(eq)
            print("=================")
            print("=================")

        min_sol = float("inf")
        max_sol = -float("inf")
        min_eq = None
        max_eq = None
        for eq in equations[1]:
            sol = eq.solve().pop()
            if sol < min_sol:
                min_sol = sol
                min_eq = eq
            if sol > max_sol:
                max_sol = sol
                max_eq = eq
        print("min: ", min_eq, "; ", min_sol)
        print("max: ", max_eq, "; ", max_sol)
