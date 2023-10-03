class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_gap = 0
        
        for i in range(1, len(nums)):
            max_gap = max(max_gap, abs(nums[i] - nums[i-1]))
            
        return max_gap