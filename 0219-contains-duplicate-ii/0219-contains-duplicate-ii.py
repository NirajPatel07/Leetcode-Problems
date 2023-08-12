class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        
        for i, n in enumerate(nums):
            if n in lookup and i-lookup[n] <= k:
                return True
            lookup[n] = i
        
        return False
                
            