class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        
        for i in range(len(s)):
            if s[i] in lookup:
                if lookup[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in lookup.values():
                    return False
                lookup[s[i]] = t[i]
        
        return True
                