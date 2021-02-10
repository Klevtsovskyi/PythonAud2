

def print_data(file):
    try:
        f = open(file)
        print(f.read())
    except FileNotFoundError:
        print("Файлу {} не існує".format(file))
    except PermissionError:
        print("Немає дозволу на відкриття файлу {}".format(file))
    else:
        f.close()


if __name__ == '__main__':
    while True:
        file = input("Введіть назву файлу: ")
        if file == "":
            break
        print_data(file)
