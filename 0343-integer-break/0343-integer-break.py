class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        
        def find_breaks(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = find_breaks(i) * find_breaks(num-i)
                dp[num] = max(dp[num], val)
            
            return dp[num]
        
        return find_breaks(n)