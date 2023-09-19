class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for k, v in count.items():
            if v > 1:
                return k
        
        return -1