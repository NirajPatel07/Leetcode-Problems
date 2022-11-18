class Solution:
    def isUgly(self, n: int) -> bool:
        
        prime_factors = [2, 3, 5]
        
        if n <= 0:
            return False
        
        for pf in prime_factors:
            while n%pf == 0:
                n = n//pf
        
        return n == 1