class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for s in strs[1:]:
            
            i, j = 0, 0
            while i < len(prefix) and j < len(s):
                if prefix[i] != s[j]:
                    break
                
                i += 1
                j += 1
            
            prefix = prefix[:i]
        
        return prefix