class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        x = 1
        
        while x <= n:
            if x != n:
                x = x * 3
            else:
                return True
            
        return False