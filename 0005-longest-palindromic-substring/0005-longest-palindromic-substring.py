class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        def check_palindrome(i, j, s):
            
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    return s[i+1:j]
                
                i -= 1
                j += 1
            
            return s[i+1:j]
        
        res = ''
        
        for i in range(len(s)-1):
            p1 = check_palindrome(i, i+1, s)
            p2 = check_palindrome(i, i, s)
            
            longest = ''
            if len(p1) > len(p2):
                longest = p1
            else:
                longest = p2
                
            if len(longest) > len(res):
                res = longest
        
        return res
                    