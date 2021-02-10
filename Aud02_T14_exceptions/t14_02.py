

def sum_digits(string):
    s = 0
    for char in string:
        try:
            n = int(char)
            s += n
        except ValueError:
            pass
    return s


if __name__ == '__main__':
    string = "vmkld4321=03kd93,cxa "
    print(sum_digits(string))
