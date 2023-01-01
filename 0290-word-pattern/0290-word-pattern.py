class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(' ')):
            return False
        
        lookup = {}
        s = s.split(' ')
        
        for i in range(len(pattern)):
            if pattern[i] in lookup and lookup[pattern[i]] == s[i]:
                continue
            elif pattern[i] not in lookup and s[i] not in lookup.values():
                lookup[pattern[i]] = s[i]
            else:
                return False
        
        return True