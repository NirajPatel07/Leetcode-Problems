class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in lookup:
                return [i, lookup[remaining]]
            else:
                lookup[nums[i]] = i
        
        return -1