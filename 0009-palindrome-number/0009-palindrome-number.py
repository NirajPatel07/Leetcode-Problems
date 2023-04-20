class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse_x = 0
        origin = x
        
        while x!= 0:
            reverse_x = (reverse_x * 10) + (x % 10)
            x //= 10
            
        return reverse_x == origin