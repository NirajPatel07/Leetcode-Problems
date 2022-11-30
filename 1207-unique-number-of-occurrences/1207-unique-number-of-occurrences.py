class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        if len(set(count.values())) != len(count):
            return False
        return True