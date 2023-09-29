class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        for i in range(0, len(nums)-1):
            if nums[i] < nums[i + 1] and nums[0] >= nums[-1]:
                return False
            if nums[i] > nums[i + 1] and nums[0] <= nums[-1]:
                return False
            
        return True