
# a_0 = 1
# a = a_i / a_(i-1) = x / i
def fun(x, n):
    a = 1
    for i in range(1, n + 1):
        a *= x / i
    return a


def gen(x):
    a = 1
    i = 0
    while True:
        yield a
        i += 1
        a *= x / i


if __name__ == '__main__':
    x = 13
    n = 2
    j = 0
    for rez in gen(x):
        print(rez)
        j += 1
        if j > n:
            break
