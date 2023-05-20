class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            del self.cache[self.order.pop(0)]
        self.cache[key] = value
        self.order.append(key)


# cache = LRUCache(2)
#
# cache.set("k1", "val1")
# cache.set("k2", "val2")
# cache.set("k3", "val3")
#
# print(cache.get("k4"))
