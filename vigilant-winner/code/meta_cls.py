

class AlphabetEncode(dict):

    def __init__(self, existing=None):
        super().__init__()
        if existing is not None:
            for k, v in existing:
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise ValueError(f'{key} is already defined')
        super().__setitem__(key, value)


class ProbihitDuplicate(type):

    @classmethod
    def __prepare__(cls, name, bases):
        return AlphabetEncode()


class Dodgy(metaclass=ProbihitDuplicate):

    def method(self):
        return "first method"

    def method(self):
        return "second method"

dodgy = Dodgy()
alpha_encode = AlphabetEncode()
alpha_encode['A'] = 1
alpha_encode['B'] = 2
