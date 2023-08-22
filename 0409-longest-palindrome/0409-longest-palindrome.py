class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        
        res = 0
        flag = False
        
        for c in count:
            if count[c] % 2 == 0:
                res += count[c]
            elif count[c] > 2:
                res += (count[c] - (count[c]%2))
            
            if count[c] % 2 == 1:
                flag = True
                
        if flag:
            res += 1
            
        return res