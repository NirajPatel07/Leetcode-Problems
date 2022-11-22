class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        num = int(pow(n, 0.5))
        lists = [pow(i,2) for i in range(1, num + 1)]
        dp[0] = 0
        
        for i in range(1, n + 1):
            nums = []
            for j in range(len(lists)):
                idx = i - lists[j]
                if idx >= 0:
                    nums.append(dp[idx])
            
            dp[i] = min(nums) + 1
        
        return dp[-1]