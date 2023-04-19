class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        
        for i, n in enumerate(nums):
            if n in lookup:
                return [i, lookup[n]]
            else:
                lookup[target-n] = i
        
        return -1