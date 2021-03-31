

import random


class ProtectedDictIntError(KeyError):

    INAPPROPRIATE_KEY_TYPE = 0
    KEY_IS_ALREADY_IN_DICT = 1
    KEY_IS_MISSING_IN_DICT = 2
    UNDEFINED_OPERATION_ADD_FOR_TUPLE = 3
    UNDEFINED_OPERATION_ADD_FOR_TYPE = 4
    UNDEFINED_OPERATION_SUB_FOR_TYPE = 5
    KEY_IS_NOT_MISSING_IN_DICT = 6

    def __init__(self, err_code, *args):
        super().__init__()
        self.err_code = err_code
        self.args = args

    def __str__(self):
        message = "ProtectedDictIntError: "
        if self.err_code == ProtectedDictIntError.INAPPROPRIATE_KEY_TYPE:
            message += "Ключ не є цілим числом: "
        elif self.err_code == ProtectedDictIntError.KEY_IS_ALREADY_IN_DICT:
            message += "Ключ вже міститься в словнику: "
        elif self.err_code == ProtectedDictIntError.KEY_IS_MISSING_IN_DICT:
            message += "Ключ відсутній в словнику: "
        elif self.err_code == ProtectedDictIntError.UNDEFINED_OPERATION_ADD_FOR_TUPLE:
            message += "Операція + не визначена для кортежа довжини не 2: "
        elif self.err_code == ProtectedDictIntError.UNDEFINED_OPERATION_ADD_FOR_TYPE:
            message += "Операція + не визначена для даного типу: "
        elif self.err_code == ProtectedDictIntError.UNDEFINED_OPERATION_SUB_FOR_TYPE:
            message += "Операція - не визначена для даного типу: "
        elif self.err_code == ProtectedDictIntError.KEY_IS_NOT_MISSING_IN_DICT:
            message += "Ключ не міститься в словнику: "
        return message + str(self.args)


class ProtectedDictInt:

    def __init__(self):
        self.dict = dict()

    def __str__(self):
        return str(self.dict)

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise ProtectedDictIntError(
                ProtectedDictIntError.INAPPROPRIATE_KEY_TYPE,
                key
            )
        elif key in self.dict:
            raise ProtectedDictIntError(
                ProtectedDictIntError.KEY_IS_ALREADY_IN_DICT,
                key
            )
        else:
            self.dict[key] = value

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ProtectedDictIntError(
                ProtectedDictIntError.INAPPROPRIATE_KEY_TYPE,
                key
            )
        elif key not in self.dict:
            raise ProtectedDictIntError(
                ProtectedDictIntError.KEY_IS_MISSING_IN_DICT,
                key
            )
        else:
            return self.dict[key]

    def __contains__(self, key):
        if not isinstance(key, int):
            raise ProtectedDictIntError(
                ProtectedDictIntError.INAPPROPRIATE_KEY_TYPE,
                key
            )
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
            if len(other) == 2:  # self + (1, "1")
                result[other[0]] = other[1]
            else:  # self + (1, 1, 1)
                raise ProtectedDictIntError(
                    ProtectedDictIntError.UNDEFINED_OPERATION_ADD_FOR_TUPLE,
                    other
                )
        else:
            raise ProtectedDictIntError(
                ProtectedDictIntError.UNDEFINED_OPERATION_ADD_FOR_TYPE,
                type(other).__name__
            )
        return result

    def __sub__(self, other):
        result = ProtectedDictInt()

        if isinstance(other, int):
            if other not in self:
                raise ProtectedDictIntError(
                    ProtectedDictIntError.KEY_IS_NOT_MISSING_IN_DICT,
                    other
                )
            for key, value in self.dict.items():
                if key != other:
                    result[key] = value
        else:
            raise ProtectedDictIntError(
                ProtectedDictIntError.UNDEFINED_OPERATION_SUB_FOR_TYPE,
                type(other).__name__
            )
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
        except ProtectedDictIntError as e:
            print(e)

    print(d1)

    try:
        d1["one"] = 1
    except ProtectedDictIntError as e:
        print(e)

    try:
        a = d1[101]
    except ProtectedDictIntError as e:
        print(e)

    try:
        d2 = d1 + (1, 2, 3)
    except ProtectedDictIntError as e:
        print(e)

    try:
        d2 = d1 + "string"
    except ProtectedDictIntError as e:
        print(e)

    try:
        d2 = d1 - []
    except ProtectedDictIntError as e:
        print(e)

    try:
        d2 = d1 - 101
    except ProtectedDictIntError as e:
        print(e)
