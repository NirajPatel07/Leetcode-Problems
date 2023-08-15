class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        
        while j < len(nums):
            if j<len(nums) and i<len(nums) and nums[j] != 0 and nums[i]==0 and j > i:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                while i<len(nums) and nums[i] != 0:
                    i+=1
            j += 1
        
        return nums
        