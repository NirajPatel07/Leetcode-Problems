class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, result, index):
            if index >= len(nums):
                result.append(nums.copy())
                
            for j in range(index, len(nums)):
                nums[index], nums[j] = nums[j], nums[index]
                backtrack(nums, result, index+1)
                nums[index], nums[j] = nums[j], nums[index]
                
        result = []
        index = 0
        backtrack(nums, result, index)
        
        return result