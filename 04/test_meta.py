import unittest

from meta import CustomClass


class TestCustomMeta(unittest.TestCase):
    def test_meta(self):
        self.assertEqual(CustomClass.custom_x, 50)
        with self.assertRaises(AttributeError):
            CustomClass.x

        self.inst = CustomClass()

        self.assertEqual(self.inst.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.inst.x

        self.assertEqual(self.inst.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.inst.line()

        self.assertEqual(self.inst.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.inst.val

        self.inst.dynamic = "added later"
        self.assertEqual(self.inst.custom_dynamic, "added later")
        with self.assertRaises(AttributeError):
            self.inst.dynamic
