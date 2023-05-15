class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in lookup:
                return [i, lookup[rem]]
            else:
                lookup[nums[i]] = i
        
        return -1