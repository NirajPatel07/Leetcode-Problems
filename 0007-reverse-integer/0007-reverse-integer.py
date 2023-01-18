class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        n=abs(x)
        
        while n:
            reverse = reverse*10 + n%10
            n = n//10
        
        if reverse > 2**31:
            return 0
        if x<0:
            return -reverse
        return reverse