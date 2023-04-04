import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def test_sum_and_difference(self):
        lst1 = CustomList([1, 2, 3, 4, 5, 6])
        lst2 = CustomList([99, 99, 99, 99])
        lst3 = CustomList([])
        lst4 = [1, 2, 3, 4, 5]
        lst5 = []

        self.assertEqual(lst1 + lst2, CustomList([100, 101, 102, 103, 5, 6]))
        self.assertEqual(lst1 + lst4, CustomList([2, 4, 6, 8, 10, 6]))
        self.assertEqual(lst1 + lst3, CustomList([1, 2, 3, 4, 5, 6]))
        self.assertEqual(lst3 + lst5, CustomList([]))
        self.assertEqual(lst4 + lst1, CustomList([2, 4, 6, 8, 10, 6]))
        self.assertEqual(lst5 + lst1, CustomList([1, 2, 3, 4, 5, 6]))

        self.assertEqual(lst1 - lst2, CustomList([-98, -97, -96, -95, 5, 6]))
        self.assertEqual(lst1 - lst4, CustomList([0, 0, 0, 0, 0, 6]))
        self.assertEqual(lst1 - lst3, CustomList([1, 2, 3, 4, 5, 6]))
        self.assertEqual(lst3 - lst5, CustomList([]))
        self.assertEqual(lst4 - lst1, CustomList([0, 0, 0, 0, 0, -6]))
        self.assertEqual(lst5 - lst1, CustomList([-1, -2, -3, -4, -5, -6]))

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
