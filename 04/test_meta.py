import unittest

from meta import CustomClass


class TestCustomMeta(unittest.TestCase):
    def setUp(self):
        self.instance = CustomClass()

    def test_meta(self):
        self.assertEqual(self.instance.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.instance.x

        self.assertEqual(self.instance.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.instance.line()

        self.assertEqual(self.instance.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.instance.val

        self.instance.dynamic = "added later"
        self.assertEqual(self.instance.custom_dynamic, "added later")
        with self.assertRaises(AttributeError):
            self.instance.dynamic
