class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sorted_count = dict(sorted(c.items(), key=lambda item: -item[1]))
        
        res = ""
        for key in sorted_count:
            res += key*sorted_count[key]
        
        return res
        