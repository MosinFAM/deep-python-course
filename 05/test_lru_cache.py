import unittest

from lru_cache import LRUCache


class TestCache(unittest.TestCase):
    def test_from_exercise(self):
        self.instance = LRUCache(2)
        self.instance.set("k1", "val1")
        self.instance.set("k2", "val2")

        self.assertEqual(self.instance.get("k3"), None)
        self.assertEqual(self.instance.get("k2"), "val2")
        self.assertEqual(self.instance.get("k1"), "val1")

        self.instance.set("k3", "val3")

        self.assertEqual(self.instance.get("k3"), 'val3')
        self.assertEqual(self.instance.get("k2"), None)
        self.assertEqual(self.instance.get("k1"), "val1")

    def test_one_capacity(self):
        self.instance = LRUCache(1)
        self.instance.set("k1", "val1")

        self.assertEqual(self.instance.get("k2"), None)
        self.assertEqual(self.instance.get("k1"), "val1")

        self.instance.set("k2", "val2")

        self.assertEqual(self.instance.get("k2"), 'val2')
        self.assertEqual(self.instance.get("k1"), None)

    def test_order_update(self):
        self.instance = LRUCache(2)
        self.instance.set("k1", "val1")
        self.instance.set("k2", "val2")

        self.assertEqual(self.instance.get("k3"), None)
        self.assertEqual(self.instance.get("k2"), "val2")

        self.instance.set("k3", "val3")

        self.assertEqual(self.instance.get("k3"), 'val3')
        self.assertEqual(self.instance.get("k2"), 'val2')
        self.assertEqual(self.instance.get("k1"), None)

    def test_update_value(self):
        self.instance = LRUCache(2)
        self.instance.set("k1", "val1")
        self.instance.set("k2", "val2")

        self.assertEqual(self.instance.get("k3"), None)
        self.assertEqual(self.instance.get("k2"), "val2")
        self.assertEqual(self.instance.get("k1"), "val1")

        self.instance.set("k2", "v2")
        self.instance.set("k3", "val3")

        self.assertEqual(self.instance.get("k3"), 'val3')
        self.assertEqual(self.instance.get("k2"), "v2")
        self.assertEqual(self.instance.get("k1"), None)
