"""
Дано текстовий файл, що містить принаймні один непорожній
рядок. Описати підпрограми:
a) виведення усіх рядків файла;
b) виведення рядків, які містять більше 60 символів;
c) підрахунку кількості порожніх рядків;
d) пошуку найдовшого рядка;
"""

FILE = "t13_01.txt"


def a(filename):
    f = open(filename, encoding="utf-8")
    data = f.read()
    print(data)
    f.close()


def b(filename):
    f = open(filename, encoding="utf-8")
    for line in f:
        lst = line.split()
        count = 0
        for word in lst:
            count += len(word)
        if count >= 60:
            print(line)
    f.close()


def c(filename):
    f = open(filename, encoding="utf-8")
    count = 0
    for line in f.readlines():
        if line == "\n":
            count += 1
    print(count)
    f.close()


def d(filename):
    f = open(filename, encoding="utf-8")
    max_line = ""
    line = f.readline()
    while line:
        if len(line) > len(max_line):
            max_line = line
        line = f.readline()
    print(max_line)
    f.close()


if __name__ == '__main__':
    d(FILE)
