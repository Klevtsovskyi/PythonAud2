"""
У текстовому файлі записана непорожня послідовність дійсних
чисел, які розділяються пропусками. Визначити функції для
обчислення:
a) суми компонент файла;
b) кількості від’ємних компонент файла;
c) останньої компоненти файла;
d) найбільшого із значень компонент файла;
e) найменшого із значень компонент файла з парними номерами;
f) суми найбільшого і найменшого із значень компонент;
g) різниці першої й останньої компоненти файла;
h) кількості компонент файла, які менші за середнє
арифметичне всіх його компонент.
"""

FILE = "t13_02.txt"


def read_numbers(filename):
    with open(filename) as f:
        numbers = [float(s) for s in f.read().split()]
    return numbers


def a(filename):
    numbers = read_numbers(filename)
    return sum(numbers)


def b(filename):
    numbers = read_numbers(filename)
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count


def c(filename):
    numbers = read_numbers(filename)
    return numbers[-1]


def d(filename):
    numbers = read_numbers(filename)
    return max(numbers)


def e(filename):
    numbers = read_numbers(filename)
    return min(numbers[::2])


def f(filename):
    numbers = read_numbers(filename)
    return min(numbers) + max(numbers)


def g(filename):
    numbers = read_numbers(filename)
    return numbers[0] - numbers[-1]


def h(filename):
    numbers = read_numbers(filename)
    avg = sum(numbers) / len(numbers)
    count = 0
    for number in numbers:
        if number < avg:
            count +=1
    return count


if __name__ == '__main__':
    print(read_numbers(FILE))
    print("a: ", a(FILE))
    print("b: ", b(FILE))
    print("c: ", c(FILE))
    print("d: ", d(FILE))
    print("e: ", e(FILE))
    print("f: ", f(FILE))
    print("g: ", g(FILE))
    print("h: ", h(FILE))
