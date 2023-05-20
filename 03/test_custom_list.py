import unittest

from custom_list import CustomList


def compare(obj1, obj2):
    for index in range(len(max(obj1, obj2))):
        if obj1[index] != obj2[index]:
            return False
    return True


class TestCustomList(unittest.TestCase):
    def test_sum_and_difference(self):
        lst1 = CustomList([1, 2, 3, 4, 5, 6])
        lst2 = CustomList([99, 99, 99, 99])
        lst3 = CustomList([])
        lst4 = [1, 2, 3, 4, 5]
        lst5 = []

        # for index in range(len(lst1 + lst2))

        self.assertTrue(compare(lst1 + lst2, CustomList([100, 101, 102, 103, 5, 6])))
        self.assertTrue(compare(lst1 + lst4, CustomList([2, 4, 6, 8, 10, 6])))
        self.assertTrue(compare(lst1 + lst3, CustomList([1, 2, 3, 4, 5, 6])))
        self.assertTrue(compare(lst3 + lst5, CustomList([])))
        self.assertTrue(compare(lst4 + lst1, CustomList([2, 4, 6, 8, 10, 6])))
        self.assertTrue(compare(lst5 + lst1, CustomList([1, 2, 3, 4, 5, 6])))

        self.assertTrue(compare(lst1 - lst2, CustomList([-98, -97, -96, -95, 5, 6])))
        self.assertTrue(compare(lst1 - lst4, CustomList([0, 0, 0, 0, 0, 6])))
        self.assertTrue(compare(lst1 - lst3, CustomList([1, 2, 3, 4, 5, 6])))
        self.assertTrue(compare(lst3 - lst5, CustomList([])))
        self.assertTrue(compare(lst4 - lst1, CustomList([0, 0, 0, 0, 0, -6])))
        self.assertTrue(compare(lst5 - lst1, CustomList([-1, -2, -3, -4, -5, -6])))

        self.assertTrue(compare(lst1, CustomList([1, 2, 3, 4, 5, 6])))
        self.assertTrue(compare(lst2, CustomList([99, 99, 99, 99])))
        self.assertTrue(compare(lst3, CustomList([])))
        self.assertTrue(compare(lst4, [1, 2, 3, 4, 5]))
        self.assertTrue(compare(lst5, []))

    def test_comparison(self):
        lst1 = CustomList([1, 2, 3, 4, 5, 6])
        lst2 = CustomList([99, 99, 99, 99])
        lst3 = CustomList([])

        self.assertEqual(lst1 > lst2, False)
        self.assertEqual(lst1 < lst2, True)
        self.assertEqual(lst3 >= lst1, False)
        self.assertEqual(lst3 <= lst1, True)
        self.assertEqual(lst2 == lst1, False)
        self.assertEqual(lst1 != lst2, True)

        self.assertTrue(compare(lst1, CustomList([1, 2, 3, 4, 5, 6])))
        self.assertTrue(compare(lst2, CustomList([99, 99, 99, 99])))
        self.assertTrue(compare(lst3, CustomList([])))

    def test_str(self):
        lst = CustomList([10, 10, 10, 10, 10])

        self.assertTrue(compare(str(lst), 'Элементы списка [10, 10, 10, 10, 10] и их сумма 50'))
