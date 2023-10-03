class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        lookup = {}
        count = 0
        
        for n in nums:
            if n in lookup:
                count += lookup[n]
                lookup[n] += 1
            else:
                lookup[n] = 1
                
        return count