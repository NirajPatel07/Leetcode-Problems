from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])  
        n = len(jobs)
        
        dp = [0] * n  
        
        for i in range(n):
            # Binary search to find the latest job that doesn't overlap
            prev_job_index = self.binarySearch(jobs, i)
            
            # Maximum profit without including the current job
            without_current = dp[i - 1] if i > 0 else 0
            dp[i] = max(without_current, dp[prev_job_index] + jobs[i][2])
        
        return dp[-1]
    
    def binarySearch(self, jobs, current_index):
        low, high = 0, current_index - 1
        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[current_index][0]:
                if jobs[mid + 1][1] <= jobs[current_index][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1
        return -1