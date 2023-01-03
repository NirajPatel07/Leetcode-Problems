class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0
        for i in range(len(strs[0])):
            curr_s = ''
            for j in range(len(strs)):
                curr_s += strs[j][i]
            if sorted(curr_s) != list(curr_s):
                c+=1
        
        return c
            
            