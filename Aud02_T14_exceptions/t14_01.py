

def triangle_square(a, b, c):
    assert a + b > c and b + c > a and a + c > b, "Даного трикутника не існує"
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5


if __name__ == '__main__':
    a = 5
    b = 4
    c = 1
    s = triangle_square(a, b, c)
    print(s)
