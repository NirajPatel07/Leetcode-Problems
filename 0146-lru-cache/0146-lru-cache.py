class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.lru = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
            self.lru.append(key)
        else:
            element = self.lru[0]
            del self.cache[element]
            self.lru.remove(element)
            
            self.cache[key] = value
            self.lru.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)