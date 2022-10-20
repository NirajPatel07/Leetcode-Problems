class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for i in range(len(nums)):
            if target-nums[i] in lookup:
                return [lookup[target-nums[i]], i]
            lookup[nums[i]] = i
        
            