class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1, idx2 = 0, 0
        result = ""
        flag = True
        
        while idx1 < len(word1) and idx2 < len(word2):
            if flag:
                result += word1[idx1]
                flag = False
                idx1 += 1
            else:
                result += word2[idx2]
                flag = True
                idx2 += 1
        
        if idx1 < len(word1):
            result += word1[idx1:]
        
        if idx2 < len(word2):
            result += word2[idx2:]
            
        return result
            