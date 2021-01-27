"""
Нехай текстовий файл, містить елементи прямокутної матриці. При
цьому, кожен рядок матриці записується у окремому рядку файла, а
елементи рядка розділені одним або кількома символами
пропуску. Опишіть підпрограми:
a) зчитування матриці з файлу;
b) запису матриці у файл.
Використовуючи описані підпрограми знайдіть суму та добуток двох
квадратних матриць та запишіть їх у два текстових файли.
"""

FILE1 = "t13_04_A.txt"
FILE2 = "t13_04_B.txt"
FILE3 = "t13_04_AaB.txt"
FILE4 = "t13_04_AmB.txt"


def read_matrix(filename):
    with open(filename) as f:
        matrix = []
        for line in f:
            row = [float(s) for s in line.split()]
            matrix.append(row)
    return matrix


def write_matrix(filename, matrix):
    with open(filename, "w") as f:
        for row in matrix:
            print(*row, file=f)


def create_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    return matrix


def add_matrix(m1, m2):
    n = len(m1)
    m3 = create_matrix(n)
    for i in range(n):
        for j in range(n):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3


def mult_matrix(m1, m2):
    n = len(m1)
    m3 = create_matrix(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m3[i][j] += m1[i][k] + m2[k][j]
    return m3


if __name__ == '__main__':
    A = read_matrix(FILE1)
    write_matrix(FILE2, A)
    B = read_matrix(FILE2)

    C = add_matrix(A, B)
    write_matrix(FILE3, C)

    D = mult_matrix(A, B)
    write_matrix(FILE4, D)
