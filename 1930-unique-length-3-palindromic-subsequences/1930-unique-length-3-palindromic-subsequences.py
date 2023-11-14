class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        position = {}
        
        for i, c in enumerate(s):
            if c in position:
                position[c][1] = i
            else:
                position[c] = [i, i]
                
        result = 0
        for i, j in position.values():
            count = set()
            for k in range(i+1, j):
                count.add(s[k])
            result += len(count)
        
        return result