class MyQueue:

    def __init__(self):
        self.st_front = []
        self.st_back = []

    def push(self, x: int) -> None:
        self.st_back.append(x)
        self.top = x

    def pop(self) -> int:
        if not self.st_front and not self.st_back:
            return -1

        if not self.st_front:
            while self.st_back:
                self.st_front.append(self.st_back.pop())
        return self.st_front.pop()

    def peek(self) -> int:
        if not self.st_front and not self.st_back:
            return -1

        if not self.st_front:
            while self.st_back:
                self.st_front.append(self.st_back.pop())
        return self.st_front[-1]

    def empty(self) -> bool:
        return not self.st_front and not self.st_back
        