class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sum_ = 0
        localMax = 0
        localMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        for n in nums:
            localMax = max(n, localMax + n)
            localMin = min(n, localMin + n)
            sum_ += n
            maxSum = max(localMax, maxSum)
            minSum = min(minSum, localMin)
        
        return maxSum if sum_ == minSum else max(maxSum, sum_ - minSum)