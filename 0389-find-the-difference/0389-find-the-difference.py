class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = Counter(t)-Counter(s)
        return "".join(res.keys())