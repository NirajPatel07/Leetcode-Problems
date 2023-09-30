class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def find_subset(subset, i):
            if i >= len(nums):
                result.append(subset)
                return
            
            find_subset(subset, i+1)
            find_subset(subset + [nums[i]], i+1)
        
        result = []
        find_subset([], 0)
        
        return result