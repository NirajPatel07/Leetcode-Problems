class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def recursion(nums, index):
            if index == len(nums):
                if nums not in result:
                    result.append(nums.copy())
                return
            
            for i in range(len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                recursion(nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]
        
        recursion(nums, 0)
        return result