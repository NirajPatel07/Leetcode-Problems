import random
class RandomizedSet:

    def __init__(self):
        self.s=set()

    def insert(self, val: int) -> bool:
        if val in self.s:return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.s))