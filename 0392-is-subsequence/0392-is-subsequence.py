class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if not s:
            return True
        
        si = 0
        for i in range(len(t)):
            if s[si] == t[i]:
                si += 1
            if si == len(s):
                return True
            
        return si == len(s)