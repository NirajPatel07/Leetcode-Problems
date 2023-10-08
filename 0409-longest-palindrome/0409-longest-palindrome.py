class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        odd = False
        
        for key, value in count.items():
            if value % 2 == 0:
                result += value
            else:
                odd = True
                result += (value - 1)
                
        return result + 1 if odd else result