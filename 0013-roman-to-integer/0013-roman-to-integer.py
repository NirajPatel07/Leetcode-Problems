class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I":            1,
            "V":            5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000
        }
        
        s_integer = 0
        
        for i, c in enumerate(s):
            if i < len(s)-1 and lookup[s[i+1]] > lookup[s[i]]:
                s_integer -= lookup[c]
            else:
                s_integer += lookup[c]
        
        return s_integer
            