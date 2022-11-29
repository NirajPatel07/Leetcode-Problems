import random

class RandomizedSet:

    def __init__(self):
        self.sets = set()

    def insert(self, val: int) -> bool:
        if val in self.sets : return False
        self.sets.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.sets:
            self.sets.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.sets))