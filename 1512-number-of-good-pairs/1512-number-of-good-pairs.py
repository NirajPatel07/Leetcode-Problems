class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        lookup = Counter(nums)
        count = 0
        
        for k, v in lookup.items():
            count += v * (v-1) // 2
            
        return count