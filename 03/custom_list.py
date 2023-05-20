from itertools import zip_longest


class CustomList(list):
    def __add__(self, other):
        return CustomList(
            x+y for x, y in zip_longest(self, other, fillvalue=0)
        )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return CustomList(
            x - y for x, y in zip_longest(self, other, fillvalue=0)
        )

    def __rsub__(self, other):
        return CustomList(
            y-x for x, y in zip_longest(self, other, fillvalue=0)
        )

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __str__(self):
        return f'Элементы списка {super().__str__()} и их сумма {sum(self)}'


data1 = CustomList([1, 1, 1, 1, 1])
data2 = CustomList([9, 9, 9, 9, 9])
data3 = [1, 1, 1, 1, 1] + data2
print(data3)
