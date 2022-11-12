from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.data = SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        n = len(self.data)
        return (self.data[n//2] + self.data[(n-1)//2]) / 2