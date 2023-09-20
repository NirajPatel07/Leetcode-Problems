class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum = 0
        max_window = -1
        l = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while l <= r and curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            
            if curr_sum == target:
                max_window = max(max_window, r-l+1)
                
        return -1 if max_window == -1 else len(nums) - max_window
                