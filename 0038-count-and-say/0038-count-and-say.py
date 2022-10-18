class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return '1'
        
        res = ['1']
        for i in range(n-1):
            i = 0
            s = res[-1]
            curr_s = ''
            j = 0
            while i<len(s):
                c = 0
                while j<len(s) and s[i] == s[j]:
                    c+=1
                    j+=1
                curr_s += str(c)
                curr_s += str(s[i])
                i = j
                
            res.append(curr_s)
        
        return res[-1]
                
            
                