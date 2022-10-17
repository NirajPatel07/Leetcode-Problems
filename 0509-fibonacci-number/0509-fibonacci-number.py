class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        if n == 0 or n == 1:
            return n
        res = 0
        for i in range(n-1):
            res = f0+f1
            f0 = f1
            f1 = res
        return res