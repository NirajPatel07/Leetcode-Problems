class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        count = Counter(nums)
        
        if 1 in count.values(): return -1
        
        for key, value in count.items():
            if value % 3 == 0:
                res += value // 3
            else:
                res += value // 3 + 1
        
        return res
        
        