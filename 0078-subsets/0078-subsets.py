class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def find_subset(subset, index):
            if index == len(nums):
                result.append(subset.copy())
                return
            
            find_subset(subset, index+1)
            find_subset(subset + [nums[index]], index+1)
        
        find_subset([], 0)
        return result