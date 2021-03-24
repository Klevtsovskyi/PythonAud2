

import random


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

    def __iter__(self):
        return ProtectedDictIntIterator(self.dict)

    def keys(self):
        return iter(self)

    def values(self):
        return ProtectedDictIntIterator(self.dict.values())

    def items(self):
        return ProtectedDictIntIterator(self.dict.items())


class ProtectedDictIntIterator:

    def __init__(self, collection):
        self.collection = sorted(collection)
        self.cursor = 0

    def __next__(self):
        if self.cursor == len(self.collection):
            raise StopIteration
        item = self.collection[self.cursor]
        self.cursor += 1
        return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    d1 = ProtectedDictInt()

    for i in range(20):
        item = random.randint(0, 100)
        try:
            d1[item] = str(item)
        except ValueError:
            pass

    print(d1)

    for key in d1.keys():
        print(key, end=" ")
    print()

    it = iter(d1)
    while True:
        try:
            item = next(it)
            print(item, end=" ")
        except StopIteration:
            break
    print()

    for value in d1.values():
        print(value, end=" ")
    print()

    for key, value in d1.items():
        print("(", key, value, ")", end=" ")
    print()
