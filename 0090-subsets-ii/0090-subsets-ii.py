class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def findSubsets(subset, index):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            findSubsets(subset + [nums[index]], index+1)
            
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            findSubsets(subset, index+1)
        
        result = []
        findSubsets([], 0)
        return result