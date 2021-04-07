

def fun(n):
    a0 = 1
    a1 = 1
    a2 = 3
    p = 1
    t = 4
    r = 1
    for i in range(n + 1):
        p *= a0 / r
        r *= 3
        a0, a1, a2 = a1, a2, a0 + a1 / t
        t *= 2
    return p


def gen():
    a0 = 1
    a1 = 1
    a2 = 3
    p = 1
    t = 4
    r = 1
    while True:
        p *= a0 / r
        yield p
        r *= 3
        a0, a1, a2 = a1, a2, a0 + a1 / t
        t *= 2


if __name__ == '__main__':
    n = 3
    i = 0
    for rez in gen():
        print(rez)
        i += 1
        if i > n:
            break
