class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        
        if n < 3:
            return dp[n-1]
        
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
            
        return dp[-1]