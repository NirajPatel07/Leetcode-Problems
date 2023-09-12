class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = Counter(s)
        seen = set()
        count = 0
        
        for key, freq in frequency.items():
            while freq > 0 and freq in seen:
                freq -= 1
                count += 1
            seen.add(freq)
            
        return count