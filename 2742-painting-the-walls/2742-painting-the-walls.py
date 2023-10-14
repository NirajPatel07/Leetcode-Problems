class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * n + [0]
        
        for row in range(n - 1, -1, -1):
            new_dp = [0] * (n + 1)
            for col in range(n - 1, -1, -1):
                painter = cost[row] + (dp[col + time[row] + 1] if col + time[row] < n else 0)
                new_dp[col] = min(dp[col], painter)
            dp = new_dp
        return dp[0]