

def amount_of_money(wallet, n):
    s = 0
    for i in range(1, n + 1):
        try:
            s += wallet[i] * i
        except KeyError:
            pass
    return s


if __name__ == '__main__':
    wallet = {100: 1, 50: 3, 25: 6, 10: 8, 5: 13, 2: 3, 1: 19}
    amount = amount_of_money(wallet, 100)
    print(amount)
