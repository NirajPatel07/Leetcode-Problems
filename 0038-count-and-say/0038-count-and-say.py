class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        def say(s):
            res = ''
            i = 0
            
            while i < len(s):
                count = 1
                while i+1 < len(s) and s[i+1] == s[i]:
                    count += 1
                    i += 1
                res += (str(count) + s[i])
                i += 1
                
            return res
        
        s = '1'
        for i in range(n-1):
            s = say(s)
        
        return s