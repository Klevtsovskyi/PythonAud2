

def run():
    exceptions = {}
    while True:
        string = input()
        if string == "досить":
            break
        try:
            n = int(string)
            if n < 0:
                raise TypeError("TypeError: {} < 0".format(n))
            elif n > 9:
                raise RuntimeError("RuntimeError: {} > 9".format(n))
            else:
                raise ValueError("ValueError: 0 <= {} <= 9".format(n))
        except Exception as e:
            name = type(e).__name__
            exceptions[name] = exceptions.get(name, 0) + 1
    return exceptions


if __name__ == '__main__':
    exceptions = run()
    print("Виключення, які були ініційовані:")
    for key, word in exceptions.items():
        print(key, ":", word)
