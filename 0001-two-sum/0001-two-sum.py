class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating Dictonary for Lookup
        lookup = {}
        
        for i in range(len(nums)):
            # if target-n in lookup return n index and current index
            if target-nums[i] in lookup:
                return [lookup[target-nums[i]], i]
            lookup[nums[i]] = i
        
            