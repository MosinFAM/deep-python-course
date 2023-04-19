import unittest

from lru_cache import LRUCache


class TestCustomMeta(unittest.TestCase):
    def setUp(self):
        self.instance = LRUCache(2)
        self.instance.set("k1", "val1")
        self.instance.set("k2", "val2")

    def test_meta(self):
        self.assertEqual(self.instance.get("k2"), 'val2')
        self.assertEqual(self.instance.get("k3"), None)

        self.instance.set("k3", "val3")
        self.assertEqual(self.instance.get("k3"), 'val3')
        self.assertEqual(self.instance.get("k1"), None)
