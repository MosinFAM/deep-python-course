import unittest

from descriptor import Data


class TestDescriptor(unittest.TestCase):
    def setUp(self):
        self.instance = Data(22, 'deep-python-course', 'Python')

    def test_data(self):
        self.assertEqual(self.instance.mark, 22)
        with self.assertRaises(TypeError):
            self.instance.mark = 15
        self.assertEqual(self.instance.mark, 22)
        with self.assertRaises(TypeError):
            self.instance.mark = 'Python'
        self.assertEqual(self.instance.name, 'deep-python-course')
        with self.assertRaises(TypeError):
            self.instance.name = 143
        self.assertEqual(self.instance.language, 'Python')
        with self.assertRaises(TypeError):
            self.instance.language = 'Java'
        self.instance.mark = 87
        self.assertEqual(self.instance.mark, 87)
