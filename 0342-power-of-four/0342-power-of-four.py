class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        
        compare = 4
        while compare < n:
            compare *= 4
            
        return compare == n