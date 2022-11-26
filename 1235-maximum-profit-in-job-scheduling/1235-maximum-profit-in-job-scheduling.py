from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(arr)
        dp = [0] * n    # dp[i]: Maimum profit with 0~i-th items taken into consideration
        
        for i in range(n):
            s, e, p = arr[i]
            idx = bisect_right(arr, s, key=lambda x: x[1])  # Find the 1st item whose end_time is <= my start_time
            
            # 1. `take_i` means the maximum profit if i-th is one of the taken-job
            if idx == 0:
                take_i = p
            else:
                take_i = dp[idx - 1] + p
                
            # 2. Stick to the "definition" of dp[i], so we should apply knock-down strategy  -- max() function -- to dp[i]!
            dp[i] = take_i
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
        return max(dp)