"""
Описати підпрограму, яка утворює текстовий файл із 9 рядків, у
першому з яких одна літера '1', у другому – дві літери '2', ... , у
дев’ятому – дев’ять літер '9'.
"""

FILE = "t13_03.txt"


def pyramid(filename):
    f = open(filename, "w")
    for i in range(1, 10):
        f.write(str(i) * i + "\n")
    f.close()


if __name__ == '__main__':
    pyramid(FILE)
