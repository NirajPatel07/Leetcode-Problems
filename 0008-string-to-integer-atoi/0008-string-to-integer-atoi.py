class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        sign = 1
        if s and s[0] == '-':
            sign = -1
        
        num = ''
        for i,c in enumerate(s):
            if i==0 and c in '-+':
                continue
            elif c.isnumeric():
                num += c
            else:
                break
        
        if not num:
            return 0
        
        num = int(num) * sign
        
        if num > (2**31 -1): return 2**31 - 1
        if num < (-2 ** 31): return -2 ** 31
        
        return num
        