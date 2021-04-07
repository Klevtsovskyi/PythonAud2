
import math


# s(n) - s(n-1) = a(n)
def fun(x, eps):
    s = 1
    a = 1
    i = 0
    while abs(a) >= eps:
        i += 1
        a *= x / i
        s += a
    return s


def gen(x):
    s = 1
    a = 1
    i = 0
    while True:
        yield s, a
        i += 1
        a *= x / i
        s += a


if __name__ == '__main__':
    x = 2
    eps = 0.00001
    for rez, a in gen(x):
        print(rez)
        if abs(a) < eps:
            break

    print("----")
    print(math.exp(x))
