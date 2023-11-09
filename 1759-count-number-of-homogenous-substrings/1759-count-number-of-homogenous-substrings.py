class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0
        count = 0
        mod = 10 ** 9 + 7
        
        for i, char in enumerate(s):
            if i == 0 or s[i-1] == char:
                count += 1
            else:
                count = 1
            
            result += count
        
        return result % mod
            