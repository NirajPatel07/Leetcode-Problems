class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        origin = x
        rev_sum = 0
        
        while origin > 0:
            rev_sum = (rev_sum * 10) + (origin % 10)
            origin = origin // 10
        
        return x == rev_sum
        