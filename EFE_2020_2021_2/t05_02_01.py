

class ProtectedDictIntError(KeyError):
    pass


class ProtectedDictInt:

    def __init__(self):
        self._dict = dict()

    def __len__(self):
        """ len(self)"""
        return len(self._dict)

    def __str__(self):
        """ str(self)"""
        return str(self._dict)

    def __setitem__(self, key, value):
        """ self[key] = value"""
        if not isinstance(key, int):
            raise ProtectedDictIntError("Ключ {} не є цілим числом".format(key))
        elif key in self._dict:
            raise ProtectedDictIntError("Ключ {} вже є в словнику".format(key))
        else:
            self._dict[key] = value

    def __getitem__(self, key):
        """ self[key]"""
        return self._dict[key]

    def __contains__(self, key):
        """ key in self"""
        return key in self._dict

    def __add__(self, other):
        """ self + other"""
        result = ProtectedDictInt()
        for key in self._dict:
            result[key] = self[key]
        if isinstance(other, ProtectedDictInt):
            for key in other._dict:
                result[key] = other[key]
        elif isinstance(other, tuple):
            if len(other) == 2:
                result[other[0]] = other[1]
            else:
                raise ProtectedDictIntError
        else:
            raise ProtectedDictIntError
        return result

    def __sub__(self, other):
        """ self - other"""
        del self._dict[other]

    def __iter__(self):
        return Iterator(sorted(self._dict.keys()))


class Iterator:

    def __init__(self, collection):
        self.collection = collection
        self.curr = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr += 1
        if self.curr == len(self.collection):
            raise StopIteration
        return self.collection[self.curr]


if __name__ == '__main__':
    d0 = ProtectedDictInt()
    d0[1] = "1"
    print("d0:", d0)
    d1 = d0 + (2, "2")
    print("d1 = d0 + (2, \"2\"):", d1)
    d2 = ProtectedDictInt()
    d2[3] = "3"
    print("d2:", d2)
    d3 = d0 + d2
    print("d3 = d0 + d2:", d3)
    d3 - 1
    print("d3:", d3)
    d3 += (5, 5)
    d3 += (2, 2)
    d3 += (10, 10)
    print("d3:", d3)

    for key in d3:
        print(key, end=" ")
