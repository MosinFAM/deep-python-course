class CustomMeta(type):
    def __new__(mcs, name, bases, class_dict):
        new_class_dict = {}
        for key, value in class_dict.items():
            if not (key.startswith('__') and key.endswith('__')):
                key = 'custom_' + key
            new_class_dict[key] = value
        return super().__new__(mcs, name, bases, new_class_dict)

    def __call__(cls, *args, **kwargs):
        def setattr_(self, key, value):
            if not (key.startswith('__') and key.endswith('__')):
                new_name = 'custom_' + key
                self.__dict__[new_name] = value
        cls.__setattr__ = setattr_

        new_object = super().__call__(*args, **kwargs)
        new_class_dict = {}
        for key, value in new_object.__dict__.items():
            if not (key.startswith('__') and key.endswith('__')):
                key = 'custom_' + key
            new_class_dict[key] = value
        new_object.__dict__ = new_class_dict
        return new_object


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

# inst = CustomClass()
# inst.dynamic = "added later"
# print(inst.custom_dynamic)
# print(inst.__dict__)
# # print(locals())
