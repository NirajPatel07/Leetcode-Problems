class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for i,n in enumerate(nums):
            rem = target-n
            if rem in lookup:
                return [i, lookup[rem]]
            lookup[n] = i
            
        return -1