class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def recursion(nums, curr, idx):
            if idx >= len(nums):
                res.append(curr.copy())
                return
            
            recursion(nums, curr, idx+1)
            recursion(nums, curr + [nums[idx]], idx+1)
            
            
        
        recursion(nums, [], 0)
        return res