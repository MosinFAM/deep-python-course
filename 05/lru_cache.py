from collections import deque


class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.cache_list = deque()

    def get(self, key):
        for element in self.cache_list:
            if key in element:
                self.cache_list.remove(element)
                self.cache_list.appendleft(element)
                return element[1]
        return None

    def set(self, key, value):
        element = key, value
        self.cache_list.appendleft(element)
        if len(self.cache_list) > self.limit:
            self.cache_list.pop()


# cache = LRUCache(2)
#
# cache.set("k1", "val1")
# cache.set("k2", "val2")
# cache.set("k3", "val3")
#
# print(cache.get("k2"))
