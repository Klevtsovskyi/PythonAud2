

class ProtectedDictInt:

    def __init__(self):
        self.dict = dict()

    def __str__(self):
        return str(self.dict)

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Ключ {} не є типом {}"
                            .format(key, int.__name__))
        elif key in self.dict:
            raise ValueError("Ключ {} вже міститься в словнику"
                             .format(key))
        else:
            self.dict[key] = value

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Ключ {} не є типом {}"
                            .format(key, int.__name__))
        else:
            return self.dict[key]

    def __contains__(self, key):
        if not isinstance(key, int):
            raise TypeError("Ключ {} не є типом {}"
                            .format(key, int.__name__))
        else:
            return key in self.dict

    def __len__(self):
        return len(self.dict)

    def __add__(self, other):
        result = ProtectedDictInt()
        for key, value in self.dict.items():
            result[key] = value

        if isinstance(other, ProtectedDictInt):
            for key, value in other.dict.items():
                result[key] = value
        elif isinstance(other, tuple):
            if len(other) == 2:
                result[other[0]] = other[1]
            else:
                raise ValueError("Операція + не визначена для {} та {} довжини {}"
                                 .format(type(self).__name__,
                                         tuple.__name__,
                                         len(other)))
        else:
            raise TypeError("Операція + не визначена для {} та {}"
                            .format(type(self).__name__,
                                    type(other).__name__))
        return result

    def __sub__(self, other):
        result = ProtectedDictInt()

        if isinstance(other, int):
            if other not in self:
                raise KeyError("Ключ {} не міститься в словнику"
                               .format(other))
            for key, value in self.dict.items():
                if key != other:
                    result[key] = value
        else:
            raise TypeError("Операція - не визначена для {} та {}"
                            .format(type(self).__name__,
                                    type(other).__name__))
        return result


if __name__ == '__main__':
    d1 = ProtectedDictInt()
    print(d1)
    d1[123] = "123"
    d1[223] = "223"
    d1[323] = "323"
    print(d1)
    try:
        d1[123] = "321"  # Забронено!
    except ValueError as e:
        print(e)
    try:
        d1["abc"] = "cba"
    except TypeError as e:
        print(e)
    print(d1[123])
    if 123 in d1:
        print("123 міститься в словнику")
    print("Дожина словника: {}".format(len(d1)))

    d2 = ProtectedDictInt()
    d2[1] = "a"
    d2[2] = "b"

    print("d1:", d1)
    print("d2:", d2)

    d3 = d1 + d2
    print("d3 = d1 + d2:", d3)

    d4 = d3 + (3, "c")
    print("d4 = d3 + (3, \"c\"):", d4)

    try:
        d5 = d4 + "string"
    except TypeError as e:
        print(e)

    d6 = d4 - 123
    print("d6 = d4 - 123:", d6)
