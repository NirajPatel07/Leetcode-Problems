class MyHashMap:

    def __init__(self):
        self.hashmap = []
        self.keys  = set()
        
    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.hashmap.append([key, value])
            self.keys.add(key)
            return
        else:
            for i, map in enumerate(self.hashmap):
                if map[0] == key:
                    map[1] = value

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        else:
            for i, map in enumerate(self.hashmap):
                if map[0] == key:
                    return map[1]

    def remove(self, key: int) -> None:
        if key in self.keys:
            for i, map in enumerate(self.hashmap):
                if map[0] == key:
                    self.hashmap.pop(i)
                    self.keys.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)