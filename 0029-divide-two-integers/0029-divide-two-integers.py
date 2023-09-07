class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 or divisor < 0:
            sign = -1
        else:
            sign = 1
            
        dividend, divisor = abs(dividend), abs(divisor)
        
        while dividend >= divisor:
            tmp = divisor
            mul = 1
            while dividend >= tmp:
                dividend -= tmp
                res += mul
                tmp += tmp
                mul += mul
        
        return min(res * sign, 2147483647)