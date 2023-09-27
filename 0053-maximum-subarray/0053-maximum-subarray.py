class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        msf = 0
        
        for n in nums:
            msf += n
            
            if msf < n:
                msf = n
            
            res = max(res, msf)
        
        return res