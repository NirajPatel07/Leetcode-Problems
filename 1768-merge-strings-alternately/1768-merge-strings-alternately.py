class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        result = ""
        flag = True
        
        while idx < len(word1) and idx < len(word2):
            result += word1[idx]
            result += word2[idx]
            idx += 1
        
        if idx < len(word1):
            result += word1[idx:]
        
        if idx < len(word2):
            result += word2[idx:]
            
        return result
            