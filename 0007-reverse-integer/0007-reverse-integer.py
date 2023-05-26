class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            x = x * -1
            negative = True
            
        rev_num = 0
        
        while x > 0:
            rev_num = rev_num * 10 + x%10
            x = x//10
            
        if negative:
            rev_num  = -1 * rev_num
        
        if rev_num > (2**31 - 1) or rev_num < (-1 * 2**31 - 1):
            return 0
        
        return rev_num