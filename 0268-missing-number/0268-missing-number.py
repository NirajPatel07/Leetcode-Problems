class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = n*(n+1)/2
        return int(sum_n-sum(nums))