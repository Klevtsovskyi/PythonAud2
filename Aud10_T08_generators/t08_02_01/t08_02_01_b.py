
# s_1 = 1
# s_i - s_(i-1) = 1 / i
def fun(n):
    s = 1
    for i in range(2, n + 1):
        s += 1 / i
    return s


def gen():
    s = 1
    i = 1
    while True:
        yield s
        i += 1
        s += 1 / i


if __name__ == '__main__':
    n = 10
    j = 1
    for rez in gen():
        print(rez)
        j += 1
        if j > n:
            break
