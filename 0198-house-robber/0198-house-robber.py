class Solution:
    def rob(self, nums: List[int]) -> int:
        odd = 0
        even = 0
        for i in range(len(nums)):
            num = nums[i]
            if i % 2 == 0:
                even = max(even + num, odd)
            else:
                odd = max(odd + num, even)
        return odd if odd > even else even