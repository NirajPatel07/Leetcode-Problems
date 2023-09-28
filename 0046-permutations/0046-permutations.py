class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, index):
            if index >= len(nums):
                result.append(nums.copy())
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(nums, index + 1)
                nums[index], nums[i] = nums[i], nums[index]
                
        result = []
        backtrack(nums, 0)
        return result