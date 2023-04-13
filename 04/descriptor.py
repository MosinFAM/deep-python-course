class Control:
    @classmethod
    def verify(cls, value):
        if type(value) != int or value < 16:
            raise TypeError("mark should be integer and more than 15, otherwise, you didn't pass the Rybejnyi Kontrol'")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = value


class String:
    @classmethod
    def verify(cls, value):
        if type(value) != str:
            raise TypeError('value should be string')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = value


class Python:
    @classmethod
    def verify(cls, value):
        if value != 'Python':
            raise TypeError('value should be Python')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = value


class Data:
    mark = Control()
    name = String()
    language = Python()

    def __init__(self, mark, name, language):
        self.mark = mark
        self.name = name
        self.language = language


# x = Data(17, 'fasfs', 'Python')
# print(x.language)
