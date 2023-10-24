class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permutations(nums, index):
            if index == len(nums):
                result.append(nums.copy())
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                permutations(nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]
        
        result = []
        permutations(nums, 0)
        return result