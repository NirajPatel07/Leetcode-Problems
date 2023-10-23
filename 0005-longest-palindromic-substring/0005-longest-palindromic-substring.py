class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        def palindrome(i, j, s):
            
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    return s[i+1:j]
                
                i -= 1
                j += 1
            
            return s[i+1:j]
        
        result = ""
        for i in range(len(s)-1):
            string1 = palindrome(i, i+1, s)
            string2 = palindrome(i, i, s)
            
            longest = ""
            if len(string1) > len(string2):
                longest = string1
            else:
                longest = string2
                
            if len(longest) > len(result):
                result = longest
                
        return result